# trio clouds,jabalpur haze,jammu smoke,goa rain
import requests
import os
from pprint import pprint
from datetime import datetime
now=datetime.now()
current_time=now.strftime("%H:%M:%S")
time=int(current_time[0:2])
local_city=input()
try:
        query_input='q='+local_city
        result=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query_input+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
        re = result.json()
        var=str("Weather: {}".format(re['weather'][0]['main']))

        #print_weather_details(weather_dat,local_city)
        output=str(var[9:])
        print(output)
        
        th="tubeerh.jpg"
        
        default ="/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/gsmodi/Desktop/team37_assignment2/q2/"

        if output == 'Haze' and time >= 0 and time <=12:
            hm1="hm1.jpeg"
            os.system(default+hm1)
        elif output == 'Haze' and time >=12 and time <24:
            hn1="hn1.jpeg"
            os.system(default+hn1)    
        elif output == 'Rain' and time >= 12 and time <24:
            rm1="rn1.jpeg"
            os.system(default+hm1)
        elif output == 'Rain' and time>=0 and time <= 12:
            rn1="rm1.jpg"
            os.system(default+hn1)    
        elif output == 'Clouds' and time >=0 and time <=12:
            cm1="cm1.jpg"
            os.system(default+cm1)
        elif output == 'Clouds':
            cn1="cn1.jpeg"
            os.system(default+cn1)
        else:
            th="th1.jpg"
            os.system(default+th)
      
except:
    print('City name not found...')

