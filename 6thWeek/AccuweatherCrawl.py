import requests
from bs4 import  BeautifulSoup
page = requests.get("http://www.accuweather.com/en/us/cupertino-ca/95014/month/332094?monyr=4/01/2017")
soup = BeautifulSoup(page.content, "html.parser")
date=soup.find('td',attrs={'class':'om'}).find('h3',attrs={'class':'date'}).get_text()
print date
actual_max_temp=soup.find('td',attrs={'class':'om'}).find('div',attrs={'class':'actual'}).find('div',attrs={'class':'temp'}).findAll('span',attrs={'class':'large-temp'})[0].get_text()
print actual_max_temp
actual_min_temp=soup.find('td',attrs={'class':'om'}).find('div',attrs={'class':'actual'}).find('div',attrs={'class':'temp'}).findAll('span',attrs={'class':'small-temp'})[0].get_text()
print actual_min_temp
hist_high_temp=soup.find('td',attrs={'class':'om'}).find('div',attrs={'class':'avg'}).find('span',attrs={'class':'temp'}).get_text()
hist_low_temp=soup.find('td',attrs={'class':'om'}).find('div',attrs={'class':'avg'}).find('span',attrs={'class':'lo'}).get_text()
print hist_high_temp
print hist_low_temp
























"""
td=soup.findAll('td')
for i in range(len(td)):
    date="Date:" + td[i].find('h3',attrs={'class':'date'}).get_text() 
    actual_max_temp="Actual max temp:" + td[i].find('div',attrs={'class':'actual'}).find('div',attrs={'class':'temp'}).findAll('span',attrs={'class':'large-temp'})[0].get_text()
    actual_min_temp="Actual min temp:" + td[i].find('div',attrs={'class':'actual'}).find('div',attrs={'class':'temp'}).findAll('span',attrs={'class':'small-temp'})[0].get_text()
    hist_high_temp="Hist high temp:" + td[i].find('div',attrs={'class':'avg'}).find('span',attrs={'class':'temp'}).get_text()
    hist_low_temp="Hist low temp:" + td[i].find('div',attrs={'class':'avg'}).find('span',attrs={'class':'lo'}).get_text()
    
    
    print date+":"+actual_max_temp+":"+actual_min_temp+":"+hist_high_temp+":"+hist_low_temp
"""