import pandas as pd

class StateViolations:
    
    def __init__(self, state, vio_df, pws_df):
        self.state = state
        self.vio_df = vio_df
        self.pws_df = pws_df
        # Creating variables to cache violation summary tables to reduce repetition
        self.vio_by_pws = None
        self.health_vio_by_pws = None
            
    def get_vio_table(self):
        """Creates  a DataFrame listing each violation and whether its health-based
        by PWSID and PWSNAME"""
        pivot = pd.pivot_table(self.vio_df,index=['PWSID','PWSNAME','VIOID','health_based'])
        pivot = pivot.reset_index().drop(columns=['CCODE','VCODE'])
        
        return pivot[['PWSID','PWSNAME','VIOID','health_based']]
    
    def get_health_vio_table(self):
        """Creates  a DataFrame listing each health-based violation by PWSID 
        and PWSNAME"""
        health_vio_df = self.vio_df[self.vio_df.health_based=='Y']
        health_pivot = pd.pivot_table(health_vio_df,index=['PWSID','PWSNAME','VIOID'])
        health_pivot = health_pivot.reset_index().drop(columns=['CCODE','VCODE'])
        
        return health_pivot[['PWSID','PWSNAME','VIOID']]

    def get_total_vio_sum_table(self):
        """Creates  a DataFrame listing a count of violations by PWSID and PWSNAME"""
        if self.vio_by_pws is None:
            pivot = self.get_vio_table()
            self.vio_by_pws = pd.pivot_table(pivot,
                                            index=['PWSID'],
                                            aggfunc='count')
            self.vio_by_pws = self.vio_by_pws.reset_index().drop(columns='health_based')
            self.vio_by_pws = self.vio_by_pws.rename(columns={'VIOID': 'all_violations'})
        return self.vio_by_pws
        
    def get_health_vio_sum_table(self):
        """Creates  a DataFrame listing a count of health-based violations by
        PWSID and PWSNAME"""
        if self.health_vio_by_pws is None:
            health_pivot = self.get_health_vio_table()
            self.health_vio_by_pws = pd.pivot_table(health_pivot,
                                                    index=['PWSID'],
                                                    aggfunc='count')
            self.health_vio_by_pws = self.health_vio_by_pws.reset_index()
            self.health_vio_by_pws = self.health_vio_by_pws.rename(
                                                    columns={'VIOID': 'health_violations'})
        return self.health_vio_by_pws
    
    def get_vio_sum_table(self):
        """Creates a DataFrame listing a count of total and health-based
        violations by PWSID and PWSNAME"""
       
        # Merge tables into one dataset
        sdwa_vios = pd.merge(self.get_total_vio_sum_table(), 
                             self.get_health_vio_sum_table().drop(columns='PWSNAME'), 
                             how='outer', 
                             on='PWSID')

        # Convert null values to 0
        sdwa_vios.fillna(0, inplace=True)

        # Convert health_violations field type to int64 to match all violations
        sdwa_vios['health_violations'] = sdwa_vios['health_violations'].astype('int64')
        
        return sdwa_vios
    
    def get_pws_vio_sum_table(self):
        """Creates a DataFrame listing a count of total and health-based
        violations by PWSID and PWSNAME, including key PWS characteristics"""
        
        # Filter down to active community water systems in NJ
        filters = (self.pws_df.STATE_CODE == self.state) & \
                    (self.pws_df.PWS_ACTIVITY_CODE == 'A') & \
                    (self.pws_df.PWS_TYPE_CODE == 'CWS')
        self.pws_df = self.pws_df[filters]    

        # Only utilize necessary columns
        pws_clean = self.pws_df.filter(['PWSID',
                                   'PRIMARY_SOURCE_CODE',
                                   'OWNER_TYPE_CODE', 
                                   'SERVICE_CONNECTIONS_COUNT',
                                   'COUNTIES_SERVED'], axis=1)
    
        # Merge with the violation data
        sdwa_vios_merged = pd.merge(pws_clean, 
                                    self.get_vio_sum_table(), 
                                    how='left', 
                                    on='PWSID', 
                                    validate="one_to_one")
        
        # Convert columns with codes to descriptions
        sdwa_vios_merged = self.column_codes_to_descriptions(sdwa_vios_merged)
        
        # Replace all null values in the violation fields with with 0 since if there 
        # isn't violation data  for a water system that means the water system did not 
        # recieve a violation.
        sdwa_vios_merged.fillna(0, inplace=True)
        
        return sdwa_vios_merged
    
    def column_codes_to_descriptions(self, df):
        """Converts PWS characteristics codes (e.g., Owner Type) to 
        descriptions"""
        
        primary_source = {'GW': 'Ground water', 
                          'SW': 'Surface water', 
                          'SWP': 'Surface water purchased', 
                          'GWP': 'Groundwater purchased',
                          'GU': 'Ground water under influence of surface water source'}
        
        owner_type = {'M': 'Mixed', 
                      'S': 'State Government', 
                      'F': 'Federal Government', 
                      'P': 'Private', 
                      'L': 'Local Government'}
        
        df['primary_source'] = df['PRIMARY_SOURCE_CODE'].apply(
                                                        lambda code: 
                                                        primary_source.get(code)
                                                        )
        df['owner_type'] = df['OWNER_TYPE_CODE'].apply(lambda code: 
                                                        owner_type.get(code)
                                                        )
        
        return df

    
        
