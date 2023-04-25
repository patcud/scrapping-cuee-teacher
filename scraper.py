from bs4 import BeautifulSoup
import requests
import csv

url = "https://ee.eng.chula.ac.th/faculty/"
res = requests.get(url)
res.encoding = "utf-8"
print(res)

soup = BeautifulSoup(res.text, 'html.parser')
results = soup.find(class_="entry-content")
# print(results.prettify())

header = ['#','email','name']
data = []
teachers = results.find_all("figcaption", class_="wp-element-caption")
for i in range(len(teachers)):
    row = []
    row.append(i)
    row.append(teachers[i].find_all("a")[1].text)
    row.append(teachers[i].find("strong").text)
    data.append(row)

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)