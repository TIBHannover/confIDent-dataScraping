

## Installation

* Install python version 3 or later: https://www.python.org/downloads
* Install pip3: `sudo apt install pip3`
* Install imported libraries: `pip3 install -r requirements.txt`
* Get code from GitHub: `git clone https://github.com/TIBHannover/confIDent-dataScraping.git`

# Event Metadata from WikiCFP
Python script to get event metadata from [wikicfp](http://wikicfp.com/): `wikicfp.py`

## Usage

Run the script ath the command line:
* `python3 wikicfp.py [startId] [stopId] [threads]`
* example: `python3 wikicfp.py 2000 2999 10`

### Parameters
* startId - the script will read data starting from this item id 
* stopId - this is the last item id, the script will read
* threads - maximum number of threads is 10

    
# Event Metadata from Crossref
Python script to get event metadata from [CrossRefs API](https://www.crossref.org/education/retrieve-metadata/rest-api/): `crossref.py`

## Usage

Run the script at the command line:
*`python3 crossref.py`

### Configuration

You can adapt the following variables at the first lines of the script: 
* rows: number of items on a result page - example: 100
* breakpoint: number of result pages can be reduced for testing - example: 10
* filename: name for the result file - example: 'crossref-events-from-proceedings.csv'
* fieldnames: set the metadata fields that should be read - example: ['name', 'start', 'end', 'acronym', 'location', 'number', 'sponsor', 'theme', 'proceedings-title', 'doi']

