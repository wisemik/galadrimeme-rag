from bs4 import BeautifulSoup
import requests


def get_about_data(coin_name='dogecoin'):
    url = f"https://coinmarketcap.com/currencies/{coin_name}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    about_headers = [x.text for x in soup.select_one("#section-coin-about").find_all("h3")]

    about = [res.text for res in soup.select_one("#section-coin-about").find_all("div")]
    about = [x for x in about if x not in ['', ' ']]

    about_ = []
    current = about[1]

    for i, head in enumerate(about_headers):
        split = current.split(head)

        if split[0] != '':
            about_.append(split[0]+' \n')

        about_.append(head)
        current = current.split(head)[1]

    about_.append(split[1]+' \n')

    return about_
