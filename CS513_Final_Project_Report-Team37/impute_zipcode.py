import sys
import urllib.request
import json
import pandas as pd
import numpy as np
df = pd.read_csv("farmersmarkets_openrefined.csv")

url = 'https://api.tomtom.com/search/2/reverseGeocode/{geocode}.json?key=Y86v3lNqi3XRTCZoeR616WLfyCSSmg14'
for index, row in df.iterrows():
        if ((row['zip'] is np.nan) and not np.isnan(row['Latitude']) and not np.isnan(row['Longitude'])):
            tobereplaced = str(row['Latitude'])+","+str(row['Longitude'])
            url1 = url.replace("{geocode}",tobereplaced)
		 print(url1)
            req = urllib.request.urlopen(url1)
            data = req.read().decode('utf-8')
            obj = json.loads(data)
            zip1 = str(obj["addresses"][0]["address"]["postalCode"])
            df.loc[index,'zip']=zip1
df.to_csv('farmersmarkets_imputed.csv',index=False)
