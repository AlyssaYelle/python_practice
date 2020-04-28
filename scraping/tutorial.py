import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# print(page) --> <Response [200]>
# print(page.status_code) --> 200
# print(page.content) --> prints the html for specified url
# b'<!DOCTYPE html>\n<html>\n    <head>\n        <title>A simple example page</title>\n    </head>\n    <body>\n        <p>Here is some simple content for this page.</p>\n    </body>\n</html>'



soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify()) --> prints same html as page.content but displayed nicely
''' print(list(soup.children)) --> ['html', '\n', <html>
<head>
<title>A simple example page</title>
</head>
<body>
<p>Here is some simple content for this page.</p>
</body>
</html>]
'''
# print([type(item) for item in list(soup.children)]) --> [<class 'bs4.element.Doctype'>, <class 'bs4.element.NavigableString'>, <class 'bs4.element.Tag'>]

# html = list(soup.children)[2]

'''
print(html)
<html>
<head>
<title>A simple example page</title>
</head>
<body>
<p>Here is some simple content for this page.</p>
</body>
</html>
'''

'''
print(list(html.children))
['\n', <head>
<title>A simple example page</title>
</head>, '\n', <body>
<p>Here is some simple content for this page.</p>
</body>, '\n']
'''


# body = list(html.children)[3]

'''
print(body)
<body>
<p>Here is some simple content for this page.</p>
</body>
'''

'''
print(list(body.children))
['\n', <p>Here is some simple content for this page.</p>, '\n']
'''

# p = list(body.children)[1]
# text = p.get_text()

# print(text) --> Here is some simple content for this page.

# print(soup.find_all('p')) --> [<p>Here is some simple content for this page.</p>]

# print(soup.find_all('p')[0].get_text()) --> Here is some simple content for this page.
# soup.find finds first instance




''' we can also search by class and ids '''


page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
'''
<html>
<head>
<title>A simple example page
</title>
</head>
<body>
<div>
<p class="inner-text first-item" id="first">
First paragraph.
</p><p class="inner-text">
Second paragraph.
</p></div>
<p class="outer-text first-item" id="second"><b>
First outer paragraph.
</b></p><p class="outer-text"><b>
Second outer paragraph.
</b>
</p>
</body>
</html>
'''

# finds any <p> tag with class outer-text
# print(soup.find_all('p', class_='outer-text'))

# finds any item with class outer-text
# print(soup.find_all(class_="outer-text"))

# can also search by id
# print(soup.find_all(id="first"))

# find all <p> inside a <div>
print(soup.select("div p"))






















