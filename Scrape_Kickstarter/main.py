import os
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
from datetime import datetime, timedelta
import time

HOST = "https://webrobots.io/kickstarter-datasets/"

projects = {"name": [], # 專案名稱
            "blurb": [], # 專案描述
            "creator": [], # 專案發起人
            "currency": [], # 貨幣
            "goal": [], # 目標金額
            "usd_goal": [], # 目標金額(usd)，透過目標金額 * "usd_exchange_rate"
            "pledged": [], # 募得金額
            "usd_pledged": [], # 募得金額(usd)
            "state": [], # 達標與否
            "country": [], # 專案國家
            "location": [], # 專案地區
            "category": [], # 專案類別
            "created_at": [], # 專案提交時間
            "launched_at": [], # 專案過審發布時間
            "deadline": [], # 專案結束時間
            # "first": [], # 是否首次發起
            }

def scroll_to_bottom(driver):
    SCROLL_PAUSE_TIME = 0.9

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scrape_json():
    driver = webdriver.Chrome("./chromedriver.exe")

    driver.get(HOST)
    driver.maximize_window()

    scroll_to_bottom(driver)

    year_ul = 5
    while year_ul <= 9:
        try:
            month_li = 1
            while True:
                try:
                    driver.find_element(By.XPATH, f'//*[@id="post-4793"]/div/div/div/div/div/div[1]/ul[{year_ul}]/li[{month_li}]/a[1]').click()
                    print(f"Scrape {year_ul}-{month_li}...")

                except Exception as e:
                    print(e)
                    break
                month_li += 1

        except Exception as e:
            break
        year_ul += 1

    driver.close()

def merge_json():
    for file in tqdm(os.listdir("./data/json")):
        with open(f"./data/json/{file}", "r", encoding="utf-8") as f:
            projects_info = f.read().split('\n')

            print(f"Now extract {file} ing...\nThis file have {len(projects_info)} data")

            extract(projects_info)

def extract(projects_info):
    """Extract data from the scrape results"""
    l = len(projects["name"])

    for project_info in projects_info[:-1]:
        project_info = json.loads(project_info)["data"]
        
        projects["name"].append(project_info.get("name"))
        projects["blurb"].append(project_info.get("blurb"))
        projects["creator"].append(project_info.get("creator", {"name": 0})["name"])
        projects["currency"].append(project_info.get("currency"))

        goal_ = project_info.get("goal") or 0
        usd_exchange_rate_ = project_info.get("usd_exchange_rate") or 1
        projects["goal"].append(goal_)
        projects["usd_goal"].append(goal_ * usd_exchange_rate_)

        projects["pledged"].append(project_info.get("pledged"))
        projects["usd_pledged"].append(project_info.get("usd_pledged"))
        projects["country"].append(project_info.get("country", "US"))
        projects["location"].append(project_info.get("location", {"state": "UK"})["state"])
        projects["category"].append(project_info.get("category", {"name": 0})["name"])
        projects["state"].append(project_info.get("state"))
        projects["created_at"].append(datetime.fromtimestamp(project_info.get("created_at")))
        projects["launched_at"].append(datetime.fromtimestamp(project_info.get("launched_at")))
        projects["deadline"].append(datetime.fromtimestamp(project_info.get("deadline")))

    print(f'Extracted {len(projects["name"]) -l} ...')

def transform(projects) -> pd.DataFrame:
    df_projects = pd.DataFrame(projects)

    df_projects = df_projects.drop_duplicates("name")

    date_now = datetime.now()
    df_projects = df_projects[(date_now - df_projects["deadline"]) <= timedelta(days=3650)]

    df_projects["first"] = df_projects.groupby('creator')['creator'].transform('count') == 1

    return df_projects

def load(df_projects) -> None:
    df_projects.to_csv("./data/kickstarter.csv", mode="a", header=False, index=False)

if __name__ == "__main__":
    scrape_json()

    merge_json()

    df_projects = transform(projects)

    load(df_projects)
