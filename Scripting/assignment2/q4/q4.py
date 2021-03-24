#!/usr/bin/env python3

import requests 
from bs4 import BeautifulSoup 
import pandas as pd


#file=open("mobile_dataset.txt","a+")
phones=[]
launchs=[]
nets=[]
wets=[]
batterys=[]
dimensions=[]
sims=[]
os=[]
rams=[]
cameras=[]
count=0
print("Start")
for i in range(8000,9100):
    URL = ("https://www.gsmarena.com/huawei_mate_30_5g-%d.php" % i)
    r = requests.get(URL) 
  
    soup = BeautifulSoup(r.content, 'html5lib') 
    try:
        phone_name=soup.find('h1',attrs={'data-spec':'modelname'}).text
        if(phone_name.find("Watch")!=-1):
            continue
        elif(phone_name.find("Tab")!=-1):
            continue
        launch=soup.find('td',attrs={'data-spec':'year'}).text 
        nettech=soup.find('a',attrs={'data-spec':'nettech'}).text
        weight=soup.find('td',attrs={'data-spec':'weight'}).text
        battery=soup.find('td',attrs={'data-spec':'batdescription1'}).text
        dimension=soup.find('td',attrs={'data-spec':'dimensions'}).text
        sima=soup.find('td',attrs={'data-spec':'sim'}).text
        osa=soup.find('td',attrs={'data-spec':'os'}).text
        try:
            ram=soup.find('td',attrs={'data-spec':'internalmemory'}).text
        except AttributeError:
                ram="Not Present"
        try:
            camera=soup.find('td',attrs={'data-spec':'cpu'}).text
        except AttributeError:
                gpsa="Not Present"
    except AttributeError:
                continue
    except IndexError:
         continue
    except TypeError:
         continue
         
             
    count+=1
    phones.append(phone_name)
    launchs.append(launch)
    nets.append(nettech)
    wets.append(weight)
    sims.append(sima)
    o=osa.split(';')
    osa=o[0]
    os.append(osa)
    k=gpsa.split(';')
    gpsa=k[0]
    rams.append(gpsa)
    battery.append(battery)
    dimensions.append(dimension)
    cameras.append(camera)
    
    if(count==499):
        break
    
dt=pd.DataFrame({'Phone Name':phones,'Launch Date':launchs,'OS':os,'SIM':sims,'Internal':rams,'Network Technology':nets,'CPU':camera,'Weight':wets,'Dimensions':dimensions,'Battery Capacity':batterys })
dt.to_csv("data.csv",index=False,encoding='utf-8')
print("End")
