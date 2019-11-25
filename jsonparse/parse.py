"""This will parse the json into a list of routers that are up."""

import sh
import os
import json

filenames = os.popen('ls -t json | head -n2').read()
#str(os.system("ls -t json | head -n2"))
#sh.ls("-t", "json" )
print(filenames)
filenames=filenames.splitlines()

with open(r"json/"+filenames[0]) as recentfile:
    recent = json.loads(recentfile.read())
    #print(recent)
print("ROUTER UP")
for team in recent["teams"]: 
    if recent["teams"][team]['Router is UP']:
        print(str(recent["teams"][team]["TeamIP"])[:-4] + "2")
    #print(str(recent["teams"][team]) + " " + str(recent["teams"][team]['Router is UP']))
    # + {team['Router is UP']}
    
#print("SERVICES UP")
#for team in recent["teams"]: 
#    if recent["teams"][team]['Service is UP']:
#        print(str(recent["teams"][team]["TeamIP"]))

#with open(r"json/"+filenames[1]) as recentfile2:
#    recent2 = json.loads(recentfile2.read())
#for team in recent2["teams"]:
#    print(team["Router is UP"])