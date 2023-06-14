from bs4 import BeautifulSoup
import lxml
import pandas as pd
import requests
import pickle

def get_pantip_tag_link(tag_list):
    pantip_tag = "https://pantip.com/tag/"
    pantip_tag_link = [pantip_tag + x for x in tag_list]

    return pantip_tag_link

def get_topic_list(tag_link):
    topic_link_list = []

    for link in tag_link:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml')
        ul = soup.find('ul', class_="pt-list pt-list-item__full-title pt-list__type-a")
        topic_list = ul.find_all('li')
        for topic in topic_list:
            link = topic.find('a', href=True)
            topic_link_list.append(link['href'])

    return topic_link_list

def scrape_text_from_link(topic_link_list):

    topic_content = {}

    for link in topic_link_list:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, 'lxml')
        title = soup.find('h2', class_="display-post-title").get_text()
        content = soup.find('div', class_="display-post-story")
        text = content.get_text()
        text = text.replace('\t', '').replace('\n', ' ')

        topic_content[title] = text
        print(f"Save {title} successfully.")
    
    return topic_content
    

tag_list = ['สุขภาพ', 'สุขภาพกาย']
tag_link = get_pantip_tag_link(tag_list)
topic_list = get_topic_list(tag_link)
text_dict = scrape_text_from_link(topic_list)

with open('text_dict.pkl', 'wb') as file:
    pickle.dump(text_dict, file)
    file.close()