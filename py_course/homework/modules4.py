import requests
x = 'https://stepic.org/media/attachments/course67/3.6.3/'
y = '699991.txt'
z = ''
file = requests.get(x+y).text.split(' ')
while file[0] != 'We':
    y = file[0]
    z = x + y
    file = requests.get(z).text.split(' ')
    print(file)
file = requests.get(z).text
print(z)
