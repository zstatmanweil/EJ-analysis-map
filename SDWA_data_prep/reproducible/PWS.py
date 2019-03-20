from Violations import Violations

class PWS:
    
    def __init__(self, vio_df, ID):
        self.vio_df = vio_df
        self.ID = ID
        self.vio_sum = Violations(vio_df)
        
    def display_name(self):
        """Identifies the PWS name and ID in parentheses"""
        name = self.vio_df[self.vio_df.PWSID==self.ID].iloc[0]['PWSNAME']
        print('{name} ({ID})'.format(name=name, ID=self.ID))
        
    def get_vio_total(self):
        """Provides the total number of violations for the specific PWS"""
        vio_sum_table = self.vio_sum.get_total_vio_sum_table().set_index('PWSID')
        
        # Check to see if PWS recieved violation during period of interest
        if self.ID in list(vio_sum_table.index):
            total = vio_sum_table.at[self.ID,'All_Violations'] 
            print(total)
        else:
            print(0)
        
    def get_health_vio_total(self):
        """Provides the total number of health violations for the specific PWS"""
        vio_sum_table = self.vio_sum.get_health_vio_sum_table().set_index('PWSID')
        
        # Check to see if PWS recieved health-based violation during period of interest
        if self.ID in list(vio_sum_table.index):
            total = vio_sum_table.at[self.ID,'Health_Violations'] 
            print(total)
        else:
            print(0)
        
        
        
        
        
        
        
        
    
    

