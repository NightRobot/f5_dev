# importing the requests library 
import requests,time
clock = 5 # sec

if __name__ == "__main__" :
    now = time.time()
    timer = now + clock
    while(True) :
         if now > timer :
            timer += clock
            r = requests.get('http://10.128.10.241/') 
            print(r.status_code)
            print(r.headers['content-type'])
            print(r.encoding)
            print(r.text)