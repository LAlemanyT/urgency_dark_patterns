from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import os

def scrape_page(url, title):
    #Home Page
    os.mkdir(title)
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    #driver.get("http://selenium.dev")
    print(f"Scraping: {url}")
    driver.get(url)
    time.sleep(3)
    driver.save_screenshot(f"{title}/home.png")
    elems = driver.find_elements(By.TAG_NAME, "a")
    links_from_home = []
    for elem in elems:
        href = elem.get_attribute('href')
        if href is not None:
            links_from_home.append(href)
            #print(href)
    to_visit = random.sample(links_from_home, min(3, len(links_from_home)))
    print(f"found: {to_visit}")
    f = open(f"{title}/home.html", "w", encoding="utf-8")
    f.write(driver.page_source)
    f.close()

    i = 1
    for link in to_visit:
        print(f"Scraping: {link}")
        driver.get(link)
        time.sleep(3)
        driver.save_screenshot(f"{title}/page{i}.png")
        f = open(f"{title}/page{i}.html", "w", encoding="utf-8")
        f.write(driver.page_source)
        f.close()
        i+=1
    
    driver.quit()

sites = open("processed_sites.txt", "r")
i = 0
while i<25:
    line = sites.readline()
    line = line.strip("\n")
    scrape_page(f"https://{line}", f"site{i}")
    i += 1
sites.close()

sites = open("processed_built_with.txt", "r")
j = 0
while j<25:
    line = sites.readline()
    line = line.strip("\n")
    scrape_page(f"https://{line}", f"site{i}")
    i += 1
    j += 1

