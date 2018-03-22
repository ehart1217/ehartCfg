#!/usr/bin/env python2
# Filename:build.py
import cmd,os

def printGreen(str) :
	print ('\033[1;32;40m ' + str)
	printNormal('')

def printRed(str) :
	print ('\033[1;31;40m ' + str)
	printNormal('')

def printBlue(str):
	print ('\033[1;34;40m ' + str)
	printNormal('')

def printNormal(str) :
	print ('\033[1;37;40m ' + str)

def searchDevice():
	command = 'adb devices'
	r = cmd.system(command)
	output = os.popen(command).read()
	if 'List of devices attached' in output:
		deviceslist = [device.split('\t')[0] for device in output.split('\n')[1:] if device != '']
		count = len(deviceslist)
		return count
	else :
	        return 0

def install(apkName, assembleName) :
	r = cmd.system(r'rm -r app/build/outputs/apk/*')

	r = searchDevice()
	if r == 0 :
		printRed('\nInstall failed : no devices\n')
		exit(1)
	if r > 1 :
		printRed('\nInstall failed : more than one device\n')
		exit(1)

	cmd.exeCmdRealTime('gradlew.bat assemble' + assembleName)

	r = cmd.system('adb root')
	if (r != 0) :
		printRed('\ninstall failed.\n')
		exit(1);
	r = cmd.system('adb remount')
	if (r != 0) :
		printRed('\ninstall failed.\n')
		exit(1);

	if('-debug' in apkName):
		apkNameNoDebug = apkName.replace('-debug', '')
	else :
		apkNameNoDebug = apkName
	
	installPath = 'app\\build\outputs\\apk\\'
	
	if('Release' in assembleName):
		flavorName = assembleName.replace('Release', '')
		installPath = installPath + flavorName + '\\' + 'release'
	else :
		flavorName = assembleName.replace('Debug', '')
		installPath = installPath + flavorName + '\\' + 'debug'
	
	flavorName = flavorName.replace('Y','y') 
 	r = cmd.system('adb shell rm system/app/' + apkNameNoDebug + '/*.apk')
	
	command = 'adb push ' + installPath + '\\' + apkName + '.apk system/app/' + apkNameNoDebug + '/' + apkNameNoDebug + '.apk'
	r = cmd.system(command)
	if (r == 0):
		cmd.system('adb shell am force-stop com.android.jv.ink.launcherink')
		printGreen('\nInstall successful!\n')
	else :
		printRed('\nInstall failed.\n')

if __name__ == '__main__' :
	install('CY_BLauncher', 'YotaDevice')

