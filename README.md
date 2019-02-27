## Introduction

I am conducting the same type of analysis I did for my thesis but this time entirely in Python rather than with desktop geospatial software. This project will give me the opportunity to use geospatial Python libraries, understand web development, and create a beautiful and useful web map where the user can explore drinking water quality and environmental justice concerns. My thesis focused on Pennsylvania, but this project will focus on New Jersey so I can compare my results and see how the results may differ between the two states.  

## Research Questions

1) Are there social disparities in CWS compliance with the SDWA? Are there more violations (total and health-based) in low-income communities, communities with a higher proportion of people of color, and/or rural communities?

2) How do the results differ depending on the spatial analysis method used to estimate the demographic characteristics of the population served by the CWS? 

## Tasks

- [x] Access and explore the Census demographic data by tractspecifically percent below the poverty line and percent people of color. [`EJ-analysis-map/Census/Census.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/tree/master/Census)
- [x] Use Jupyter Notebooks to explore public water system data, and estimate the population, and their sociodemographic characteristics, within each water system through areal weighting. [`EJ-analysis-map/SpatialAnalysis/ArealWeighting.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/blob/master/SpatialAnalysis/ArealWeighting.ipynb)
- [ ] Same as above but estimate population through dasymetric mapping. [`EJ-analysis-map/SpatialAnalysis/Dasymetric.ipynb`](https://github.com/zstatmanweil/EJ-analysis-map/blob/master/SpatialAnalysis/Dasymetric.ipynb)
- [ ] Create classes/functions that will automate the areal weighting and dasymetric processes for others to use.
- [ ] Create maps showing the results of my estimations.
- [ ] Conduct a statistical analysis of the results to determining the correlation, if any, between the EJ variables and the SDWA violations. The negative binomial regression code I created for the Pennsylvania data can be found here: [`NegBinomialModel`](https://github.com/zstatmanweil/NegBinomialModel) 
- [ ] Get those map  and statistical results on the web!





