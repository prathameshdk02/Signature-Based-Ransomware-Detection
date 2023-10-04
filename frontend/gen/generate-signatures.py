from pathlib import Path
from datetime import datetime
import hashlib
import json
import requests

samplePath = __file__ + '/../liveSamples'

samples = [file for file in Path(samplePath).iterdir() if file.is_file()]
sampleCount = len(samples)
hashGenerations = 0

obj_list = []

print(f"\nFile Hashes from \"{samplePath}\":")

for sample in samples:
    try:
        hash = hashlib.sha256(Path(sample).read_bytes()).hexdigest()
        hashGenerations += 1
        obj = {
            'name': sample.name,
            'extension': sample.suffix,
            'size': sample.stat().st_size,
            'creation-time': datetime.strftime(datetime.fromtimestamp(sample.stat().st_ctime),"%Y-%M-%d"),
            'hash': hash   
        }
        obj_list.append(obj)
    except Exception as e:
        print(e)

print(f"\nGenerated over {hashGenerations} hashes from {sampleCount} samples.\nEncountered Errors were {sampleCount - hashGenerations}")

final_obj = {
    'data': obj_list
}

with open("sampleData.txt","w") as sampleData:
    json.dump(final_obj,sampleData)


# json_obj = json.dumps(final_obj,indent=4)

# print(json_obj)


# response = requests.post('http://localhost:3000/scan',json=final_obj)
# print(response)









    