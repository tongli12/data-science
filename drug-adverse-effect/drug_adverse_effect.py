
# coding: utf-8

# In[1]:

import pandas as pd
import fnmatch
import os


# In[2]:

#api_key = 'akRNpS3NuuctC1HBWjDOT5q3JXAYXlvU0epO7Sv6'
#url = 'https://api.fda.gov/drug/event.json?api_key=yourAPIKeyHere&search=drug_


# In[2]:

import urllib2
import urllib
import json
import pprint


# In[4]:

# Download the Drug Adverse Effect files from FDA using API
# Put the details of the dataset we're going to create into a dict.
#dataset_dict = {
#    'name': 'my_dataset_name',
#    'notes': 'A long description of my dataset',
#}

# Use the json module to dump the dictionary to a string for posting.
#data_string = urllib.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
#request = urllib2.Request('https://open.fda.gov') #https://api.fda.gov/download.json') #Request('https://api.fda.gov/download.json')
#request
# Creating a dataset requires an authorization header.
# Replace *** with your API key, from your user account on the CKAN site
# that you're creating the dataset on.
#request.add_header('Authorization', 'akRNpS3NuuctC1HBWjDOT5q3JXAYXlvU0epO7Sv6')

# Make the HTTP request.
#response = urllib2.urlopen(request, data_string)
#assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
#response_dict = json.loads(response.read())
#assert response_dict['success'] is True

# package_create returns the created package as its result.
#created_package = response_dict['result']
#pprint.pprint(created_package)


# In[76]:

# Data of Drug Adverse Effect from FDA is stored in each quarter subfolders (Q1, Q2, Q3, Q4) \
# of year folders (2013, 2014, 2015). No data from Q3 and Q4 of 2015 year.
# Read each json file one by one from these folders
# 
folders = ['2013', '2014', '2015']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Automatically search the json files in these folders and store their path and file names
json_files = []
for folder in folders:
    for quarter in quarters:
        path = folder + '/' + quarter
        if not os.path.isdir(path)
        for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)) and fnmatch.fnmatch(name, '*.json'):
                json_files.append(name)

# Combine all the json data together
df_sum = pd.DataFrame()                
for json_file in json_files:
    #with open('2015/Q1/drug-event-0001-of-0004.json') as data_file:    
    print json_file
    with open(json_file) as data_file:
        data = json.load(data_file)
        print (data.keys())
        df = pd.DataFrame(data['results'])

        # Drop the columns that are not interesting
        removed_columns = ['authoritynumb', 'duplicate', 'primarysourcecountry', 'primarysource'                           'receiptdate', 'receiptdateformat','receivedateformat', 'receiver',                            'reporttype', 'reportduplicate', 'safetyreportversion', 'sender'                            'transmissiondate', 'transmissiondateformat']
        try:
            df = df.drop(removed_columns, axis=1)
            df_sum = df_sum.append(df)
        except ValueError:
            pass
df_sum.to_json('drug_adverse_effect_2014-15.json')


# In[ ]:

with open('drug_adverse_effect_2014-15.json') as data_file:
    data = json.load(data_file)
    df = pd.DataFrame(data['results'])
    #df[df['serious']=='1'].count()["serious"]
    #removed_columns = ['authoritynumb', 'duplicate', 'primarysourcecountry', 'primarysource'\
    #              'receiptdate', 'receiptdateformat','receivedateformat', 'receiver', \
    #              'reporttype', 'reportduplicate', 'safetyreportversion', 'sender' \
    #              'transmissiondate', 'transmissiondateformat']
    #df = df.drop(removed_columns, axis=1)
    df.head()


# In[78]:

#df.ix[:5, 13:]
df.to_json('test.json')


# In[ ]:

# What's the fraction of servious (1=yes or 2=no?
# How many deaths due to the drug adverse effect?
# The top ten drugs reported to have serious adverse effect. Note that it doesn't mean that these top ten drugs have
# more serious adverse effect than other drugs and these drugs ranked ahead maybe because more people have this kind of diseases 
# more people are using these drugs 
# Which drug leads to the most reported serious adverse effect? and From which pharaceutical company? Note that 


# In[ ]:



