# Import packages
import os
import geopandas as gpd
from ArealWeighting import ArealWeighting

# Identify working directory
wd.oschdir(r'C:\Users\zstat\Documents\RecurseCenter\EJ-analysis-map\'+
           'SpatialAnalysis\PopEstimation')

# Identify Census boundary, this shapefile must contain a column for total 
# population within each union (e.g., tract), population below the poverty line,
# and population people of color
cen_boundary = gpd(r'C:\Users\zstat\Documents\RecurseCenter\EJ-analysis-map\'+
                   'Data\Created\NJ_cen_data.shp')

# Identify public water system boundary data
pws_boundary = gpd('C:\Users\zstat\Documents\RecurseCenter\EJ-analysis-map\' +
                   'Data\NJDEP\New_Jersey__Public_Community_Water_Purveyor_Service_Areas.shp')



