from selenium import webdriver
import time
import pandas as pd
cd='chromedriver.exe'
browser=webdriver.Chrome(cd)

browser.get('https://twitter.com/explore/tabs/trending')
time.sleep(15)
sp=browser.find_elements_by_tag_name('span')
fl=[]
for i in sp:
    a=i.get_attribute('textContent')
    if(a.startswith('#')):
        if a not in fl:
            fl.append(a)
urls=[]
for i in fl:
    i=i[1:]
    url='htttps://twitter.com/search?q=%23'+i+'&src=trend_click'
    urls.append(url)

dict={'Hashtag':fl,'URL':urls}

df=pd.DataFrame(dict)
df.to_csv("trends.csv",index=False)
print("done")