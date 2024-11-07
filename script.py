
import requests
from bs4 import BeautifulSoup

url = "https://news.mail.ru/tag/39/?ysclid=lz5azahzgd211200526" # Сaйт с новостями
page = requests.get(url) # Отправка запроса на сайт
soup = BeautifulSoup (page.text, "html.parser") # Haчало парсинга сайтa

filteredNews = []
allNews = soup.findAll('div', class_= 'ae54c73111')

for data in allNews:
    if 'Байден' in data.text or 'Трамп' in data.text or 'Харисс' in data.text or 'демократ' in data.text or 'республикан' in data.text: 
        print ("Оглавление: " , data.find('a', class_ = 'dfe7838f95 def3c4dc17 a334cd468c').text.strip())
        print ("Аннотация: " , data.find('div', class_ ="cca994f104 f63c3a51cb c347f8a549").text.strip())
        print ("Источник: " , data.find('div', class_ ="cca994f104 faddfda2ca a9c76ad6b1").text.strip(), "\n")
        
        
         