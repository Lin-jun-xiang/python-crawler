import cloudscraper
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta

def scraper_(page: int):
    """
    ex: https://www.kickstarter.com/discover/advanced?sort=popularity&seed=2794782&page=1
    
    Description
    -----------
    * page=1~n

    Scrape these information for each project as following:
    1. project name : name/slug
    2. project 發起人
    3. 是否第一次發起
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

    return soup.find_all("div", {"class": "js-react-proj-card grid-col-12 grid-col-6-sm grid-col-4-lg"})

a = datetime.datetime.fromtimestamp(1277052802)

now = datetime.datetime.now()

print((now-a) <= datetime.timedelta(days=365*10))

    
def extract(projects_info_html):
    """Extract data from the scrape results"""

    projects = {"name": [], # 專案名稱
                "blurb": [], # 專案描述
                "creator": [], # 專案發起人
                "first": [], # 是否初次發起，透過 urls.api.user.created_projects_counts 得知
                "currency": [], # 貨幣
                "goal": [], # 目標金額
                "usd_goal": [], # 目標金額(usd)，透過目標金額 * "usd_exchange_rate"
                "pledged": [], # 募得金額
                "usd_pledged": [], # 募得金額(usd)
                "disable_communication": [], # 結束募款是否
                "country": [], # 專案國家
                "location": [], # 專案地區
                "category": [], # 專案類別
                "created_at": [], # 專案提交時間
                "launched_at": [], # 專案過審發布時間
                "deadline": [], # 專案結束時間
                }

    date_now = datetime.now()

    for project_info_html in projects_info_html:
        project_info = json.loads(project_info_html["data-project"])

        if datetime.fromtimestamp(project_info["deadline"]) - date_now <= timedelta(days=365*10):
            
        
            projects["name"].append(project_info["name"])
            projects["blurb"].append(project_info["blurb"])
            projects["creator"].append(project_info["creator"]["name"])
            projects["currency"].append(project_info["currency"])
            projects["goal"].append(project_info["goal"])
            projects["usd_goal"].append(project_info["goal"] * project_info["usd_exchange_rate"])
            projects["pledged"].append(project_info["pledged"])
            projects["usd_pledged"].append(project_info["usd_pledged"] * project_info["usd_exchange_rate"])
            projects["country"].append(project_info["country"])
            projects["location"].append(project_info["location"]["state"])
            projects["category"].append(project_info["category"]["name"])

            # projects["first"].append(project_info["creator"]["urls"]["api"][""])
            projects["disable_communication"].append(project_info[""])



    



