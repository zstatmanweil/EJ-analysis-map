import numpy as np
import pandas as pd
import requests
import io

state = 'NJ'
begindate_after = '31-DEC-11'
begindate_before = '01-JAN-17'
url = "https://iaspub.epa.gov/enviro/efservice/SDW_VIOL_ENFORCEMENT/STATE/" + \
"{state}/COMPPERBEGINDATE/>/{before}/COMPPERENDDATE/</{after}/CSV".format(state=state, 
                    before=begindate_after, 
                    after=begindate_before)
r = requests.get(url)

# Get data as pandas DataFrame
if r.status_code == 200:
    vio_df = pd.read_csv(io.StringIO(r.text))
else:
    raise Exception("Request was not valid. Code: {code}".format(code=r.status_code))

# Clean up headers
for col in vio_df.columns:
    vio_df = vio_df.rename(index=str, 
                           columns={col: col.replace('SDW_VIOL_ENFORCEMENT.','')})
  
# Add 'health_based' column
vio_df['health_based'] = np.where(
                        (np.logical_or(vio_df['VTYPE']=='MR',
                                       vio_df['VTYPE']=='OTHER')),
                                       'N','Y')                        
                        
vio_df.to_csv(r'C:\Users\zstat\Documents\RecurseCenter\EJ-analysis-map\SDWA\Reproducible\SDWISData\vio_df_NJ.csv')