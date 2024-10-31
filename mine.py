import pandas as pd 
import numpy as np
import logging



#got data for excel file !
data = [] ; 

def STOCHASTIC_RATE(TYPE , data):
    epselon = 1+(data['b']/data['a'])-(data['c']/data['a'])-(data['d']/data['a']);
    Ca = (data['Fa0'](1-data['conv']))/(data['VolumeFlowrate'] * (1-epselon)); 
    Cb = (data['Fa0']((data['Cb0']/data['Ca0'])-(data['b']/data['a'])*data['conv']))/(data['VolumeFlowrate'] * (1-epselon));     
    Cc = (data['Fa0']((data['Cc0']/data['Ca0'])+(data['c']/data['a'])*data['conv']))/(data['VolumeFlowrate'] * (1-epselon));
    Cd = (data['Fa0']((data['Cd0']/data['Ca0'])+(data['d']/data['a'])*data['conv']))/(data['VolumeFlowrate'] * (1-epselon)); 
    if TYPE == 'ELEMENTARY':      
        #convert elementary conv function      
        R = data['K'] * (Ca**data['a'])*(Cb**data['b']);
        return R 
    elif TYPE == 'EQUILIBRIUM': 
        R = data['K'] * (Ca**data['a'])*(Cb**data['b']) - (data['K_EQ']*(Cc**data['c'])*(Cd**data['d']));
        return R 
    

def CSTR_DSR(TYPE,Rate = None,Volume = None ,Molar_Flowrate = None):
    global data ;
    try : 
        if TYPE == 'Volume':
            
    except : 
        logging.warning('CSTR : Invalid Data .')
        

#import data from user 

