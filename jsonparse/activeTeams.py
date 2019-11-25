"""Grabs information from the site(vpn.ructfe.org) and parses to json."""

import json
from sh import wget
from sh import rm
import os
import datetime

from time import gmtime, strftime

i=strftime("%H.%M.%S", gmtime())
#print("current time: ", i)


htmlfilename=f"html/index.{i}.html"
jsonfilename=f"json/activeTeams.{i}.json"
mostrecientFilename=f"json/mostrecient"

activeips=""
with open('team_ip_addrs.txt') as iplist:
    activeips=iplist.read()

#print(activeips)

#rm("-f", "index.html")
wget("https://vpn.ructfe.org/", "-O",htmlfilename )
arr = []
summ=[]
tojson = {}
teams={}
count = -1

with open(htmlfilename,mode = 'r', encoding = 'utf-8') as f:
    for line in f:
        #print(count, line)
        if "<h3>" in line:
            #print("found!")
            timestamp = line[13:]
            timestamp = timestamp.split("+")[0]
            timestamp = timestamp.strip()
            #print(timestamp)
            tojson.update({"timestamp":timestamp})
            
        if "<th " in line and count == 1:
            #print("found sum")
            line = line.strip()
            line = line.split("= ")[1]
            line = line.split("<")[0]
            #print(line)
            summ.append(int(line))

        if "<tr>" in line:
            count = count+1
            #print("found tr")
            arr = []
            #while not "</tr>" in line:
        if "<td" in line:
            # print("found td")
            if len(arr) <= 1:
                line = line.split(">")[1]
                line = line.split("<")[0]
                line = line.strip()
                arr.append(line)
            else:
                line = line.split("yesnocell ")[1]
                line = line.split("\">")[0]
                val = (line == "yescell")
                arr.append(val)

            # print(line)
        if "</tr>" in line and count > 1:
            teamid = int(arr[0])
            IPA = 60 + int(teamid/256)
            IPB = teamid%256
            ip = f"10.{IPA}.{IPB}.0/24"
            #print(ip)
            team =  {
                "TeamId": teamid,
                "TeamIP": ip, 
                "Router is UP": arr[2],
                "Image is UP":arr[3],
                "Service is UP":arr[4],
                "Router was UP":arr[5],
                "Image was UP":arr[6],
                "Service was UP":arr[7]
            }
            #print( ip[:-4])
            if ip[:-4] in activeips:
                teams.update({arr[0]:team})
            

sums =  {
    
        "Routers currently up": summ[0],
        "Images currently up": summ[1],
        "Services currently up":summ[2],
        "Routers that have been up":summ[3],
        "Images that have been up":summ[4],
        "Services that have been up":summ[5]
    
}

tojson.update({"stats":sums})

tojson.update({"teams":teams})
thejson= json.dumps(tojson, indent=2)
#print(thejson)
f2 = open(jsonfilename, "w")
f2.write(thejson)
f2.close()
print(jsonfilename)