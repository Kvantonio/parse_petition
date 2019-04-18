import requests
from bs4 import BeautifulSoup as bs
import csv

headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/70.0'
}

url = "https://petition.president.gov.ua/"

url_data = []
pet = []



for i in range(1, 41):
    url_page = "https://petition.president.gov.ua/?status=active&page=" + str(i)
    url_data.append({'url_page': url_page})


def pet_parse(url_data, headers):
    for g in url_data:
        url_text = (g['url_page'])
        session = requests.Session()
        request = session.get(url_text, headers=headers)
        soup =  bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'pet_content'})
        for div in divs:
            id = div.find('span', attrs={'class': 'pet_number'}).text[4:10]
            count = div.find('strong').text
            pet.append({
                'id': id, 'count': count
           })



def file_len(pet_parse):
    for l in pet:
        try:
            file_name = (l['id'])
            with open(file_name + '.csv', 'r+') as file:
                reader = csv.reader(file)
                value = len(list(reader))
        except BaseException:
            value = 0
        l['value'] = value


def save_csv(pet):
    for a in pet:
        file_name = (a['id'])
        with open(file_name + '.csv', 'a+') as file:
            wrtr = csv.writer(file)
            wrtr.writerow((a['value'], a['count']))


def main():
    pet_parse(url_data, headers)
    file_len(pet)
    save_csv(pet)

if __name__ == '__main__':
    main()