#from violations import StateViolations

class PWS:
    
    def __init__(self, state_violation_class, ID):
        self.vio_sum = state_violation_class.get_pws_vio_sum_table()
        self.ID = ID
        
    def display_name(self):
        """Identifies the PWS name and ID in parentheses"""
        if self.ID in list(self.vio_sum.PWSID):
            name = self.vio_sum[self.vio_sum.PWSID==self.ID].iloc[0]['PWS_NAME']
            title_name = name.title()
            return f'{title_name} ({self.ID})'
        else:
            raise ValueError('That PWS ID is not in this dataset')
        
        
    def get_vio_total(self):
        """Provides the total number of violations for the specific PWS"""
        vio_sum_table = self.vio_sum.set_index('PWSID')
        
        if self.ID in list(vio_sum_table.index):
            return vio_sum_table.at[self.ID,'all_violations']
        else:
            raise ValueError('That PWS ID is not in this dataset')
        
    def get_health_vio_total(self):
        """Provides the total number of health violations for the specific PWS"""
        vio_sum_table = self.vio_sum.set_index('PWSID')
        
        if self.ID in list(vio_sum_table.index):
            return vio_sum_table.at[self.ID,'health_violations']
        else:
            raise ValueError('That PWS ID is not in this dataset')
        
        
        
        
        
        
        
        
    
    

