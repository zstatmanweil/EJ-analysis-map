from violations import Violations
from PWS import PWS
import pandas as pd
import get_data as data

# Get violation data
state = 'NJ'
date_before = '31-DEC-11'
date_after = '01-JAN-17' 

vio_df = data.get_vio_data_df(state, date_before, date_after)
print(vio_df.head())

pws_df = data.get_pws_data_df(state)
print(pws_df.head())

vio = Violations(vio_df, pws_df)

## Print summary tables of total and health-based violations
print(vio.get_vio_table().head())
#print(vio.get_health_vio_table().head())
#print(vio.get_total_vio_sum_table().head())
#print(vio.get_health_vio_sum_table().head())
print(vio.get_vio_sum_table().head())

#Print name and ID of specific PWS
WS1 = PWS(vio_df, ID='NJ0102001')
WS1.display_name()
WS1.get_vio_total()
WS1.get_health_vio_total()

