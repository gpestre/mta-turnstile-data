# To handle dates:
from datetime import date,time,datetime,timedelta

# To handle webpage requests:
import requests
from lxml import html

# To handle data:
import numpy as np
import pandas as pd

# To preview HTML:
#from IPython.core.display import HTML

# Get Turnstile Data landing page:
session_requests = requests.session()
url = 'http://web.mta.info/developers/turnstile.html'
page_result = session_requests.get(
    url, 
    headers = dict(referer = url)
)
page_tree = html.fromstring(page_result.content)

# Get list of data files available for download:
data_files = []
for a in page_tree.xpath("//h2[contains(string(),'Data Files')]")[0].getparent().findall("a"):
    data_label = a.text
    data_date = datetime.strptime(data_label,"%A, %B %d, %Y").date()
    data_url = "http://web.mta.info/developers/" + a.attrib['href']
    data_files.append({'label':data_label,'date':data_date,'url':data_url})
data_files = pd.DataFrame(data_files,columns=['label','date','url'])
data_files

# Filter to only 2018 data:
#data_files = data_files[data_files['date']>=datetime(2018,1,1).date()]

# Download each data file:
for i,row in data_files.iterrows():
    
    data_csv = session_requests.get(
        row['url'], 
        headers = dict(referer = row['url'])
    ).text
    
    data_date = row['date'].strftime("%Y-%m-%d")
    data_filepath = '../data/mta-turnstile-data_{}.csv'.format(data_date)
    with open(data_filepath,'w') as f:
        f.write(data_csv+"\n")
    print("Saved : {}".format(data_filepath))
    
    now_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('../data/_mta-turnstile-data_download-log.txt','a') as log:
        log.write("{} : Downloaded mta-turnstile-data_{} .\n".format(now_date,data_date))
    
print("Done.")
