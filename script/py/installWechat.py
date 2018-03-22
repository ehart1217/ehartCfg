#!/usr/bin/env python
# Filename:installWechat.py 
import os,cmd	

def install (rootDir) :
	for apkfile in os.listdir(rootDir):
		if ('apk' in apkfile):
			path = os.path.join(rootDir,apkfile)
			cmd.system('adb install -r -d ' + path)

if(__name__ == '__main__'):
	install('E:\decode\wechat-all')
