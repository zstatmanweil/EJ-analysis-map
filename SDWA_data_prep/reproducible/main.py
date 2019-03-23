from violations import StateViolations
from PWS import PWS
import get_data as data

# Identify parameters   
state = 'NJ'
date_before = '31-DEC-11'
date_after = '01-JAN-17' 

# Get all the SDWA violation data for the paramaters identified above
vio_df = data.get_vio_data_df(state, date_before, date_after)
print(vio_df.head())

# Get all the water system characteristic data for the state of interest
pws_df = data.get_pws_data_df(state)
print(pws_df.head())

# Create a violation class for this state of interest
vio = StateViolations(state, vio_df, pws_df)

# Print summary tables of PWS characteristics and total and health-based violations
#print(vio.get_total_vio_sum_table().head())
#print(vio.get_health_vio_sum_table().head())
#print(vio.get_vio_sum_table().head())
print(vio.get_pws_vio_sum_table().head())

# Get information about a specific water system
PWS1 = PWS(vio, ID='NJ0102001')
print(PWS1.display_name())
print(PWS1.get_vio_total())
print(PWS1.get_health_vio_total())

