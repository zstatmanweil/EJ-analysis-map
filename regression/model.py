import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

class NegBinModel:
    
    def __init__(self, df, violation_type, data):
        self.data = data
        self.df = df
        self.violation_type = violation_type
        self.model_fit = None

        #define the target and predictors 
        self.target = self.df[self.violation_type]
        self.predictors = self.df[["perc_pov", 
                                      "perc_POC", 
                                      #"rural", 
                                      "public",
                                      "connections_less_200", 
                                      "gw_or_combined"
                                      ]]

    # Cache fit of model to reduce repetition 
    def fit(self):
        if not self.model_fit:
            self.model_fit = self.run().fit(maxiter=100)
        return self.model_fit
         
    def run(self):
        X = sm.add_constant(self.predictors)
        y = self.target
        
# =============================================================================
#         There are two ways to run the negative binomial regression using 
#         statsmodel. One way provides a value for alpha (dispersion paramater), 
#         and one does not but provides an easy way to get residuals. Thus, I 
#         ran the way that provides the alpha for each dataset, recorded alpha below, 
#         and reran with the method (GLM) that provides an easy way to analyze residuals. .
# =============================================================================
        alpha_data = {"all_violations": [2.8241, 2.8207],
                      "health_violations": [3.9016, 4.0531]}
        alpha_df = pd.DataFrame(alpha_data, index=['AW_vios.geojson','county_vios.geojson'])
        a = alpha_df.loc[self.data, self.violation_type]
        
        model = sm.GLM(y,X,family=sm.families.NegativeBinomial(alpha=a))
        
        # Method which provides alpha: 
        #model = sm.NegativeBinomial(y,X)
        return model      
    
    def summarize(self):        
        print(self.fit().summary2())
        
    def get_mle_retvals(self):
        print(self.fit().mle_retvals)
        
    def get_pearson(self):
        print(self.fit().pearson_chi2)
        
    def get_predictions(self):
        params = self.fit().params
        self.df["predictions"] = self.run().predict(params)
               
    def get_residuals(self):
        self.df["residuals"] = self.fit().resid_response
        
    def get_pearson_residuals(self):
        self.df["std_pearson_residuals"] = self.fit().resid_pearson
        
    def get_deviance_residuals(self):
        self.df["std_deviance_residuals"] = self.fit().resid_deviance
        
