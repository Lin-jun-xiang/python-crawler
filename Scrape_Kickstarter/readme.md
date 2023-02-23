# Scrape-Kickstarter
`Kickstarter`, `Python`, `Selenium`, `Cleanup`

### Python Selenium with chromeDriver

1. pip require module

```python
pip install -r requirements.txt
```

2. download chromeDriver

> 1. Go to : https://chromedriver.chromium.org/
> 2. Choose the .exe (ex: https://chromedriver.storage.googleapis.com/index.html?path=108.0.5359.71/)
> 3. Remember the .exe version should according to your chrome version (chrome://settings/help)
> 4. Put the driver.exe in project folder - dcard/driver

3. Using `scrape_json` function to download the `json` file from `webrobots.io`

4. Move all the json file to specific folder

5. Using `merge_json` function and `extract` function to extract information we want

6. Using `transform` function to cleanup data

7. write to `csv`
