import requests
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient
import datetime
import time as t


account_sid = "AC654930cd56308bb85c89e74f5f5a7a10" 
auth_token  = "079aae0b8785686e201b2098a8b5e60a"

airtime=[]
day = []
canary = 0

while canary == 0:
    
    
    r = requests.get('http://www.tvguide.com/tvshows/the-bachelor/191811/')

    soup = BeautifulSoup(r.content,'lxml')

    time = soup.findAll('span',{'class':'tvobject-right-rail-airing-date-time'})

    for i in time:
        airtime.append(i.text)
    
    
        

    date = soup.findAll('span',{'class':'tvobject-right-rail-airing-date-date'})

    for d in date:
        day.append(d.text)
        
        

    now = datetime.datetime.now()

    month = now.month
    real_hour = now.hour +3 #3 is added to adjust for east coast time
    real_min = now.minute
    real_day = now.day
   
    mth = str(day[0]) #needs to split month from date string then use month
    
    mth2 = mth[:3]

    dy = mth[4:]
    
    

    month_conversion = {1:'Jan', 2:'Feb', 3: 'Mar',4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug',9:'Sep',10:'Oct', 11: 'Nov', 12:'Dec'}
        
    month_abrev = month_conversion[month] #converts number of current month into 3 letter abbreviation. 

        
    if real_min < 10:
        real_min = '0'+str(real_min)
        
        
    if real_hour > 12:
        real_hour -=12
        real_time = str(real_hour) +':'+ str(real_min) +'pm'
    else:
        real_time = str(real_hour) +':'+ str(real_min) +'pm'
        
        
    if month_abrev == mth2: #mth needs to be a new variable that contains the 3 letter month abbreviation stripped for day
        print "Month"
        if ''.join(sorted(str(dy))).strip()==''.join(sorted(str(real_day))).strip():
            print "Day"                                          
                                
                      
            if ''.join(sorted(airtime[0])).strip() == ''.join(sorted(real_time)).strip():
                client = TwilioRestClient(account_sid, auth_token)
                call = client.calls.create(to="+", # Any phone number
                from_="+18184235158", # Must be a valid Twilio number
                url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
                print(call.sid)
                print "Calling"
                canary =+1
                t.sleep(60)
                exit()
                
    print airtime[0] 
    print real_hour
    t.sleep(60)            
    print "Another minute has passed."
    
    
    


    
    




