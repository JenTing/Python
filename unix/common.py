#!/usr/bin/env python
import subprocess
import time

IP_LIST = ['google.com', 'yahoo.com', 'amazon.com']

cmd_stub = 'ping -c 5 %s'

def do_ping(addr):
	print time.asctime(), "DOING PING FOR", addr
	cmd = cmd_stub % (addr, )
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
