import cloudscraper
from bs4 import BeautifulSoup
import json, re

def scraper_(page: int):
    """
    https://www.kickstarter.com/discover/advanced?google_chrome_workaround&staff_picks=1&sort=popularity&seed=2794782&page=1
    
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
    9. 專案開始時間
    10. 專案結束時間
    """
    scraper = cloudscraper.create_scraper()

    res = scraper.get(f"https://www.kickstarter.com/discover/advanced?google_chrome_workaround&staff_picks=1&sort=popularity&seed=2794782&page={page}")

    soup = BeautifulSoup(res.text)

    data = re.sub(
        r'(?<="description" : )"(.*?)"(?=,\s+")',
        lambda g: json.dumps(g.group(1)),
        res.text,
        flags=re.S,
    )

    data = json.loads(data)

# cloudflare v2 captcha : https://stackoverflow.com/questions/74352220/cloudscraper-exceptions-cloudflarechallengeerror-detected-a-cloudflare-version 