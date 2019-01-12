#Use to find dataset parameters needed ie parameters("Regional")
#Use to find parameter values of the required parameters / parameters("linecode") ***only avail for Regional at the moment
# additional arguments:
# view = True, displays on the terminal - default false
# csv = True, outputs to output.csv - default false

import requests
import pandas as pd
method = ("GetData", "GetParameterList", "GETDATASETLIST", "GetParameterValues")

def parameters(x, view=False, csv=False):   
    count =+1
    paras = []
    parameter_values = (x)

    try:
        response = requests.get(f"{url}{method[3]}&datasetname=Regional&ParameterName={parameter_values}").json() 
        paras.append(response["BEAAPI"]["Results"]["ParamValue"])
        if view == True:
            pprint(response)
        elif csv == True:
            paras = pd.DataFrame(paras)
            paras.to_csv("output.csv")  
        else:
            print(f"Parameters Retrived")
            

                
        response = requests.get(f"{url}{method[3]}&datasetname=Regional&ParameterName={parameter_values}").json() 
        paras.append(response["BEAAPI"]["Results"]["ParamValue"])
        if view == True:
            pprint(response)
        elif csv == True:
            paras = pd.DataFrame(paras)
            paras.to_csv("output.csv")  
        else:
            print(f"error")
            
    except:
        response = requests.get(f"{url}{method[1]}&datasetname={parameter_values}").json() 
        paras.append(response["BEAAPI"]["Results"]["Parameter"])
        if view == True:
            pprint(response)
        elif csv == True:
            paras = pd.DataFrame(paras)
            paras.to_csv("output.csv")  
        else:
            print(f"Parameters Retrived") 
    return