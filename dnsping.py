import dns.resolver
import time
from datetime import datetime
my_resolver = dns.resolver.Resolver()

def output (time,total):
    file = open('dns.csv', 'a+')
    file.write(("{},{},{}{}".format(date_time, total,"ms","\n")))




# 8.8.8.8 is Google's public DNS server
while True:
    now = datetime.now()
    my_resolver.nameservers = ['212.143.0.1']
    time.sleep(0.10)
    time1 = time.time()
    answer = my_resolver.query('google.com', raise_on_no_answer=True)
    time2 = time.time()
    total = (time2 - time1) * 1000.0
    date_time = now.strftime("%d/%m/%Y,%H:%M:%S")
    total = "%.2f"%total
    #output(date_time, total)
    print(("{},{},{}".format(date_time, total, "ms")))
