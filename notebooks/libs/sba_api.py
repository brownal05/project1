import json
import pandas as pd 
import numpy as np
from pprint import pprint

sba_df = pd.read_json("./raw_data/sba_data.json")
#json_read = (json_file).json
sba_df.head()