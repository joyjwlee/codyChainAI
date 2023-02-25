# run this python file to update the json's whenever you want :)

# imports
from bs4 import BeautifulSoup
import requests
import json

# variables
ao3_domain = "https://archiveofourown.org"
JSON_PATH = "web/json/fandoms.json"

# returns an array of each cateogory link (on which multiple fandoms are listed)
def generate_category_links():
    ao3 = requests.get(ao3_domain)
    soup = BeautifulSoup(ao3.text)
    all_categories = soup.select("div.browse a")
    for i in range(len(all_categories)):
        all_categories[i] = ao3_domain + str(all_categories[i].attrs["href"])
    return all_categories

#TODO:? a potential helper function, optional! 
# returns an array of {"name":"fandom_name", "link":"fandom_link"} for all fandoms
def get_all_fandoms():
    return None

#TODO:? a potential helper function, optional! 
# returns an array of {"name":"fandom_name", "link":"fandom_link"} for the top most written fandoms in each category

def get_top_fandoms(n):
    for i in range(n):
        print(i)
    return None

#TODO: Week One deliverable ! it's to write a function that will populate fandoms.json 
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
