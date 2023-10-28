import os
import shutil
i = 0

for x in os.walk("obj_train_data"):
    direct = x[0]
    files = x[2]
    for y in files:
        f = open(direct+"/"+y, "r")
        if f.readlines() != [] and i < 1850:
            shutil.copyfile(direct+"/"+y, f"train2_text/{y}")
            shutil.copyfile("Cleaned/"+y.strip(".txt")+".png", f"train2_images/{y.strip('.txt')+'.png'}")
        i += 1
        