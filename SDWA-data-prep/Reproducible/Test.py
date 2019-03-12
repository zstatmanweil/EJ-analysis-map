

file = './SDWISData/vio_df_NJ.csv'
f = open(file, "r")

# vio_df = pd.read_csv(file)
#
# # Delete all rows that don't begin with 'NJ'
# vio_df = vio_df[vio_df['PWSID'].str.startswith('NJ')]
#
# vio = Violations(vio_df)
#
# # Print summary tables of total and health-based violations
# print(vio.get_vio_table().head(5))
# print(vio.get_health_vio_table().head(5))
# print(vio.get_total_vio_sum_table().head(5))
# print(vio.get_health_vio_sum_table().head(5))
#
# #Print name and ID of specific PWS
# PWS1 = PWS(vio_df, ID='NJ0102001')
# PWS1.display_name()
# PWS1.get_vio_total()
# PWS1.get_health_vio_total()
