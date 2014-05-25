Berlin Marathon
===============

The official results from the Berlin marathons.
The python script [scraper.py](scripts/scraper.py) collects JSON data using the API offered by the [Berlin marathon website](http://www.bmw-berlin-marathon.com/files/addons/scc_events_data/ajax.results.php?) and writes it in csv format.
It was hacked together to get the job done; the code is ugly and uncommented.
Although data exists for every year since 1974, the API only offers the data since 2005.

Modifications
-------------

* Names were replaced by their SHA1 hash values
* Bib numbers were removed
* Team names were removed
* The abbreviations for nationalities were replaced by their [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) equivalents as far as possible.  
Missing entries were given a value of 'XXX'.
* Notation for age class was standardised as describle below.  
In particular, entries with no value or a value of 'M' or 'W' were set to 0.
* The id fields were removed

CSV format
----------

There are 9 fields, described below.
Some entries are missing for some runners.

|Field|Meaning|
|-----|-------|
|place|Ranking amongst all runners|
|netTime|Time in seconds measured by runner's chip|
|clockTime|Time in seconds measured from start of race|
|yob|Year of birth|
|ageClass|Age group|
|acPlace|Ranking amongst all runners in the same age group|
|sex|Sex of runner|
|nationality|Nationality of runner|
|name|SHA1 hash value of the name of the runner|

Nationalities
-------------

The file [abbreviations.csv](scripts/abbreviations) contains all country codes used.
The following abbreviations have not yet been identified:
* GAN 
* ISI
* KZK  
* MKO

Age classes
-----------

Below are the age groups used in the Berlin marathon.

|Code | Meaning  |
|-----|----------|
| 0 | No age class |
| U20 | Age under 20 |
| 20 | Age between 20 and 30 |
| 30 | Age between 30 and 35 |
| 35 | Age between 35 and 40 |
| 40 | Age between 40 and 45 |
| 45 | Age between 45 and 50 |
| 50 | Age between 50 and 55 |
| 55 | Age between 55 and 60 |
| 60 | Age between 60 and 65 |
| 65 | Age between 65 and 70 |
| 70 | Age between 70 and 75 |
| 75 | Age between 75 and 80 |
| 80 | Age between 80 and 85 |

