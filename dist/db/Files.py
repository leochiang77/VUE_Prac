import os
import glob
from dotenv import load_dotenv

load_dotenv()
transDict = {
    "CVD":"CVD_FILE_LOCATION",
    "SPT":"SPT_FILE_LOCATION"
}

def get_daily_move_textarea(unitid):
    FILE_LOCATION = os.environ.get(transDict[unitid])
    res=[]
    for file in glob.glob(f"{FILE_LOCATION}/*.txt"):
        tempDict = {}
        with open(file, 'r',encoding='big5') as f:
            tempDict["FILENAME"] = file.split('\\')[-1]
            tempDict["CONTENT"] = f.read()
        res.append(tempDict)

    return res