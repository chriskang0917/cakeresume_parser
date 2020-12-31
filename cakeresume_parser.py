from bs4 import BeautifulSoup
import requests
import pandas as pd


# Load input
input_url = input('輸入你想要爬的網址：')
input_page_count = input('輸入你想要爬的頁數：')


def web_parser(home_url, page_count):
    """
    :param home_url:
    :param page_count:
    :return:
    """

    def parse_process(_url):
        response = requests.get(_url).text
        soup = BeautifulSoup(response, 'html.parser')

        name_element = soup.find_all('a', class_='page-link ellipsis')
        desc_element = soup.find_all('p', class_='page-desc')
        link_element = soup.find_all('a', class_='page-link ellipsis')

        name_list = [company.get_text() for company in name_element]
        desc_list = [description.get_text() for description in desc_element]
        link_list = [link_url.get('href') for link_url in link_element]

        return name_list, desc_list, link_list

    def list_appender(origin_list, new_data):
        for data in new_data:
            origin_list.append(data)

    # Initialize the data_list
    name_total = []
    desc_total = []
    link_total = []

    for page in range(1, int(page_count) + 1):
        if page != 1:
            url = home_url + "?page={}".format(page)
            name, desc, link = parse_process(url)
            # append to the list to store
            list_appender(name_total, name)
            list_appender(desc_total, desc)
            list_appender(link_total, link)
            print('Page {} has complete!'.format(page))
        else:
            url = home_url
            name, desc, link = parse_process(url)
            # append to the list to store
            list_appender(name_total, name)
            list_appender(desc_total, desc)
            list_appender(link_total, link)
            print('Page {} has complete!'.format(page))

    # Output to csv file
    df = pd.DataFrame()
    df['Company'] = pd.Series(name_total)
    df['Description'] = pd.Series(desc_total)
    df['Link'] = pd.DataFrame(link_total)
    df.to_csv('Info.csv')


# link = 'https://www.cakeresume.com/companies'
# page_number = 100

web_parser(input_url, input_page_count)

print('All parse Done!')
