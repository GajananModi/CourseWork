#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random 
b_indian=[]
bow_indian=[]
all_indian=[]
wk_indian=[] 
b_for=[]
bow_for=[]
all_for=[]
wk_for=[]

    
file2=open("ipl.txt","r")
for line in file2:
    if(line.find("Batsman")!=-1 and line.find("India")!=-1):
        b_indian.append(line.strip())
    if(line.find("Batsman")!=-1 and line.find("India")==-1):
        b_for.append(line.strip())
    
    if(line.find("Wicket Keeper")!=-1 and line.find("India")!=-1):
        wk_indian.append(line.strip())
    if(line.find("Wicket Keeper")!=-1 and line.find("India")==-1):
        wk_for.append(line.strip())
    
   
    if(line.find("Bowler")!=-1 and line.find("India")==-1):
        bow_for.append(line.strip())
    if(line.find("Bowler")!=-1 and line.find("India")!=-1):
        bow_indian.append(line.strip())
        
    
        
    
    if(line.find("All-Rounder")!=-1 and line.find("India")!=-1):
        all_indian.append(line.strip())
    if(line.find("All-Rounder")!=-1 and line.find("India")==-1):
        all_for.append(line.strip())
   
file2.close()


config =[]

file1= open ("c.txt", "r")
for line in file1:
    config.append(line.strip()) 
file1.close()
#print(config)

st=config[0].split(':')
o1=int(st[1]) 
o2=int(st[2])

st=config[1].split(':')
b1=int(st[1])
b2=int(st[2])
st=config[2].split(':')
ba1=int(st[1])
bat2=int(st[2])

st=config[3].split(':')
w1=int(st[1])
w2=int(st[2])

st=config[4].split(':')
a1=int(st[1])
a2=int(st[2])
teamlist=[] 

teamlist=config[7:16]

for team in teamlist:               
    while(1):
        while(1):
            indianb=random.randrange(ba1,bat2)
            overseasb=random.randrange(0,bat2)
            io=indianb+overseasb        
            break
                    
        while(1):
            indianbow=random.randrange(b1,b2)
            overseasbow=random.randrange(0,b2)
            iob=indianbow+overseasbow
            break
            
        while(1):
            indianalr=random.randrange(a1,a2)
            overseasalr=random.randrange(0,a2)
            ioalr=indianalr+overseasalr
            break
            
        while(1):
            indianwk=random.randrange(w1,w2)
            overseaswk=random.randrange(0,w2)
            iowk=indianwk+overseaswk
            break
                
        overseas=overseasb+overseasbow+overseasalr+overseaswk
        total=io+ioalr+iowk+iob
        if(total==18 and overseas>=4 and overseas<=7):
            break
                    
    
    
    players=[]
    for i in range(0,indianb):
        j=random.randrange(0,len(b_indian))
        players.append(b_indian[j])
        b_indian.pop(j)
    for i in range(0,overseasb):
        j=random.randrange(0,len(b_for))
        players.append(b_for[j])
        b_for.pop(j)
    for i in range(0,indianalr):
        j=random.randrange(0,len(all_indian))
        players.append(all_indian[j])
        all_indian.pop(j)
    for i in range(0,overseasalr):
        j=random.randrange(0,len(all_for))
        players.append(all_for[j])
        all_for.pop(j)
    for i in range(0,indianwk):
        j=random.randrange(0,len(wk_indian))
        players.append(wk_indian[j])
        wk_indian.pop(j)
    for i in range(0,overseaswk):
        j=random.randrange(0,len(wk_for))
        players.append(wk_for[j])
        wk_for.pop(j)
    for i in range(0,indianbow):
        j=random.randrange(0,len(bow_indian))
        players.append(bow_indian[j])
        bow_indian.pop(j)
    for i in range(0,overseasbow):
        j=random.randrange(0,len(bow_for))
        players.append(bow_for[j])
        bow_for.pop(j)
        
    #print(players)
    filename=team + '.txt'
    file=open(filename,'w')
    file.write("Team:"+team+"\n\n")
    k=1
    for player in players:
        data=player.split(':')
        file.write("Player ")
        file.write(str(k))
        file.write("\n")
        file.write("Name: "+data[0])
        file.write("\n")
        file.write("Country: "+data[1])
        file.write("\n")
        file.write("Ability: "+data[2])
        file.write("\n")
        file.write("Fees: "+data[3])
        file.write("\n")
        file.write("\n")
        k+=1
    #file.write("\n")
    file.close()
        
    
        
    
        

    
    

        
        
  
