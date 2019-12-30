import pandas as pd
# import requests
# from bs4 import BeautifulSoup
import webbrowser as wb
from datetime import datetime as DATE
import os

# os.system('wget http://hjakgjkdf.fggf --no-check-certificate')
# print('############################################')
wCtlr= wb.get('firefox')



def search_in_site (site,keyword):
    with open(site+'.txt', 'r') as file:
        data = file.read()
    s= data.find(keyword)
    if data == '':
        out= 'service unavailable'
    else:
        if s != -1:
            out= 'دارای نماد ساپرا'

        else:
            out= 'فاقد نماد ساپرا'

    return out


df = pd.read_excel('sitesList.xlsx', index_col=0)
sitesList = list(df.index)
check=[]
for site in sitesList:
    site= site.lower()
    os.system('wget -O ./'+site+ '.txt https://'+site+' --tries=1 --no-check-certificate')
    out= search_in_site(site,"offers.sapra.ir")
    if out != 'service unavailable':
        check.append([out])
        continue
    os.system('wget -O ./'+site+ '.txt http://'+site+' --tries=1 --no-check-certificate')
    out = search_in_site(site,"offers.sapra.ir")
    check.append([out])
    if out == 'service unavailable':
         wCtlr.open('https://'+site)


    # try:
    #     os.system('wget -O ./'+site+ '.txt https://'+site+' --no-check-certificate')
    #     s= search_in_site(site,"offers.sapra.ir")
    #     if s != -1:
    #         check.append(["دارای نماد ساپرا"])
    #     else:
    #         check.append(["فاقد نماد ساپرا"])
    # except Exception:
    #     try:
    #         os.system('wget -O ./'+site+ '.txt http://'+site+' --no-check-certificate')
    #         s= search_in_site(site,"offers.sapra.ir")
    #         if s != -1:
    #             check.append(["دارای نماد ساپرا"])
    #         else:
    #             check.append(["فاقد نماد ساپرا"])
    #     except Exception:
    #             check.append(["service unavailable"])
    #             wCtlr.open('https://'+site)  #just for checking weather it is unavailable or not by open the site in firefox browser

x= DATE.now()
xname=  x.strftime('%d')+x.strftime('%b')+x.strftime('%Y')
xname= str(xname)+'.xlsx'
df1 = pd.DataFrame(check,index= df.index,columns=df.columns)
df1.to_excel(xname)
