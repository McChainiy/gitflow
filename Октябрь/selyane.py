from zipfile import ZipFile
import json

tough = 0

with ZipFile('input.zip') as myzip:
    for i in myzip.namelist():
        if i.split('.')[-1] == 'json':
            file = json.loads(myzip.read(i))
            if file['city'] == 'Москва':
                tough += 1
print(tough)
