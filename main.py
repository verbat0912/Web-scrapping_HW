import requests
import bs4
from fake_headers import Headers
from pprint import pprint as pp
from tqdm import tqdm


BASE_URL = 'https://habr.com/ru/articles/'
keywords = ['дизайн', 'фото', 'web', 'python']


def all_articles():
    response = requests.get(url=BASE_URL, headers=Headers(browser='chrome', os='win').generate())
    soup = bs4.BeautifulSoup(response.text, features='lxml')
    news_list = soup.select_one('div.tm-articles-list')
    articles = news_list.select('div.tm-article-snippet')
    return articles


def result_articles():
    analyzed_articles = []
    for article in tqdm(all_articles(), desc ="Идет обработка статей..."):
        link = article.select_one('a.tm-title__link')
        response = requests.get('https://habr.com' + link['href'])
        article_soup = bs4.BeautifulSoup(response.text, features='lxml')
        title = link.select_one('span').text
        body = article.find('div', class_='article-formatted-body')
        time = article_soup.select_one('time')['datetime']
        for i in keywords:
            if i.lower() in title.lower() or i.lower() in body.text.lower():

                analyzed_articles.append({
                    'title': title,
                    'time': time,
                    'URL': 'https://habr.com' + link['href'],
                })
    return pp(analyzed_articles)

if __name__ == "__main__":
    result_articles()
