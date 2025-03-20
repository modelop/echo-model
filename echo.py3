import os
import json
import pandas as pd
#Echo model
#modelop.init
def begin():
    print(os.environ)
    pass

#modelop.score
def action(datum):
    yield datum

#modelop.metrics
def metrics(data):
    dict_data = data.to_dict(orient='records')
    json_string = json.dumps(dict_data)
    with open('/tmp/dataframe.json', 'w') as file:
        json.dump(dict_data, file, indent=4)
    yield dict_data
