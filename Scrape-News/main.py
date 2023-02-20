from src import *
import pandas as pd

# Get the CNN
# Set the page range
df_cnn = scrape()

# Get the BBC
df_bbc = scrape_BBC()

# Get the NYT, others...
df_nyt = scrape_NYT(apikey = "p3PHHaCPF6P5h94tLGFp3lRaIXbIY4wF")

# This query key just a example, change you want
query_key = ["asia", "us", "bitcoin", "data", "science", "car", "uk", "world", "teacher", "kill", "foot", "ball", "1", "2", "3", "english", "already", "chance", "door"]

df_others = scrape_API('927e8b0a15bd4539891ff4c86c812a8b',
                        query_key)

# Concate
df_output = pd.concat([df_cnn,
                        df_nyt,
                        df_others,
                        df_bbc
                        ],
                        axis=0)

# Drop duplications
df_output.drop_duplicates(["url", "title"], inplace=True)

# Create order column
df_output["orders"] = [i for i in range(1, len(df_output)+1)]

df_output["date"] = df_output["date"].apply(lambda x: str(x)[:10])

# Write to file
df_output.to_csv("news.csv", index=False, encoding="utf_8_sig")
