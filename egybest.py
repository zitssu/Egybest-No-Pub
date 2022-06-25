from bs4 import BeautifulSoup
from requests_html import  HTML, HTMLSession
import requests
import time


y = input("the Film =")


url = "https://mila.egybest.kim/explore/?q={}".format(y)
x =  requests.get(url).text
soup = BeautifulSoup(x, 'html.parser')


search = soup.find_all('a', class_='movie')
lst = []
count = 0

for search in search:
    search_name = search.find('span', class_='title').text 
    search_url = search["href"]
    if search_name is None:
        print("Nothing Found") 
    lst.append(search_url)         
    print(count, search_name) 
    count += 1




y = int(input("the Number = "))
url_1 = lst[y]
time.sleep(2)

b =  requests.get(url_1).text
noup = BeautifulSoup(b, 'html.parser')
search = noup.find_all("a", class_="nop btn b dl _open_window")
lst=[]
for search in search:
    search_url = search["data-url"]
    lst.append(search_url)


server = input("SERVER (0) or (1) or (2) or (3) ==")
server = int(server)
g = lst[server]
url_2 = "https://mila.egybest.kim{}".format(g)
print(url_2)
n =  requests.get(url_2).text
doup = BeautifulSoup(n, 'html.parser')
source = doup.find('source')
print(source)







