import os
import shutil
i = 0
shutil.copyfile("Final Scrape/site0/home.png", "test.png")
for x in os.walk("Final Scrape"):
    direct = x[0]
    files = x[2]
    for y in files:
        if y.endswith(".png"):
            shutil.copyfile(direct+"/"+y, f"Cleaned/{i:05}.png")
            i+=1