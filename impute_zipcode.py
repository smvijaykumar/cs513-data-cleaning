import sys
import urllib.request
import json
import pandas as pd
import numpy as np
df = pd.read_csv("farmersmarkets.csv")

url = 'https://api.tomtom.com/search/2/reverseGeocode/{geocode}.json?key=Y86v3lNqi3XRTCZoeR616WLfyCSSmg14'
for index, row in df.iterrows():
        if ((row['zip'] is np.nan) and not np.isnan(row['y']) and not np.isnan(row['x'])):
            tobereplaced = str(row['y'])+","+str(row['x'])
            url1 = url.replace("{geocode}",tobereplaced)
            req = urllib.request.urlopen(url1)
            data = req.read().decode('utf-8')
            obj = json.loads(data)
            zip1 = str(obj["addresses"][0]["address"]["postalCode"])
            df.loc[index,'zip']=zip1
df.to_csv('out1.csv',index=False)
