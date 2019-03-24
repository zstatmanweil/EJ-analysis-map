import pandas as pd
import geopandas as gpd
from variables import Variables
from model import NegBinModel
from summary_stats import SummaryStats
import os
import matplotlib.pyplot as plt

os.chdir('../data/Created/SpatialAnalysis')

# Select the dataset
data = 'AW_vios.geojson'
#data = 'county_vios.geojson'

# Read relevant file and confert to pandas DataFrame
gpddf = gpd.read_file(data).drop(columns='geometry')
df = pd.DataFrame(gpddf)

# Select violation data of interest
#vio_data = "all_violations"
vio_data = "health_violations"

# Add dummy variables
new_df = Variables(df)
new_df.add_all_variables()
complete_df = new_df.df

# Analyze data with negative binomial regression model (results will be table)
print("Results of Negative Binomial Regression Model:")
model = NegBinModel(complete_df, vio_data, data)
model.summarize()
print("\npearson chi2:", model.get_pearson())
#model.get_mle_retvals()

# Get violation predictions
model.get_predictions()

# Get summary stats
print("\nSummary stats for the continuous and categorical variables")
continuous_columns = ('perc_pov', 'perc_POC')
cat_columns = ("urban", "public","connections_less_200", "gw_or_combined")
summary = SummaryStats(complete_df, continuous_columns, cat_columns)
print("Continuous variables:\n", summary.cont_summary_table(), "\n")
print("Categorical variables:\n", summary.count_table())

# Get residuals
model.get_pearson_residuals()
model.get_deviance_residuals()
model.get_residuals()

# Explore residuals
print("\nPredictions and residuals:")
pd.set_option('max_columns', 7)
print (model.df[["predictions","std_pearson_residuals","std_deviance_residuals", "residuals"]].head(5))

#create plot of residuals
# =============================================================================
# plt.scatter(model.df["predictions"], model.df["std_deviance_residuals"], s=5, color="black")
# plt.xlabel("Predicted Value of Mean Response")
# plt.ylabel("Standardized Deviance Residuals")
# #plt.xlim([0,5])
# #plt.ylim([-3, 6])
# =============================================================================

# Export DataFrame to csv
#model.df.to_csv("../export/" + data[0:-9] + "_" + vio_data + ".csv")
