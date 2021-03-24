#pip install lxml
#pip install beautifulsoup4
#pip install requests
import requests
from bs4 import BeautifulSoup
import time
from playsound import playsound
import random
import os


def get_details (url):
    try:
        #load page and create soup
        page = requests.get(url)

        src = page.content
        soup = BeautifulSoup(src, 'lxml')


        #extract wickets
        divs = soup.find_all("div", class_="cscore_score")
        for div in divs:
            if div.span == None:
                continue
            score = div.text.split(" ")[0]
            print("score = " , score)
            wickets = int(score.split("/")[1])
            break


        #extract 4s and 6s
        fours = 0
        sixes = 0
        table = soup.find("table", {"data-text-contract" : "Contract table",
                                    'data-text-expand' : 'Expand table'})
        for tr in table.tbody:
            td=tr.find_all("td", class_ = "u-tt-l")
            fours += int(td[0].string)
            sixes += int(td[1].string)
          

        #get latest commentary item
        comment_item_pre = soup.find("div", {"class"  : "commentary-item"})
        
        comment = "no commentary available"
        over=-1
        item_wrap = comment_item_pre.find("div", {"class"  : "item-wrapper"})
        comment = item_wrap.find("div",{ "class" : "description"}).text
        over = item_wrap.find("div", { "class" : "over"}).find("div", { "class" : "time-stamp"}).text

        


        '''
        TODO does not work ...why?
        for div in divs:
            try:
                if div['class'] == "cscore_score ":
                    print(div.string)
                #print(div)
            except:
                continue
        '''
    except requests.exceptions.ConnectionError:
        print ("Page could not be opened")
        exit()
    except:
        print("Some details not available for showing...")
        
    return wickets,fours,sixes,comment,over

#for i in range(1,4):
 #   playsound('''audio/wicket/'''+ str(i) + ".mp3")
  #  time.sleep(5)  

#play random sound from directory = path
def play_rand_sound(path):
    files = os.listdir(path)
    nfiles = len(files)
    aud = random.randrange(1,nfiles+1,1)
    pathtoaud = path+"/"+ str(aud) + ".mp3"
    print("playing ", pathtoaud)
    playsound(pathtoaud)


url = input("enter the espncricinfo.com url: ")


#initialize
wickets,fours,sixes,c,o = get_details(url)
owick = wickets
ofours = fours
osixes = sixes

#periodically check for updates and play_rand_sound appropriately
while True:
    try:
        wickets, fours, sixes,comment,over = get_details(url)
    
        if(wickets == owick+1):
            play_rand_sound("audio/wicket")
        if(fours == ofours+1):
            play_rand_sound("audio/fours")
        if(sixes == osixes+1):
            play_rand_sound("audio/sixes")

       
        owick = wickets
        osixes = sixes
        ofours = fours
        os.system('cls')
        print ("wickets = ", wickets, "\tsixes = ", sixes, "\tfours = ", fours)
        print("Latest update retrieved: ", over," ",  comment)
        
        time.sleep(10)
        print ("Updating...")
        time.sleep(1)
        
    except:
        print("Some details not available for showing...")

   
