import requests
x = 'https://stepic.org/media/attachments/course67/3.6.2/273.txt'
file = requests.get(x).text.splitlines()
print(file)
print(len(file))
