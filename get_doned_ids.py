import yaml

file = open('doned.yml')
data = yaml.safe_load(file)

res = list()
for i in data:
    res.append(i['_id'])

print(res)