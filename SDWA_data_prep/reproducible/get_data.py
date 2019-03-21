import numpy as np
import pandas as pd
import requests
import io

def get_vio_data_df(state, date_before, date_after):
    """Gets a DataFrame of violations within a given state and time period
    from the Envirofacts RESTful API. The begin and after date refers to the
    Compliance Beriod Begin Date, and Compliance Period End Date, respectively"""
    
    # Create url
    url = f'https://iaspub.epa.gov/enviro/efservice/SDW_VIOL_ENFORCEMENT/STATE/{state}/COMPPERBEGINDATE/>/{date_before}/COMPPERENDDATE/</{date_after}/CSV'
    
    r = requests.get(url)

    # Get data as pandas DataFrame
    if r.status_code == 200:
        vio_df = pd.read_csv(io.StringIO(r.text))
    else:
        raise Exception("Request was not valid. Code: {code}".format(code=r.status_code))
    
    # Clean headers and remove last "unnamed" column
    vio_df = clean_headers(vio_df, 'SDW_VIOL_ENFORCEMENT.').drop(labels='Unnamed: 20', axis=1)
    
    # Add columns for health-based violations
    add_health_based_vio_column(vio_df)
    
    # Remove any water systems that don't start with state ID
    vio_df = remove_other_state_pws(vio_df, state)
   
    return vio_df


def get_pws_data_df(state):
    """Gets a DataFrame of water systems within a given state and time period
    form the Envirofacts RESTful API."""
    
    # Create url
    url = f'https://iaspub.epa.gov/enviro/efservice/WATER_SYSTEM/STATE_CODE/{state}/CSV'
    r = requests.get(url)

    # Get data as pandas DataFrame
    if r.status_code == 200:
        pws_df = pd.read_csv(io.StringIO(r.text))
    else:
        raise Exception("Request was not valid. Code: {code}".format(code=r.status_code))
    
    # Clean headers and remove last "unnamed" column
    pws_df = clean_headers(pws_df, 'WATER_SYSTEM.').drop(labels='Unnamed: 47', axis=1)
   
    # Remove any water systems that don't start with state ID
    pws_df = remove_other_state_pws(pws_df, state)
    
    return pws_df

def clean_headers(df, to_remove):
    """Cleans up headers of a DataFrame downloaded from Enviro API"""
    for col in df.columns:
        df = df.rename(index=str, 
                columns={col: col.replace(to_remove,'')})
    return df

def add_health_based_vio_column(df):
    """Adds a column for health-based violations"""
    df['health_based'] = np.where(
                            (np.logical_or(df['VTYPE']=='MR',
                                           df['VTYPE']=='OTHER')),
                                           'N','Y')                        
    return df

def remove_other_state_pws(df, state):
    """Removes other states' water systems that end up in DataFrame"""
    df = df[df.PWSID.str.startswith(state)]
    return df   
