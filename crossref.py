# script to read event metadata from crossref
# use: python crossref.py

import json
import requests
import csv
import urllib.parse

# VARIABLES
rows = 10 # number of items on a result page
filename = 'crossref-events-from-proceedings.csv'
fieldnames = ['name', 'start', 'end', 'acronym', 'location', 'number', 'sponsor', 'theme', 'proceedings-title', 'doi']

# FUNCTIONS

# call crossref api
def getData(cursor):

    return requests.get("https://api.crossref.org/types/proceedings/works?select=event,title,DOI&rows="+str(rows)+"&cursor="+cursor).json()

# handle and write data to file
def handleData(response, file):

        # get all entries
        for i in range(1, int(rows), 1):

            # get this item from response
            item =  response['message']['items'][i]

            # read the metadata of one event from item
            metadata = item['event']

            # add the title and doi of the proceeding
            metadata['proceedings-title'] = item['title']
            metadata['doi'] = item['DOI']

            # write metadata to file
            file.writerow(metadata)

        # read and return next cursor
        return urllib.parse.quote(response['message']['next-cursor'])

# MAIN

# prepare output file
with open(filename, 'w') as csvfile:
    file = csv.DictWriter(csvfile, fieldnames = fieldnames)
    file.writeheader()

    # get and handle data
    response = getData('*')
    cursor = handleData(response, file)

    # get next page using cursor
    counter = 0
    while cursor:
        if counter >= 10: break # for testing
        counter += 1
        print(cursor)
        response = getData(cursor)
        cursor = handleData(response, file)
