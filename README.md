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
* The abbreviations for nationalities were replaced by their [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) equivalents as far as possible
* Team names were removed
* The id fields were removed

CSV format
----------

There are 9 fields, described below.
Some entries are missing for some runners.

|Field|Meaning|
|-----|-------|
|place|Ranking amongst all runners|
|netTime|Time measured by runner's chip|
|clockTime|Total time measured from start of race|
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
The meaning of `JA' has not yet been identified.

|Code | Meaning  |
|-----|----------|
| U20 | Under 20 |
| 30  | All runners between 30 and 35 |
| 35  | All runners between 35 and 40 |
| 40  | All runners between 40 and 45 |
| 45  | All runners between 45 and 50 |
| 50  | All runners between 50 and 55 |
| 55  | All runners between 55 and 60 |
| 60  | All runners between 60 and 65 |
| 65  | All runners between 65 and 70 |
| 70  | All runners between 70 and 75 |
| 75  | All runners between 75 and 80 |
| 80  | All runners between 80 and 85 |
| H   | Half marathon |
| JA  | ? |
| M   | Men |
| M30 | Men between 30 and 35 |
| M35 | Men between 35 and 40 |
| M40 | Men between 40 and 45 |
| M45 | Men between 45 and 50 |
| M50 | Men between 50 and 55 |
| M55 | Men between 55 and 60 |
| M60 | Men between 60 and 65 |
| M65 | Men between 65 and 70 |
| M70 | Men between 70 and 75 |
| M75 | Men between 75 and 80 |
| M80 | Men between 80 and 85 |
| MH  | Men's half marathon |
| MJA | ? |
| W   | Women |
| W30 | Women between 30 and 35 |
| W35 | Women between 35 and 40 |
| W40 | Women between 40 and 45 |
| W45 | Women between 45 and 50 |
| W50 | Women between 50 and 55 |
| W55 | Women between 55 and 60 |
| W60 | Women between 60 and 65 |
| W65 | Women between 65 and 70 |
| W70 | Women between 70 and 75 |
| W75 | Women between 75 and 80 |
| W80 | Women between 80 and 85 |
| WH  | Women's half marathon |
| WJA | ? |

