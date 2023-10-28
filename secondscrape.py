from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import os

def get_next_layer(elems, url, limit):
    links_from_home = []
    page = url[8:]
    for elem in elems:
        href = elem.get_attribute('href')
        if href is not None and page in href:
            links_from_home.append(href)
            #print(href)
    return random.sample(links_from_home, min(limit, len(links_from_home)))
    

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
    to_visit = get_next_layer(elems, url, 2)
    print(f"found: {to_visit}")
    f = open(f"{title}/home.html", "w", encoding="utf-8")
    f.write(driver.page_source)
    f.close()

    second_layer = []
    i = 1
    for link in to_visit:
        print(f"Scraping: {link}")
        driver.get(link)
        time.sleep(3)
        driver.save_screenshot(f"{title}/page{i}.png")
        elems = driver.find_elements(By.TAG_NAME, "a")
        second_layer += get_next_layer(elems, url, 1)
        print(f"found: {second_layer}")
        f = open(f"{title}/page{i}.html", "w", encoding="utf-8")
        f.write(driver.page_source)
        f.close()
        i+=1
    
    for link in second_layer:
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
    if i < 25:
        i+=1
        continue
    scrape_page(f"https://{line}", f"site{i}")
    i += 1
sites.close()

sites = open("processed_built_with.txt", "r")
i = 25
j = 0
while j<25:
    line = sites.readline()
    line = line.strip("\n")
    if i < 29:
        i+=1
        j+=1
        continue
    scrape_page(f"https://{line}", f"site{i}")
    i += 1
    j += 1

