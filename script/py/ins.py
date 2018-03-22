#!/usr/bin/env python
# Filename:ins.py
import sys,build
paramLen = len(sys.argv)
print paramLen
if(paramLen > 2) :
	arg1 = sys.argv[1]
	arg2 = sys.argv[2]
	build.install(arg1,arg2)
else :
	build.printRed('\nERROR:You need two param. Please input apkName and assembleName, and try again.\n')
