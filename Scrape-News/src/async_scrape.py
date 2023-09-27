import httpx
import pandas as pd
import asyncio

async def scrape(s: int = 0, e: int = 10000) -> pd.DataFrame:
    async with httpx.AsyncClient() as client:
        # CNN
        news = {"platform": [],
                "title": [],
                "date": [],
                "url": []}

        # 非同步函數來爬取CNN
        async def foo(i: int):
            try:
                response = await client.get(f"https://search.api.cnn.io/content?q=news&size=50&from={i}")
                response.raise_for_status()
                data = response.json()["result"]
                news["title"] += [x["headline"] for x in data]
                news["url"] += [x["url"] for x in data]
                news["date"] += [x["lastPublishDate"] for x in data]

                print("正在爬取 CNN...")
            except Exception as e:
                print(f"錯誤: {str(e)}")

        # 創建任務列表
        tasks = [foo(i) for i in range(s, e, 11)]

        # 異步執行任務
        await asyncio.gather(*tasks)

        news["platform"] = "CNN"

        df = pd.DataFrame(news)

        return df

async def main():
    df = await scrape()
    print(df)

if __name__ == "__main__":
    asyncio.run(main())
