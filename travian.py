import cookielib
import urllib
import urllib2
import time
import pyfcm
from pyfcm import FCMNotification
time.sleep(1)
def pushmessage(num):
    push_service = FCMNotification(api_key="")
    registration_id = ""
    data_message = {
    "command" : "travian",
    "village" : num
    }
    result = push_service.notify_single_device(registration_id=registration_id, data_message=data_message)
    print result
######################    
villages=['49008&','61055&','71714&','44591&','81062&','87958&','89674&']
ts = int(time.time())
url = 'http://ts9.travian.com.tr/dorf1.php'
values = {'name' : 'Travianusername',
          'password' : 'Travianuserpassword',
          'w':'1300:1102',
          'login' : ts
           }
data = urllib.urlencode(values)
cookies = cookielib.CookieJar()

opener = urllib2.build_opener(
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPHandler(debuglevel=0),
    urllib2.HTTPSHandler(debuglevel=0),
    urllib2.HTTPCookieProcessor(cookies))

response = opener.open(url, data)
the_page = response.read()
http_headers = response.info()
warned=[0] * 10
while True:    
    for idx, val in enumerate(villages):
        time.sleep(1)    
        print(idx, val)
        response = opener.open(''.join([url,'?newdid=',val]))
        the_page = response.read()
        #print the_page
        warning='class="a1"' in the_page
        print warning
        if warning==True and warned[idx]!=1:
            warned[idx]=1
            pushmessage(idx+1)
        elif warning==False:
            warned[idx]=0
    time.sleep(300)
#print the_page
