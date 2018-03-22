#!/usr/bin/env python2
# Filename:cmd.py
import subprocess,os,build
from subprocess import Popen, PIPE, STDOUT
def exeCmdRealTime(command):
	print '*****start*****'
	build.printBlue(command)
	p = subprocess.Popen(command, stdout=subprocess.PIPE)
	while p.poll() is None:
		l = p.stdout.readline()
		l = l.strip('\r\n')
		print l
	#print p.stdout.read()
	print '*****end*****' + '\n'
def popen(command):
	print '*****start*****'
	build.printBlue(command)
	r = os.popen(command)
	info = r.readlines()
	for line in info:
		line = line.strip('\r\n')
		print line
	print '*****end*****' + '\n'
def system(command):
	print '*****start*****'
	build.printBlue(command)
	r = os.system(command)
	print '*****end*****' + '\n'
	return r
if __name__ == '__main__':
	exeCmd('adb root')
