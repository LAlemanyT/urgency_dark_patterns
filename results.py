f = open("processed.txt", "r")
totals = {'urgency': 0, 'borderline':0, 'unique':0}
#image 1/1 /mnt/c/Users/Luis/Desktop/Final Scrape/YOLO/images/Test/00091.png: 352x640 1 urgency, 1 borderline, 7.6ms
#l = "image 1/1 /mnt/c/Users/Luis/Desktop/Final Scrape/YOLO/images/Test/00091.png: 352x640 1 urgency, 1 borderline, 7.6ms"

while True:
    l = f.readline()
    if l == "":
        break
    if "Speed:" in l or l =="\n":
        continue
    if  "(no detections)" in l:
        continue
    else:
        print(l)
        totals["unique"] += 1
        l = l.split()
        totals[l[6].strip(",").strip("s")] += int(l[5])
        if len(l) >= 9 and l[8].strip(",").strip("s") in totals:
            totals[l[8].strip(",").strip("s")] += int(l[7])
        print(l)
    print(totals)

f.close()