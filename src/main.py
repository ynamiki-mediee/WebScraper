#!/usr/bin/env python3
# test script for playwright
# 1. access to google.com
# 2. search "pokemon"
# 3. get the search result
# 4. save the result to csv file

import csv
import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    word = "pokemon"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # 1. access to google.com
        print("access to google.com")
        await page.goto("https://google.com")
        await page.wait_for_timeout(3000)

        # 2. search the target word
        print(f"searching `{word}`...")
        await page.fill('input[name="q"]', word)
        await page.press('input[name="q"]', 'Enter')
        await page.wait_for_timeout(3000)

        # 3. get the search result
        print("get the search result")
        search_results = await page.query_selector_all(".g")
        results = []
        for result in search_results:
            title = await result.query_selector(".LC20lb")
            link = await result.query_selector("a")
            if title and link:
                title_text = await title.inner_text()
                link_href = await link.get_attribute("href")
                results.append([title_text, link_href])

        # 4. create the csv file and save the result to ./data/{word}.csv
        print(f"save the result to ./data/{word}.csv")
        file_path = f"./data/{word}.csv"
        assert os.path.isfile(file_path) == False, f"Path {file_path} is a folder, not a file."
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["title", "link"])
            writer.writerows(results)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
