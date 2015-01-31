#!/usr/bin/env python
from threading import Thread
import subprocess
from Queue import Queue

num_threads = 3
queue = Queue()
ips = ["www.google.com", "tw.yahoo.com", "192.168.1.100", "192.168.1.1"]
def pinger(i, queue):
	"""Pings subnet"""
	while True:
		ip = queue.get()
		print "Thread %s: Pinging %s" % (i, ip)
		ret = subprocess.call("ping -c 1 %s" % ip,
							shell=True,
							stdout=open('/dev/null', 'w'),
							stderr=subprocess.STDOUT)
		if ret == 0:
			print "%s: is alive" % ip
		else:
			print "%s: did not respond" % ip
		queue.task_done()

for i in range(num_threads):
	worker = Thread(target=pinger, args=(i, queue))
	worker.setDaemon(True)
	worker.start()

for ip in ips:
	queue.put(ip)

print "Main Thread Waiting"
queue.join()
print "Done"
