import cloudscraper
from bs4 import BeautifulSoup
import json, re

def scraper_(page: int):
    """
    ex: https://www.kickstarter.com/discover/advanced?sort=popularity&seed=2794782&page=1
    
    Description
    -----------
    * page=1~n

    Scrape these information for each project as following:
    1. project name : name/slug
    2. project 發起人
    3. 是否第一次發起 *
    4. 地區
    5. 專案類別
    6. 達標與否
    7. 募資目標金額
    8. 實際募得金額
    9. 專案開始時間 *
    10. 專案結束時間 *
    """
    scraper = cloudscraper.create_scraper()

    res = scraper.get(f"https://www.kickstarter.com/discover/advanced?sort=newest&seed=2794782&page={page}")

    soup = BeautifulSoup(res.text)

    projects = {"project_name": [], # 專案名稱
                "project_blurb": [], # 專案描述
                "project_sponsor": [], # 專案發起人
                "project_first": [], # 是否初次發起，透過 urls.api.user.created_projects_counts 得知
                "project_currency": [], # 貨幣
                "project_goal": [], # 目標金額
                "project_usd_goal": [], # 目標金額(usd)，透過目標金額 * "usd_exchange_rate"
                "project_pledged": [], # 募得金額
                "project_usd_pledged": [], # 募得金額(usd)
                "project_disable_communication": [], # 結束募款是否
                "project_country": [], # 專案國家
                "project_location": [], # 專案地區
                "project_category": [], # 專案類別
                }

    projects_info_html = soup.find_all("div", {"class": "js-react-proj-card grid-col-12 grid-col-6-sm grid-col-4-lg"})
    
    a = projects_info_html[1]["data-project"]


    

# cloudflare v2 captcha : https://stackoverflow.com/questions/74352220/cloudscraper-exceptions-cloudflarechallengeerror-detected-a-cloudflare-version 

