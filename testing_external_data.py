import json

path_to_data= "C:\\Users/morte/Desktop/Datasets/AQuA/dev.json"

# load the data
# print the first 10 entries
# json.decoder.JSONDecodeError: Extra data: line 2 column 1 (char 447)
count = 0
with open(path_to_data) as f:
  for line in f:
        data = json.loads(line)
        print(data)
        if count == 10:
            break
        count += 1