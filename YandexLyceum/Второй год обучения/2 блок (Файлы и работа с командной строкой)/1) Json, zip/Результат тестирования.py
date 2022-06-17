import json


with open('scoring.json') as jsn:
    data = json.load(jsn)
result = 0
tests_verdict = [input() for i in range(1, 34)]
for item in data['scoring']:
    for i in item['required_tests']:
        if tests_verdict[i - 1] == 'ok':
            result += (item['points'] // len(item['required_tests']))
print(result)

