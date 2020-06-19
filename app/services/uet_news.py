import requests

from bs4 import BeautifulSoup


def get_newsfeed():
    r = requests.get('https://uet.vnu.edu.vn/')

    html = r.text

    soup = BeautifulSoup(html)
    divs = soup.findAll("div", {"class": "post-scroller-item"})

    newsfeed = []
    for div in divs:
        img = div.find("img")
        a = div.find("a")

        newsfeed.append([img['title'], img['src'], a['href']])

    return newsfeed


def get_url(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html)
    content = soup.findAll("div", {"id": "content"})
    return str(content[0])


def get_dashboard():
    r = requests.get('https://uet.vnu.edu.vn/')

    html = r.text
    print(html)
    soup = BeautifulSoup(html)
    divs = soup.findAll("div", {"class": "event-thumbnail"})

    newsfeed = []
    for div in divs:
        img = div.find("img")
        a = div.find("a")

        newsfeed.append([img['title'], img['src'], a['href']])

    return newsfeed


def get_studentnews():
    r = requests.get('https://uet.vnu.edu.vn/category/tin-tuc/tin-sinh-vien/')

    html = r.text

    soup = BeautifulSoup(html)
    divs = soup.findAll("div", {"class": "item-thumbnail"})

    newsfeed = []
    for div in divs:
        
        img = div.find("img")
        a = div.find("a")

        newsfeed.append([img['title'], img['src'], a['href']])

    return newsfeed
