import re
import csv
import io

entryList = {}
count = 0
with open ("log.ini", "r") as logFile:
    for line in logFile:
        pattern = re.compile(r"mac (\S+) among ports (\S+) and (\S+)")
        match = pattern.findall(line)
        if match!=[]:
            mac = match[0][0]
            port1 = match[0][1]
            port2 = match[0][2]
            entryList[count] = [mac, port1, port2]
        count += 1
with open ('log.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    for key, val in entryList.items():
        csvWriter.writerow(val)
