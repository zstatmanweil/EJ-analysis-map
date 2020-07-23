## Introduction

I am conducting the same type of spatial environmental justice analysis I did for my thesis on disparities in compliance with the Safe Drinking Water Act (SDWA), but this time entirely in Python rather than with desktop geospatial software (e.g., ArcGIS). Additionally, my thesis focused on Pennsylvania, but this project will focus on New Jersey so I can compare my results.  This project will give me the opportunity to use **geospatial Python libraries** (e.g., geopandas, rasterio), build a small **web application**, and create a beautiful and useful **web map** where the user can explore drinking water quality and environmental justice concerns.

## Research Questions

1) Are there social disparities in CWS compliance with the SDWA? Are there more violations (total and health-based) in low-income communities, communities with a higher proportion of people of color, and/or rural communities?

2) How do the results differ depending on the spatial analysis method used to estimate the demographic characteristics of the population served by the CWS? 

## Project Steps

- [x] Access Census data through the Census APIs, and use Jypter Notebooks to explore the demographic data by tract, specifically percent below the poverty line and percent people of color. 
  - [`census_data_prep/census.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/tree/master/census_data_prep/census.ipynb)
- [x] Access the SDWA violation data through the [Envirofacts REST API](https://www.epa.gov/enviro/other-service-enabled-data), and use Jupyter Notebooks to explore and organize the data. 
  - [`SDWA_data_prep/sdwis_data.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/tree/master/SDWA_data_prep/sdwis_data.ipynb)
- [x] Make an ad hoc data pipeline for accessing and organizing the public water system data from the Envirofacts REST API so the analysis is reproducible in other states.
  - [`SDWA_data_prep`](https://github.com/zstatmanweil/EJ-analysis-map/tree/master/SDWA_data_prep)
- [x] Etimate the population and the public water systems' sociodemographic characteristics within each water system through **areal weighting**. Create maps to visualize the results.
  - [`spatial_analysis/areal_weighting.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/blob/master/spatial_analysis/areal_weighting.ipynb)
- [ ] Etimate the population and the public water systems' sociodemographic characteristics within each water system through **dasymetric mapping**. Create maps to visualize the results.
  - *In progress:* [`spatial_analysis/dasymetric.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/blob/master/spatial_analysis/dasymetric.ipynb)
- [ ] Make the areal weighting and dasymetric processes reproducible through a chain of Python scripts.
- [x] Conduct a statistical analysis of the results to determine the correlation, if any, between the EJ variables and the SDWA violations. The negative binomial regression code I created for the Pennsylvania data can be found here: 
  - [`regression`](https://github.com/zstatmanweil/EJ-analysis-map/blob/master/regression) 
- [x] Get the map  and statistical results on the web!
  - The map is working! But is unfortunately not on the web. [`web_app`](https://github.com/zstatmanweil/EJ-analysis-map/blob/master/web_app)
  
![Website](https://github.com/zstatmanweil/EJ-analysis-map/blob/master/data/ej_website.png)

## Notes

A lot of my data analysis has been completed in Jupyter Notebooks, which is usually easily viewable on GitHub but sometimes does not load properly. If not loading, the notebooks can be viewed by cloning the repository and viewing in Jupyter Notebooks.  Jupyter Notebooks can be installed as follows if you have Python 3 installed:

`python3 -m pip install --upgrade pip` 

`python3 -m pip install jupyter`

To run the notebook, run the following command in your Terminal:

`jupyter notebook`



