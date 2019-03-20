## Introduction

I am conducting the same type of spatial environmental justice analysis I did for my thesis on disparities in compliance with the Safe Drinking Water Act (SDWA), but this time entirely in Python rather than with desktop geospatial software (e.g., ArcGIS). Additionally, my thesis focused on Pennsylvania, but this project will focus on New Jersey so I can compare my results.  This project will give me the opportunity to use geospatial Python libraries (e.g., geopandas, rasterio), understand web development, and create a beautiful and useful web map where the user can explore drinking water quality and environmental justice concerns.

## Research Questions

1) Are there social disparities in CWS compliance with the SDWA? Are there more violations (total and health-based) in low-income communities, communities with a higher proportion of people of color, and/or rural communities?

2) How do the results differ depending on the spatial analysis method used to estimate the demographic characteristics of the population served by the CWS? 

## Tasks

- [x] Access Census data through the Census APIs, and use Jypter Notebooks to explore the demographic data by tract, specifically percent below the poverty line and percent people of color. 
  - [`EJ-analysis-map/Census/Census-data-prep.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/tree/master/Census-data-prep/Census.ipynb)
- [x] Access the SDWA violation data through the [Envirofacts REST API](https://www.epa.gov/enviro/other-service-enabled-data), and use Jupyter Notebooks to explore and organize the data. 
  - [`EJ-analysis-map/SDWA-data-prep/SDWIS.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/tree/master/SDWA-data-prep/SDWISData.ipynb)
- [ ] Make the process of accessing and organizing the public water system data reproducible through a chain of Python scripts.
- [x] Etimate the population and the public water systems' sociodemographic characteristics within each water system through **areal weighting**. Create maps to visualize the results.
  - [`EJ-analysis-map/spatial-analysis/ArealWeighting.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/blob/master/spatial-analysis/ArealWeighting.ipynb)
- [ ] Etimate the population and the public water systems' sociodemographic characteristics within each water system through **dasymetric mapping**. Create maps to visualize the results.
  - [`EJ-analysis-map/spatial-analyss/Dasymetric.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/blob/master/spatial-analysis/Dasymetric.ipynb)
- [ ] Make the areal weighting and dasymetric processes reproducible through a chain of Python scripts.
- [ ] Conduct a statistical analysis of the results to determine the correlation, if any, between the EJ variables and the SDWA violations. The negative binomial regression code I created for the Pennsylvania data can be found here: 
  - [`NegBinomialModel`](https://github.com/zstatmanweil/NegBinomialModel) 
- [ ] Get the map  and statistical results on the web!





