from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from nltk.tokenize import sent_tokenize

import json
# url_domain = "financialservices"
# url = "https://financialservices.gov.in/new-initiatives/schemes"    

# url_domain = "incometaxindia"
# url = r"https://incometaxindia.gov.in/charts%20%20tables/tax%20rates.htm"

def extract_save_txt(url,url_domain):
    html = urlopen(url).read()    
    raw = BeautifulSoup(html,'html.parser').get_text()

    raw = re.sub('\s{2,}', ' ', raw)

    raw_data_list = sent_tokenize(raw)

    N= 15

    subList = [raw_data_list[n:n+N] for n in range(0, len(raw_data_list), 15)]

    final_dictionary = {}
    for i in range(len(subList)):
        txt = ''.join(subList[i])
        final_dictionary[str(i)] = txt

    with open(f"./webData/{url_domain}.json", 'w', encoding='utf-8') as f:
        json.dump(final_dictionary, f, ensure_ascii=False, indent=4)

    # print("raw_data_list----",final_dictionary)
    # file1 = open(f"./webData/{url_domain}.txt","w+", encoding="utf-8")

    # file1.write(raw)
    # file1.close()