import requests
import json

def uploadDataset():
    dataPath = __file__ + '/../sampleData.json'
    # Read from the sampleData.json
    jsonData = {}
    with open(dataPath,'r') as file:
        jsonData = json.load(file)

    data = jsonData['data']

    # Send data in chunks of 300 objects...
    while (len(data) != 0):
        obj_frag = []
        count = 0
        while (len(data) != 0 and count < 300):
            obj_frag.append(data[-1].copy())
            data.pop()
            count += 1
        
        obj = {
            'data': obj_frag
        }
        response = requests.post('http://localhost:3000/scan',json=obj)
        print(response.json())
    
    return
