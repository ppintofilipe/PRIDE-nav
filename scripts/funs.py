from . import vars
import os
import requests
import pandas as pd

def select_hot_field(local_dict):
    '''
    Select which output to mine from the specific metadata field.
    '''
    otp = []
    
    if 'value' in local_dict.keys():
        otp = local_dict['value']
    elif 'name' in local_dict.keys():
        otp = local_dict['name']
    elif 'doi' in local_dict.keys():
        otp = local_dict['doi']
    
    return(otp)

def extract_values(attr_list):
    '''
    Mines relevant information in the accession metadata.
    '''
    info = [select_hot_field(x) for x in attr_list]
    return(info)


def get_accession_metadata(acc_dict):
    '''
    Extracts information from the dictionary of the accession.
    '''
    
    accession = acc_dict['accession']
    title = acc_dict['title']
    licence = acc_dict['license']
    
    organisms = extract_values(acc_dict['organisms'])
    organismParts = extract_values(acc_dict['organismParts'])
    diseases = extract_values(acc_dict['diseases'])
    references = extract_values(acc_dict['references'])
    additionalAttributes = extract_values(acc_dict['additionalAttributes'])
    
    extracted_information = [accession, title, licence, organisms, organismParts, diseases, references, additionalAttributes]
    return(extracted_information)

def get_accessions_in_page(page):
    '''
    Gets available accessions per page.
    '''
    req_url = 'https://www.ebi.ac.uk/pride/ws/archive/v2/projects?pageSize=500&page=' + str(page) + '&sortDirection=DESC&sortConditions=submissionDate'
    
    page = requests.get(req_url)
    results = page.json()

    if '_embedded' in results.keys():
        proj_information = results['_embedded']
        instances = proj_information['projects']
        
        all_accessions = [get_accession_metadata(x) for x in instances]
    else:
        all_accessions = []
    
    return(all_accessions)

def obtain_all_experiments():
    '''
    Reads PRIDE for all available projects, so that these can be iterated later on.
    '''
    req_url = 'https://www.ebi.ac.uk/pride/ws/archive/v2/projects?pageSize=500&page=1&sortDirection=DESC&sortConditions=submissionDate'
    
    page = requests.get(req_url)
    results = page.json()
    
    pages = results['page']
    
    pages = pages['totalPages']
    
    total_accessions = [get_accessions_in_page(x) for x in range(1, pages+1)]
    total_accessions = [y for x in total_accessions for y in x]
    
    info_structured = pd.DataFrame(total_accessions, columns=['accession', 'title', 'licence', 'organisms', 'organismParts', 'diseases', 'references', 'additionalAttributes'])
    save_dev_database(info_structured)
    
    return(info_structured)

def save_dev_database(pandas_df):
    '''
    Saves the dataframe created as an explorable csv.
    '''
    
    export_name = os.path.join(vars.DATA_DIR, vars.DATABASE_DATE + '_dev_database.csv')
    pandas_df.to_csv(export_name, index=False)
