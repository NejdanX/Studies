from zipfile import ZipFile
import random
import json
import pydoc


count_human_living_in_moscow = 0
with ZipFile('A.zip') as myzip:
    files = [f.filename for f in myzip.filelist if 'json' in f.filename]
    for file in files:
        myzip.extract(file)
        with open(file, encoding='utf-8') as jsn:
            data = json.load(jsn)
            if isinstance(data, dict):
                count_human_living_in_moscow += (data['city'] == 'Москва')
            else:
                for item in data:
                    count_human_living_in_moscow += (item['city'] == 'Москва')
print(count_human_living_in_moscow)
