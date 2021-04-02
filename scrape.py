from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape(let):
    url1="https://www.1mg.com/drugs-all-medicines?label="
    url2=url1+let
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
    br=requests.get(url2,headers=hdr)
    soup=BeautifulSoup(br.text,"html.parser")
    s1=soup.find_all('a',{"class":"button-text link-page"})
    lastpage=0
    for j in s1:
        lastpage=int(j.text)

    
    for k in range(1,lastpage+1):
        print(k)
        pstr="&page="
        url=url2+pstr+str(k)
        br=requests.get(url,headers=hdr)
        soup=BeautifulSoup(br.text,"html.parser")
        s4 = soup.find_all('div',{"class":"style__font-bold___1k9Dl style__font-14px___YZZrf style__flex-row___2AKyf style__space-between___2mbvn style__padding-bottom-5px___2NrDR"})
        for i in s4:
            a=i.text.split("MRP")
            l3.append(a[0])
            l4.append(a[1])
    
    
l=[]
l3=[]
l4=[]
for i in range(97,123):
    let=chr(i)
    print(let)
    scrape(let)
md={"name":l3,"price":l4}
df=pd.DataFrame(md)
df.to_csv("medicine.csv")
