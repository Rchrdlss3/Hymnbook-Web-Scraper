from bs4 import BeautifulSoup
import requests
import os
###THIS IS JUST FOR THE CHANTE DESPERANCE KREYOL SONGS SO FAR. 
###TOTAL OF 62 PAGES


##USING BEAUTIFUL SOUP AND REQUESTS TO GET THE SOURCE CODE
page_number = 1
##USING A WHILE LOOP TO AGEE THE PAGE NUMBERS INTO THE LINKS,WILL LATER USE
links2=[]
while page_number <= 62:
    new_page = requests.get('http://haitianview.com/category/chants-desperance/page/' + str(page_number)).text
    soup2 = BeautifulSoup(new_page,'lxml')
    singles2 = soup2.find_all('a',class_ ='td-image-wrap')
    for x in singles2:
        x2 = x['href']
        links2.append(x2)
    page_number +=1
    
html_text = requests.get('http://haitianview.com/category/chants-desperance/').text
soup = BeautifulSoup(html_text,'lxml')

links = []
singles = soup.find_all('a',class_ ='td-image-wrap')

for single in singles:
    x = single['href']
    links.append(x)


def createFolder(directory):
    try: 
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('This is not working dummy')
ai = 0
 
for x in links2:
    #FOR LOOP
    z= links2[ai]
    ai +=1
    #CREATES THE FOLDER NAME FOR THE TEXT FILE OF THE SONGS
    folderName = (z.strip('http://haitianview.com/'))
    createFolder(folderName)
    filepath= folderName
    ###CREATE TEXT FILE, AND WRITING IN IT
    file = open(filepath+'/'+filepath+'.txt','w')
    songlink = requests.get(z).text
    soup2 = BeautifulSoup(songlink,'lxml')
    x = soup2.find_all('h3')
    for i in x:
        y = i.get_text().strip('h3 style="text-align: center;')
        file.write(y)      


