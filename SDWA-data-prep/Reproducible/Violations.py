import pandas as pd

class Violations:
    
    def __init__(self, vio_df):
        self.vio_df = vio_df
            
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
        pivot = self.get_vio_table()
        vio_by_pws = pd.pivot_table(pivot,index=['PWSID'],aggfunc='count')
        vio_by_pws = vio_by_pws.reset_index().drop(columns='health_based')
        vio_by_pws = vio_by_pws.rename(columns={'VIOID': 'All_Violations'})
        return vio_by_pws
        
    def get_health_vio_sum_table(self):
        """Creates  a DataFrame listing a count of health-based violations by
        PWSID and PWSNAME"""
        health_pivot = self.get_health_vio_table()
        health_vio_by_pws = pd.pivot_table(health_pivot,index=['PWSID'],aggfunc='count')
        health_vio_by_pws = health_vio_by_pws.reset_index()
        health_vio_by_pws = health_vio_by_pws.rename(columns={'VIOID': 'Health_Violations'})
        return health_vio_by_pws
    
        