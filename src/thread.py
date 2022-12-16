import cloudscraper
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool

def scrape(s : int=0, e : int=10000) -> pd.DataFrame:
    scraper = cloudscraper.create_scraper()
    
    # CNN
    news = {"platform": [],
            "title": [],
            "date": [],
            "url": []}

    # Thread
    def foo(i : int):
        try:
            res = scraper.get(f"https://search.api.cnn.io/content?q=news&size=50&from={i}")
            news["title"] += [x["headline"] for x in res.json()["result"]]
            news["url"] += [x["url"] for x in res.json()["result"]]
            news["date"] += [x["lastPublishDate"] for x in res.json()["result"]]

            print("Scrap CNN...")
        except:
            pass

    with ThreadPool(16) as pool:
        pool.map(foo, range(s, e, 11))

    news["platform"] = "CNN"

    df = pd.DataFrame(news)

    return df
