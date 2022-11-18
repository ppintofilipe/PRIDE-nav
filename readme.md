# PRIDEnav
---
## About
These are a couple of simple python scripts to help you navigate through [**PRIDE**](https://www.ebi.ac.uk/pride/) (The Proteomics Identifications Database) [1].

## Details
It fetches the most up to date metadata from PRIDE projects to help you navigate, select experiments, and set up your experimental design.

## Queried information
Basic data
* Accession ID
* Project title
* Licence
* URL to project
    
Metadata
* Organisms
* Tissue
* Diseases
* References

## How to use
Scripts are written in Python3.
To get the most up-to-date information, you can extract the datasets yourself (which takes about 20 minutes).
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```
then
```
python run.py
```
It will save a csv file in the ```data``` directory.

If you want to save some time, a snapshot is already saved and available on the ```data``` directory for you to use right away.

Enjoy :wink: