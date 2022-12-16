import pandas as pd
import requests
from newsapi import NewsApiClient

def scrape_NYT(apikey : str) -> pd.DataFrame:
        year, month = "1895", "6"
        
        query_url = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={apikey}"

        response = requests.get(query_url)

        response = response.json()["response"]["docs"]

        news = {"platform": [],
                "title": [],
                "date": [],
                "url": []}

        for i in range(len(response)):
                news["title"].append(response[i]["headline"]["main"])
                news["date"].append(response[i]["pub_date"])
                news["url"].append(response[i]["web_url"])
                news["platform"].append("NYC")

        df = pd.DataFrame(news)

        return df

def scrape_API(apikey : str, query_key : str) -> pd.DataFrame:
        news = {"platform": [],
                "title": [],
                "date": [],
                "url": []}

        newsapi = NewsApiClient(api_key=apikey)

        for q in query_key:
                res_newsapi = newsapi.get_everything(q=q)
                new = res_newsapi["articles"]
                for i in range(len(res_newsapi["articles"])):
                        news["title"].append(new[i]["title"])
                        news["date"].append(new[i]["publishedAt"])
                        news["url"].append(new[i]["url"])
                        news["platform"].append(new[i]["source"]["name"])

        df = pd.DataFrame(news)

        return df

def scrape_BBC() -> pd.DataFrame:
        HOST = "https://www.bbc.com/news/"

        news = {"platform": [],
                "title": [],
                "date": [],
                "url": []}

        climate_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2Fe6369e45-f838-49cc-b5ac-857ed182e549%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        war_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2Fd0b3af0d-c4e5-4bbf-a3ec-3e28d82589a8%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        cor_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2F63b2bbc8-6bea-4a82-9f6b-6ecc470d0c45%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        world_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2F8467c0e0-584b-41de-9682-756b311216b5%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F1%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        asia_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2F070fca6a-b5c7-4b7f-8834-1c989fd40297%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        uk_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2F082101b1-72b1-4e45-943d-29d6dc6f97b4%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        bus_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2F19a1d11b-1755-4f97-8747-0c9534336a47%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        tech_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2Fe745fc56-51bf-46b5-9b74-f0f529ea4d8e%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        science_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2F0e18053e-731e-400a-a5b4-0f4088c74fd0%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        art_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2F7359a091-bee5-4927-8e96-bae36add5aa8%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]
        health_url = [f"https://push.api.bbci.co.uk/batch?t=%2Fdata%2Fbbc-morph-lx-commentary-data-paged%2Fabout%2Fa5a85236-f96d-477c-acfb-b236fcddf65c%2FisUk%2Ffalse%2Flimit%2F20%2FnitroKey%2Flx-nitro%2FpageNumber%2F{i}%2Fversion%2F1.5.6?timeout=5" for i in range(1, 51)]

        urls = [climate_url,
                war_url,
                cor_url,
                world_url,
                asia_url,
                uk_url,
                bus_url,
                tech_url,
                science_url,
                art_url,
                health_url]

        for url_ in urls:
                for url in url_:
                        response = requests.get(url)
                        res = response.json()["payload"][0]["body"]["results"]
                        for r in res:
                                try:
                                        print("Scrap BBC")
                                        news["url"].append(HOST + r["url"])
                                        news["title"].append(r["title"])
                                        news["date"].append(r["dateAdded"])
                                except:
                                        pass

        news["platform"] = "BBC"

        df = pd.DataFrame(news)

        return df