import pandas as pd
import requests
from bs4 import BeautifulSoup
import webbrowser as wb
import datetime.datetime as DATE

wCtlr= wb.get('firefox')


# try:
#
#     result= requests.get('https://www.uptvs.com/' , verify=False)
#     page= result.text
#     print('###########################################')
#
# except Exception:
#     print(11111111111111111111111111)
#     wCtlr.open('https://www.uptvs.com/')

def search_in_site (site,keyword):
    result = requests.get(site , verify=False)
    page = result.text
    print(site)
    soup = BeautifulSoup(page, 'html.parser')
    s= page.find(keyword)
    return s


df = pd.read_excel('sitesList.xlsx', index_col=0)
sitesList = list(df.index)
check=[]
for site in sitesList:
    try:
        s= search_in_site('https://'+site,"offers.sapra.ir")
        print(s)
        if s != -1:
            check.append([1])
        else:
            check.append([0])
    except Exception:
        try:
            s= search_in_site('http://'+site,"offers.sapra.ir")
            if s != -1:
                check.append([1])
            else:
                check.append([0])
        except Exception:
                check.append(["service unavailable"])
                wCtlr.open('https://'+site)  #just for checking weather it is unavailable or not by open the site in firefox browser
x= DATE()
xname=  x.strftime('%d')+x.strftime('%b')+x.strftime('%Y')
xname= str(xname)+'.xlsx'
df1 = pd.DataFrame(check,index= df.index,columns=df.columns)
df1.to_excel(xname)
