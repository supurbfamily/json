# created by: Subhojit
# purpose: Learn json and file operations

import json
import datetime
from os import path

sFName =  "myvalues.json"
jsonvals = ""
if path.exists(sFName):
    with open(sFName, "r") as jsf:
        jsonvals = jsf.read()
    print(jsonvals)

try:
    jsf = open(sFName, "a")

    timeval = datetime.datetime.now()

    print(len(jsonvals))

    # build once repeat each turn. 
    x = lambda a : '\n' + a if (len(a) > 0) else json.dumps({"token":30, "value":{"name":"SB", "mrn": str(timeval) }})

    jsf.writelines (x (jsonvals))

finally:
    jsf.close()
