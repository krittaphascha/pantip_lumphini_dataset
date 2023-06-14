from pantip_scraper import get_pantip_tag_link, get_topic_list, scrape_text_from_link
import pickle

tag_list = ['สุขภาพ', 'สุขภาพกาย']
tag_link = get_pantip_tag_link(tag_list)
topic_list = get_topic_list(tag_link)
text_dict = scrape_text_from_link(topic_list)

with open('text_dict.pkl', 'wb') as file:
    pickle.dump(text_dict, file)
    file.close()
