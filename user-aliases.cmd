;= @echo off
;= rem Call DOSKEY and use this file as the macrofile
;= %SystemRoot%\system32\doskey /listsize=1000 /macrofile=%0%
;= rem In batch mode, jump to the end of the file
;= goto:eof
;= Add aliases below here
e.=explorer .
gl=git log --oneline --all --graph --decorate  $*
ls=ls --show-control-chars -F --color $*
la=ls -a --show-control-chars -F --color $*
ll=ls -a -l --show-control-chars -F --color $*
pwd=cd
clear=cls
history=cat %CMDER_ROOT%\config\.history
unalias=alias /d $1
vi=vim $*
cmderr=cd /d "%CMDER_ROOT%"
cfg = cd %CMDER_ROOT%\config
aliase = vim %CMDER_ROOT%\config\user-aliases.cmd 
profile = vim %CMDER_ROOT%\config\user-profile.cmd
recmd = %CMDER_ROOT%\config\user-aliases.cmd & %CMDER_ROOT%\config\user-profile.cmd
e=exit
apk=cd app\build\outputs\apk
py=cd /d %PY_HOME%
gv=%HOME%/.vim/gvim.exe -p $*
ai=adb install $*
aui=adb uninstall $*
pkg=e: & cd e:\apk

home=c: & cd %HOME%
roger=c: & cd %HOME%\.Config4Roger

gst = git status
gl =git pull --rebase
glg=git log --stat
gp=git push
gco=git checkout $*
gcob=git checkout -b $*
gb=git branch
gba=git branch -a
gbv=git branch -vv
gc=git commit -s -am $*
gca=git commit --amend -a
gpdev=git push origin HEAD:refs/for/coolyota_msm8953_dev

o=explorer .

ak=adb kill-server
as=adb start-server
ad=adb devices
ash=adb shell
ar=adb root & adb remount
art=adb reboot
astart=adb shell am start -n com.android.jv.ink.launcherink/com.android.jv.ink.launcherink.ui.home.JvMainActivity
astartd=adb shell am start -D -n com.android.jv.ink.launcherink/com.android.jv.ink.launcherink.ui.home.JvMainActivity
astop=adb shell am force-stop com.zhangyue.iReader.Eink.study
astk=adb shell am stack list
aps=adb shell ps
apsg=adb shell ps | grep $1
aclear=adb root & adb remount & adb shell rm -rf data/data/com.android.jv.ink.launcherink/databases & adb shell rm -rf data/data/com.android.jv.ink.launcherink/shared_prefs & adb shell am force-stop com.android.jv.ink.launcherink  
acdb=adb root & adb remount & adb shell rm -rf /data/data/com.zhangyue.iReader.Eink.study/databases/task.db
acsp=adb root & adb remount & adb shell rm -rf data/data/com.android.jv.ink.launcherink/shared_prefs
afind = adb shell pm path $*
are = adb reboot edl
apdb = adb remount & adb pull /data/data/com.zhangyue.iReader.Eink.study/databases/task.db
atop=adb shell dumpsys activity | grep top-activity
aom=adb shell getprop |grep omsub
aback=adb shell input keyevent 4
adf=adb shell df

ins = ins.py $1 $2
insdebugy3 = cd /d %WORK_SPACE%\APP_BLauncher\LauncherInk &   ins.py CY_BLauncher-debug y3Debug
insdebugt6 = cd /d %WORK_SPACE%\APP_BLauncher\LauncherInk &   ins.py CY_BLauncher-debug t6Debug
insreleasey3 = cd /d %WORK_SPACE%\APP_BLauncher\LauncherInk &   ins.py CY_BLauncher y3Release
insreleaset6 = cd /d %WORK_SPACE%\APP_BLauncher\LauncherInk &   ins.py CY_BLauncher t6Release

frt = fastboot reboot
fco = fastboot oem config-omsub $*
fgn = fastboot oem get-number
artb = adb reboot bootloader
foe = fastboot oem edl

ecfg=c: & cd %HOME%\.ehartcfg
ss=screenCap.py $*

ir=c: & cd C:\ireader
ird=c: & cd C:\ireader\dev
temp=d: & cd d:\files\temp