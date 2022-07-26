import requests
from bs4 import BeautifulSoup

URL = "https://www.securitylab.ru/news/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('a', class_='article-card inline-card')
    news = []
    for item in items:
        news.append({
            'time': item.find("time").getText(),
            'title': item.find("h2", class_='article-card-title').getText(),
            'desc': item.find("p").getText(),
            'link': "https://www.securitylab.ru" + item.get('href'),
            # 'photo': "https://www.securitylab.ru" + item.find('img', class_='d-none').get('src')
        })
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 3):
            html = get_html(f"{URL}page1_{page}.php")
            answer.extend(get_data(html.text))
        return answer
    else:
        raise Exception("Error in parser!")
