import httplib
import urllib
import time
key='UEGQF5U7QPFVZS2L'

while True:
    temp=25
    params=urllib.urlencode({'field1':temp,'key':key})
    headers={"content-typezze":"application/x-www-form-urlencoded","Accept":"text/plain"}
    
    try:
        conn=httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("post","/update",params,headers)
        response=conn.getresponse()
        print(response.status,response.reason)
        conn.close()
    except:
        print("no net connection")
