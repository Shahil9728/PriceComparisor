#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
from tabulate import tabulate
import operator
import pandas as pd
import sys
import json

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


# q = '+'.join(input().split())
q = '+'.join(str(sys.argv[1]).split())

furl = 'https://www.flipkart.com/search?q='+q
r0 = requests.get(furl, 'html.parser', headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'})
soup = BeautifulSoup(r0.content, 'html.parser')
fimg = list(soup.find_all('img', class_='_396cs4'))
fname = list(soup.find_all('div', class_='_4rR01T'))
fprice = list(soup.find_all('div', class_='_30jeq3 _1_WHN1'))
flink = list(soup.find_all('a', class_='_1fQZEK'))
# frating=list(soup.find('div',class_="_3LWZlK"))
f1name = list(soup.find_all('a',class_='s1Q9rs'))
f2link = list(soup.find_all('a',class_='_2rpwqI'))
# Query = slippers then write the data by name along with the data

fsimg = list(soup.find_all('img', class_='_2r_T1I'))
fsname = list(soup.find_all('div', class_='_2WkVRV'))
fsname1 = list(soup.find_all('a', class_='IRpwTa'))
fsprice = list(soup.find_all('div', class_='_30jeq3'))
fslink = list(soup.find_all('a', class_='IRpwTa'))
# # try:
# #     if fname:
        # print([fimg[0].get('src'),fname[0].text,fprice[0].text,'https://www.flipkart.com'+flink[0].get('href')])

        # class Fdata:
        #     dfimg = fimg[0].get('src')
        #     dfname = fname[0].text,fprice[0].text
        #     dfprice = fprice[0].text
        #     dflink = 'https://www.flipkart.com'+flink[0].get('href')

        # # Fdata = {
        # #     'dfimg' : fimg[0].get('src'),
        # #     'dfname' : fname[0].text,
        # #     'dfprice' : fprice[0].text,
        # #     'dflink' : 'https://www.flipkart.com'+flink[0].get('href')
        # # }

        # # Fdata = json.dumps(Fdata)
        # # print(Fdata)
        # print(type(Fdata))
        # print(fimg[0].get('src'))
        # print(fname[0].text)
        # print(fprice[0].text)
        # print('https://www.flipkart.com'+flink[0].get('href'))
        # print()
    # # elif fsname:
    # #     Fdata = {
    # #         'dfimg' : fsimg[0].get('src'),
    # #         'dfname' : fsname[0].text,
    # #         'dfprice' : fsprice[0].text,
    # #         'dflink' : 'https://www.flipkart.com'+fslink[0].get('href')
    # #     }

    # #     Fdata = json.dumps(Fdata)
    # #     print(Fdata)
    #     print(fsimg[0].get('src'))
    #     print(fsname[0].text+' '+fsname1[0].text)
    #     print(fsprice[0].text)
    #     print('https://www.flipkart.com'+fslink[0].get('href'))
    #     print()
# #     else:
# #         print("Sorry, no results found!\n")
# # except Exception as e:
# #     print(e)
# #     print()

aurl = 'https://www.amazon.in/s?k='+q
r1 = requests.get(aurl, 'html.parser', headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'})
soup1 = BeautifulSoup(r1.content, 'html.parser')
aimg = list(soup1.find_all('img', class_='s-image'))
aname = soup1.find_all(
    'span', class_='a-size-medium a-color-base a-text-normal')
apricediv = soup1.find(
    'div', class_='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1')
if apricediv:
    b = apricediv.find('span', class_='a-price-whole')
alink = soup1.find_all(
    'a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')

asname = soup1.find_all(
    'span', class_='a-size-base-plus a-color-base a-text-normal')
asnamediv = soup1.find(
    'div', class_='a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro')

# aratingdiv = soup1.find_all('div',class_='a-row a-size-small')
# arating = aratingdiv.find('span',class_='a-size-base')
if asname and asnamediv:
    asprice = asnamediv.find('span', class_='a-price-whole')
else:
    asprice = apricediv.find('span', class_='a-price-whole')

# # try:
# #     if aname:
# #         Fdata = {
# #             'daimg' : aimg[0].get('src'),
# #             'daname' : aname[0].text,
# #             'daprice' : b.text,
# #             'dalink' : 'https://www.amazon.in'+alink[0].get('href')
# #         }

# #         Fdata = json.dumps(Fdata)
# #         print(Fdata)
#         print(aimg[0].get('src'))
#         print(aname[0].text)
#         print(b.text)
#         print('https://www.amazon.in'+alink[0].get('href'))
#         print()
    # # elif asname:
    # #     Fdata = {
    # #         'daimg' : aimg[0].get('src'),
    # #         'daname' : asname[0].text,
    # #         'daprice' : asprice.text,
    # #         'dalink' : 'https://www.amazon.in'+alink[0].get('href')
    # #     }

    # #     Fdata = json.dumps(Fdata)
    # #     print(Fdata)
#         print(aimg[0].get('src'))
#         print(asname[0].text)
#         print(asprice.text)
#         print('https://www.amazon.in'+alink[0].get('href'))
#         print()
# #     else:
# #         print("Sorry, no results found!\n")
# # except:print('No more results')
try:
    if aname:
        adname = aname[0].text
    else: adname = asname[0].text

    if fname:
        fdname = fname[0].text
    elif fsname:
        fdname=fsname[0].text
    else:
        fdname=f1name[0].text

    if fprice:
        fprice=fprice
    else:
        fprice=fsprice
except Exception as e:print(e)

if flink:
    flink = flink
else:flink=f2link

try:
    if fname or aname:
        Data = {
            'dfimg': fimg[0].get('src'),
            'dfname': fdname,
            # 'dfrating':frating[0].text,
            'dfprice': (fprice[0].text)[slice(1,7)],
            'dflink': 'https://www.flipkart.com'+flink[0].get('href'),
            
            'daimg': aimg[0].get('src'),
            'daname': adname,
            # 'darating':arating.text,
            'daprice': b.text,
            'dalink': 'https://www.amazon.in'+alink[0].get('href')
        }
        Data = json.dumps(Data)
        print(Data)
    elif fsname or asname:
        Data = {
            'dfimg' : fsimg[0].get('src'),
            'dfname' : fsname[0].text,
            # 'dfrating':frating.text,
            'dfprice' : fsprice[0].text,
            'dflink' : 'https://www.flipkart.com'+fslink[0].get('href'),            'daimg' : aimg[0].get('src'),
            
            'daimg' : aimg[0].get('src'),
            'daname' : asname[0].text,
            # 'darating':arating.text,
            'daprice' : asprice.text,
            'dalink' : 'https://www.amazon.in'+alink[0].get('href')
        }
        Data = json.dumps(Data)     
        print(Data)
    else:
        str1 = {'msg':'Hello Eror here in python'}
        print(json.dumps(str1))
except Exception as e:
    print(e)
    print()