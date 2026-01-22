[app]
title = SystemUpdate
package.name = sysupdate
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,requests,urllib3,charset-normalizer,idna,certifi
orientation = portrait
android.permissions = INTERNET, READ_SMS, RECEIVE_SMS
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = armeabi-v7a
p4a.branch = master
