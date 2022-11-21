
"""task 1"""
symbals_ = [',','.',':']
with open('text.txt') as file:
  lines = file.readlines()
  count_lines = len(lines)
  print('Количество строк: ', count_lines)
  count = 0
  for i in lines: 
    line = i.replace('\n','')
    symbals = len(line)
    for j in symbals_:
        line.replace(j,'')
    words = len(line.split())
    count += 1
    print('Строка:', count, '; символов:', symbals, '; слов:', words )



"""task2"""
import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open('task2.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data])

def get_html(url_):
    response = requests.get(url_)
    print(response.status_code)
    html = response.text
    return html

def get_total_pages(html):
    soup = BeautifulSoup(html,'lxml')
    pages = soup.find('nav', class_ = 'pagination').find_all('span')
    print(pages)

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('div', class_ = 'itemList').find_all('a')
    return data


def main():
    with open('task2.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['title'])
    url_ = 'https://vesti.kg'
    html = get_html(url_)
    data =get_data(html)
    # get_total_pages(html)
    for i in data:
        title = i.text.strip()
        if title != '':
            write_to_csv(title)

main()

