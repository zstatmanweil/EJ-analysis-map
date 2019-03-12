import geopandas as gpd

class ArealWeighting:
    
    def __init__(self, PWS_gdf, census_gdf, PWSID, total_pop, pop_pov, pop_poc):
        self.census_gdf = census_gdf
        self.PWS_gdf = PWS_gdf
        self.PWSID = PWSID
        self.total_pop = total_pop
        self.pop_pov = pop_pov
        self.pop_poc = pop_poc
        
    def get_census_area(self):
        self.census_gdf['census_area'] = self.census_gdf.geometry.area
        
    def get_pop_estimation(self):
        #Add tract area
        self.census_gdf.get_census_area()
        
        union = gpd.overlay(self.census_gdf, self.PWS_gdf, how='union')
        union['union_area'] = union.geometry.area
        union['union_total_pop'] = (union['union_area'] / union['census_area']) * self.total_pop
        
        # Once I get this working, I can maybe loop through all the EJ variables 
        # so the user can add as many as they want
        union['union_pov_pop'] = (union['union_area'] / union['census_area']) * self.pov_pop
        union['union_POC_pop'] = (union['union_area'] / union['census_area']) * self.pop_poc
        
        PWS_union = union.dropna(subset=self.PWSID)
        PWS_dissolve = PWS_union['PWID','geometry','union_area','union_total_pop',
                                 'union_pov_pop','Union_POC_pop']
        PWS_dissolve['geometry'] = PWS_dissolve.buffer(0.01)
        
        PWS_agg = PWS_dissolve.dissolve(by=self.PWSID,aggfunc='sum')
        PWS_agg['perc_pov'] = PWS_agg['Union_pov_pop'] / PWS_agg['union_total_pop']
        PWS_agg['perc_poc'] = PWS_agg['Union_poc_pop'] / PWS_agg['union_total_pop']
        
        return pws_agg
        
    
        
        
    

