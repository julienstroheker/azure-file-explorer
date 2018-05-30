import os

from flask import Flask,json
from azure.storage.common import CloudStorageAccount
from azure.common import AzureHttpError

STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
STORAGE_ACCOUNT_KEY = os.getenv("STORAGE_ACCOUNT_KEY")
SHARE_NAME = os.getenv("SHARE_NAME")

print("Authentication")
account = CloudStorageAccount(account_name=STORAGE_ACCOUNT_NAME,
                                    account_key=STORAGE_ACCOUNT_KEY, sas_token='')
print("fileSvc Service")
filesvc = account.create_file_service()

app = Flask(__name__)

@app.route('/')
def list_directory():
    data = {}
    i=0
    try:
        root_file_dir = list(filesvc.list_directories_and_files(SHARE_NAME))
    except AzureHttpError as e:
        print("AzureHttpError {}".format(e))
        return("Error - See logs")
    for res in root_file_dir:
        data[i] = res.name
        i = i+1
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')