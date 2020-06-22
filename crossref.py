# script to read event metadata from crossref
# use: python crossref.py

import json
import requests
import csv
from pprint import pprint

# functions

# call crossref api
def getData(cursor):
    return requests.get("https://api.crossref.org/types/proceedings/works?rows="+str(rows)+"&cursor="+cursor).json()

# handle and write data to file
def handleData(response):
    # prepare output file
    with open(filename, 'w') as csvfile:
        file = csv.DictWriter(csvfile, fieldnames = fieldnames)
        file.writeheader()

        print('handleData', response['message'].keys())
        # NOTE: slow as a lot of the reponse['message'] does not have keu 'item'
        # TODO: can getData() API ca;; only return response['message'] w/ item key??
        for item in response['message']:
            if 'item' in response['message'].keys():
                item = item['items']
                print('item')
                pprint(item)
                metadata = item['event']
                #  metadata = response['message']['items'][i]['event']

                # add the title and doi of the proceeding
                # TODO: .replace('\n', '')
                metadata['proceedings-title'] = item['title']
                # metadata['proceedings-title'] = response['message']['items'][i][
                # 'title']
                #''.join(response['message']['items'][i]['title']).encode('utf-8')

                metadata['doi'] = item['DOI']
                # metadata['doi'] = response['message']['items'][i]['DOI']

                # TODO: fix encoding
                # [''.join(x).encode('utf-8') for x in metadata ]
                print(metadata)

                # write metadata to file
                # file.writerow(metadata)

# variables
rows = 10
filename = 'crossref-events-from-proceedings.csv'
fieldnames = ['name', 'start', 'end', 'acronym', 'location', 'number', 'sponsor', 'theme', 'proceedings-title', 'doi']

# main: get and handle data, go to next page using the cursor
response = getData('*')
handleData(response)
cursor = response['message']['next-cursor']

while cursor:
    response = getData(cursor)
    handleData(response)
