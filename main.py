import requests
import bs4


KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'и']
response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')
articles = soup.select_one('div.tm-articles-list')

articles_list = articles.select('div.tm-article-snippet')

for article in articles_list:
    link = 'https://habr.com' +  article.select_one('a.tm-title__link')['href']
    title = article.select_one('h2').text.strip()
    time = article.select_one('time')['datetime']
    previews = article.select('div.article-formatted-body article-formatted-body article-formatted-body_version-2')
    previews = [preview.find('p') for preview in previews]
    text = {i for i in str(previews).split()} | {i for i in title.split()}
    if text & set(KEYWORDS):
        print(f'{time} - {title} - {link}')