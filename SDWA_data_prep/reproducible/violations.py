import pandas as pd

class Violations:
    
    def __init__(self, vio_df, pws_df):
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
        if not self.vio_by_pws:
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
        if not self.health_vio_by_pws:
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
        sdwa_vios = pd.merge(self.vio_by_pws(), self.health_vio_by_pws(), how='outer', on='PWSID')

        # Convert null values to 0
        sdwa_vios.fillna(0, inplace=True)

        #convert health_violations field type to int64 to match all violations
        sdwa_vios['health_violations'] = sdwa_vios['health_violations'].astype('int64')

        return sdwa_vios
        
