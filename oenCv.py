from bs4 import BeautifulSoup
from requests_html import  HTML, HTMLSession
import requests
import cloudscraper
import time
import re



url = open("html.html")
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


scraper = cloudscraper.create_scraper()
#x= scraper.get(url).text
lst_name = []
lst_link = []

count = 0
soup = BeautifulSoup(url, 'html.parser')


search = soup.find('div',{ "id" : "sidebar_right3" })
search_1 = search.find_all('div', class_='cat-eps')


for a in search.find_all('a', href=True, title=True)[::-1]: 
    n = a["href"]
    l = a["title"]
    lst_name.append(l)
    lst_link.append(n)          
    print(count, l) 
    count += 1


y = int(input("Which Ep (1/279) =="))
i_name = lst_name[y]
i_link = lst_link[y]
print(i_name)
url1 = "https://ndiskc12.cizgifilmlerizle.com/getvid?evid=vyLxzB5kF78WGA-Us7bonlKZYcHoOBR451sMV9OewBvHm4TSLzGsxgLWj6GEPJv7g8Bt2iMWN8Rmd_-s0_u1cK2lfq7mbVVA4cVKhKkhPESrd2bRalWv3fMKsKNFG5-OANF-42UkOWRObLkjlVd21aLHVFarNwieMIy7W5Yr9WX3NeOinUKgXtWLlsdhsFD0ef7XygKNNdnHnSTf1J0VZ1WrlbE-06w56riyea5rN0g4IFvkP0Kxuu1gvg5WmbXcTZEY8TbPPX8biBlbzL5ATukJ7M-JBIz1g_PzBuupoT0H3eCCreuWUWdDcODuec0luja19ef0RHUrXrkYH7PqigkDNxNQxNQlQMDI6kBtqa0tVYG-GSBNjOziYuXGNe0XK5qJWzl_svvW64JTojaiA91OCZ2sLsqkCmLlv854rMHcKmtMh9yuZ-2sFnLVqQ-Q"
def PlayUrl(url):
    html = GetHTML(url);
    soup = bs(html, "html.parser")
    
    
    id = soup.find('div',{'class':'b-video_player'})['data-video_id']
    
    player = soup.find('div', {'class':'c-videos'})
    player = player.find('div', attrs={'data-video_id': id})
    player = player.find('span', {'class': 'video-hosting'})
    player = player.text
    
    if 'vk.com' in player:
        url = GetVKUrl(html)
    elif 'myvi.tv' in player or 'myvi.ru' in player:
        url = GetMyviUrl(html, url)
    elif 'rutube.ru' in player:
        url = GetRutubeUrl(html)
    elif 'sibnet.ru' in player:
        url = GetSibnetUrl(html)
    elif 'sovetromantica.com' in player:
        url = GetSRUrl(html)
    elif 'smotret-anime.ru' in player:
        url = GetSAUrl(html, url)
    else :
        Notificator('ERROR', 'Not supported player', 3600)
        return None
    if url :
        i = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(h, True, i) 



PlayUrl(url1)