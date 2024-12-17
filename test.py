# adding more data to the dictionary.
"""

dict = {
    "key":"value",
}
dict[key] = value
print(dict)

"""

import json

def save(front:str, back:str):
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    
    data[front] = back
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
    return True

save("1dsdsddsdsddsdsd", "2dsdsdsdsdsd")