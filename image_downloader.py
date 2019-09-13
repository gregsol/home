import requests
import bs4 as bs
import os

path = os.getcwd()

print ('Please, enter a valid URL in the following format: https://facebook.com/')
url = str(input('URL: '))

split = url.split('/')
folder = path +'/downloads/' + split[2]
if not os.path.exists(folder):
    os.makedirs(folder)

raw = requests.get(url).text
soup = bs.BeautifulSoup(raw, 'html.parser')

imgs = soup.find_all('img')

links = []

for img in imgs:
    link = img.get('src')
    if 'https://' not in link:
        link = url + link
    links.append(link)

print('Images detected: ' + str(len(links)))

for i in range(len(links)):
    print(links[i])
    p = requests.get(links[i])
    filename = 'img{}.png'.format(i)
    filepath = folder + '/' + filename
    out = open(filepath, "wb")
    out.write(p.content)
    out.close()

print('Images successfully downloaded')