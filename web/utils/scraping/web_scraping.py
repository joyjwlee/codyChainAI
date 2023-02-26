# run this python file to update the json's whenever you want :)

# imports
from bs4 import BeautifulSoup
import requests
import json
import re

# variables
ao3_domain = "https://archiveofourown.org"
JSON_PATH = "web/json/fandoms.json"

# returns an array of each cateogory link (on which multiple fandoms are listed)
def generate_category_links():
    # get site text
    ao3 = requests.get(ao3_domain)
    soup = BeautifulSoup(ao3.text)

    # get all the category divs
    all_categories = soup.select("div.browse a")

    # loop through, concatenate, and return
    for i in range(len(all_categories)):
        all_categories[i] = ao3_domain + str(all_categories[i].attrs["href"])
    return all_categories

# returns an array of {"name":"fandom_name", "link":"fandom_link"} for all fandoms
def get_all_fandoms():
    # init
    dict = {}
    all_fandoms_domains = generate_category_links()

    # loop through all domains
    for domain in all_fandoms_domains:
        # get site text
        soup = BeautifulSoup(requests.get(domain).text)

        # get all of the fanfic divs
        all_top = soup.select("ol.group a")

        # loop through and return
        for i in all_top:
            div = str(i)
            name = re.search(">(.*)<", div).group(1)
            link = ao3_domain + re.search("href=\"(.*)\"", div).group(1)
            dict[name] = link

    return dict

# returns an array of {"name":"fandom_name", "link":"fandom_link"} for the top most written fandoms in each category
def get_top_fandoms():
    # get site text
    all_fandoms_domain = generate_category_links()[0]
    soup = BeautifulSoup(requests.get(all_fandoms_domain).text)

    # get all of the fanfic divs
    all_top = soup.select("ol.group a")

    # loop through and return
    dict = {}
    for i in all_top:
        div = str(i)
        name = re.search(">(.*)<", div).group(1)
        link = ao3_domain + re.search("href=\"(.*)\"", div).group(1)
        dict[name] = link
    return dict

# TODO: Week One deliverable ! it's to write a function that will populate fandoms.json
# creates fandoms.json file in the json folder with all fandoms and top fandoms in the listed format: '*shoudln't return anything'
# {
#    "top":[
#       {
#          "name":"topfandom",
#          "link":"link"
#       }
#    ],
#    "all":[
#       {
#          "name":"fandom",
#          "link":"link"
#       }
#    ]
# }
def gen_fandom_json():
    return


# gen_fandom_json() # <-- uncomment this and run the file to update or create fandoms.json

print(get_all_fandoms())
