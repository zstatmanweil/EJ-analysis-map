from violations import StateViolations

class PWS:
    
    def __init__(self, state, vio_df, pws_df, ID):
        self.vio_df = vio_df
        self.ID = ID
        self.vio_sum = StateViolations(state, vio_df, pws_df)
        
    def display_name(self):
        """Identifies the PWS name and ID in parentheses"""
        name = self.vio_df[self.vio_df.PWSID==self.ID].iloc[0]['PWSNAME']
        title_name = name.title()
        return f'{title_name} ({self.ID})'
        
    def get_vio_total(self):
        """Provides the total number of violations for the specific PWS"""
        vio_sum_table = self.vio_sum.get_pws_vio_sum_table().set_index('PWSID')
        return vio_sum_table.at[self.ID,'all_violations'] 
        
    def get_health_vio_total(self):
        """Provides the total number of health violations for the specific PWS"""
        vio_sum_table = self.vio_sum.get_pws_vio_sum_table().set_index('PWSID')
        return vio_sum_table.at[self.ID,'health_violations'] 
        
        
        
        
        
        
        
        
    
    

