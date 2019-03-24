import pandas as pd
import numpy as np

class Variables(object):
    
    def __init__(self, df):
        self.df = df
        
    def add_all_variables(self):
        self.rural_urban()
        self.owner_type_public()
        self.few_sewer_connections()
        self.groundwater_source()

    # Get dummy variables for rural vs urban and owner type and 
    # concactenate to original table 
    def rural_urban(self):
        dummyUR = pd.get_dummies(self.df['urban_rural'])
        self.df = pd.concat([self.df, dummyUR], axis=1)
   
    # Create a private vs public variable
    def owner_type_public(self):
        self.df["public"] = np.where(
                (np.logical_or(self.df["owner_type"]=="Private", self.df["owner_type"]=="Public/Private")), 0, 1)
        
    # Create a column identifying all public water systems with service connections less than 200
    def few_sewer_connections(self):
        self.df["connections_less_200"] = np.where(
                self.df["SERVICE_CONNECTIONS_COUNT"] <= 200, 1, 0)
        
    # Create a column identifying all public water systems with groundwater sources
    def groundwater_source(self):
        self.df["gw_or_combined"] = np.where(
                (np.logical_or(self.df["primary_source"] ==
                "Surface water purchased", self.df["primary_source"] =="Surface water")), 0, 1)
