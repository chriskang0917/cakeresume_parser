import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


# Input param
# url = input('URL: ')
# fix = input('Surfix: ')
# page = input('Page Count: ')


def yourator_parser(url_link, page_count, fix='&page='):

    safari = webdriver.Safari()
    total_name = []
    total_desc = []

    for page in range(1, page_count + 1):
        if page != 1:
            url = url_link + fix + str(page)
        else:
            url = url_link

        safari.get(url)
        sleep(6)

        soup = BeautifulSoup(safari.page_source, 'html.parser')

        # Extract the info from table
        name_element = soup.find_all('div', class_='y-card-content-title')
        desc_element = soup.find_all('div', class_='y-card-content-description')

        name_list = [name.find('a').string for name in name_element]
        desc_list = [desc.get_text(strip=True) for desc in desc_element]

        for i in range(len(name_list)):
            total_name.append(name_list[i])
            total_desc.append(desc_list[i])

        print(name_list)
        print(desc_list)

    total = pd.DataFrame([total_name, total_desc]).T
    total.columns = ['Company', 'Description']
    total.to_csv('total.csv')
    # print(total.head())
    safari.close()


link = 'https://yourator.co/companies?area[]=TPE&area[]=NWT'
fix = '&page='
pages = 30

yourator_parser(link, fix, pages)
