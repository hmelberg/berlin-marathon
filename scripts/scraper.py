#!/usr/bin/env python

from urllib.error import  URLError
import urllib.request
import urllib.parse
import json
import time
import csv
import hashlib
import re, os, random, operator

years = {
        #'1974',
        #'1975',
        #'1976',
        #'1977',
        #'1978',
        #'1979',
        #'1980',
        #'1981',
        #'1982',
        #'1983',
        #'1984',
        #'1985',
        #'1986',
        #'1987',
        #'1988',
        #'1989',
        #'1990',
        #'1991',
        #'1992',
        #'1993',
        #'1994',
        #'1995',
        #'1996',
        #'1997',
        #'1998',
        #'1999',
        #'2000',
        #'2001',
        #'2002',
        #'2003',
        #'2004',
        '2005',
        '2006',
        '2007',
        '2008',
        '2009',
        '2010',
        '2011',
        '2012',
        '2013',
}

keys = [ 
    'id', 
    'place', 
    'bib', 
    'surname', 
    'forename', 
    'team', 
    'nationality', 
    'yob', 
    'sex', 
    'ageClass', 
    'acPlace', 
    'netTime', 
    'clockTime' 
]
fieldnames=[ 
    "place", 
    "netTime",
    "clockTime",
    "yob",
    "ageClass",
    "acPlace",
    "sex",
    "nationality",
    "name",
]

def makeQuery( year, page ):
    url = "http://www.bmw-berlin-marathon.com/files/addons/scc_events_data/ajax.results.php"
    params =  { 't': 'BM_{}'.format(year), 'ci': 'MAL', 'page': str(page) }
    data = urllib.parse.urlencode( params )
    return url + '?' + data

def getData(year,page=1):

    time.sleep( 5 )

    query = makeQuery( year, page )
    try:
        response = urllib.request.urlopen( query )
    except URLError as e:
        data = { 'page': None, 'total': None, 'records': None, 'rows': None }
        if hasattr(e, 'reason'):
            print("We failed to reach a server.")
            print("Reason: ", e.reason)
        elif hasattr(e, 'code'):
            print("The server couldn't fulfill the request.")
            print("Error code: ", e.code)
    except timeout:
        print("Timed out")
    else:
        data = json.loads( response.read().decode('utf-8') )

    return data

def getMeta(year):
    jData = getData(year)
    return { 'currentPage': int(jData['page']), 'numOfPages': int(jData['total']), 'numOfEntries': int(jData['records']) }

def cleanData(jData):

    data = [ dict( zip( keys, entry['cell'] ) ) for entry in jData['rows'] ]

    with open('abbreviations.csv') as abvs:
        rows = csv.DictReader(abvs)
        abbreviations = { row['Abbreviation']:row['ISO 3166-1 alpha-3'] for row in rows }

    for row in data:

        name = re.sub( r"[-.,_'!?0-9]+|\s+", '', ( row['forename'] + row['surname'] ).lower() )
        nameHash = hashlib.sha1( name.encode() ).hexdigest()
        row['name'] = nameHash

        row['nationality'] = abbreviations.get( row['nationality'], row['nationality'] )
        if not row['nationality']:
            row['nationality'] = 'XXX'

        ac = row['ageClass']
        if ac in {'M','W'} or not ac:
            ac = '0'
        elif ac[0] in {'M','W'} and len(ac) > 1:
            ac = ac[1:]
        if ac == 'JA':
            ac = 'U20'
        if ac == 'H':
            ac = '20'
        row['ageClass'] = ac

        netTime = datetime.datetime.strptime( row['netTime'], '%H:%M:%S' )
        netTimeDelta = datetime.timedelta( hours=netTime.hour, minutes=netTime.minute, seconds=netTime.second )
        row['netTime'] = netTimeDelta.seconds

        clockTime = datetime.datetime.strptime( row['clockTime'], '%H:%M:%S' )        
        clockTimeDelta = datetime.timedelta( hours=clockTime.hour, minutes=clockTime.minute, seconds=clockTime.second )
        row['clockTime'] = clockTimeDelta.seconds

        row['place'] = int( row['place'] )

        del row['forename']
        del row['surname']
        del row['team']
        del row['id']
        del row['bib']

    return sorted( data, key=lambda k: k['place'] )

def add2dataset(jData,year):
    data = cleanData(jData)
    with open('{}.csv'.format(year),'a') as dataset:
        dictWriter = csv.DictWriter( dataset, fieldnames )
        [ dictWriter.writerow(row) for row in data ]

if __name__ == '__main__':

    for year in years:
        print("Collecting data for year {}...".format(year))
        with open('{}.csv'.format(year),'w') as empty:
            csv.DictWriter( empty, fieldnames ).writeheader()
        meta = getMeta(year)
        print("...there are officially {0} records for year {1}".format(meta['numOfEntries'], year))
        pages = meta['numOfPages']
        for page in range(pages):
            print("...page {0} of {1}".format(page+1,pages))
            add2dataset( getData(year,page+1), year )

