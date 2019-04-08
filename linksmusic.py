#!/bin/python3

# music get links 
# then you will receive mp3 link
import sys

import time
assert ('linux' in sys.platform), "This code runs on Linux only."
from colored import fore, back, style
time.sleep(1)
print(fore.LIGHT_BLUE + back.RED + style.BOLD +'----------------> wellcome to musiclik <---------------'+ style.RESET)
time.sleep(1)
import requests
from bs4 import BeautifulSoup
import re
import wget
import urllib.request
import os 
import wget
import moc
import mpv
try:
    lnk = input("\nPlease Enter the music site link: ")
except ValueError:
    print('The link entered is incorrect')
try:
    num = int(input('\nPlease enter a number a download music: '))
    urlnumber = 0
    url = requests.get(lnk)
    URL = url.text
    soup = BeautifulSoup(URL, 'lxml')
    links = soup.find_all('a',  href=True)

    for  a in links:
        if re.findall('http.*\.mp3', a['href']):
            if a.string is None:
                continue
            urlnumber = urlnumber + 1 
            s = a['href']
            n = a['href']
            result = re.sub('http\+', '', n)
            print(fore.LIGHT_BLUE + back.BLACK +'URL :' +style.RESET, urlnumber, '\n', "---------->",result, '\n\n')
            time.sleep(2)
            d = input('Do you want to download the song? (y/n)  play(p) stop(s) exit(e): ')

            if d == 'y':
                dl = os.system('torsocks wget ' + s)
                os.system('mkdir mymusic')
                os.system('mv  *.mp3  mymusic')
                time.sleep(5)
            elif d == 'e':
                break
            else:
                pass
                
            if d == 'p':
                os.system('if [ $(ls mymusic) == '' ]; then echo "there is no music to play"; else  mocp mymusic *.mp3 ;  fi')
                

            elif  d == 's':
                os.system('sudo killall mocp')
                break
            if urlnumber > num:
                break


except ImportError:
   print('NO module found')
finally:
    print(fore.LIGHT_BLUE + back.BLACK +'---------------------> done <-----------------------'+style.RESET)


