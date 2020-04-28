import requests
from bs4 import BeautifulSoup

# set url
url = "https://cooking.nytimes.com/recipes/1019944-vegan-broccoli-soup-with-cashew-cream"

# get page data
page = requests.get(url)

# gets html content of page in parsable format
soup = BeautifulSoup(page.content, 'html.parser')


# find the recipe title
# TODO: remove leading and trailing whitespace
title = soup.find(class_="recipe-title").get_text()
#print(title)


# find recipe steps
recipe_steps = soup.find(class_="recipe-steps")

# parses recipe steps to get just the text from list items and puts the instructions in a list
steps = [item.get_text()  for item in recipe_steps.find_all('li')]

# for step in steps:
#     print(step)


# find list items for ingredients list
ingredients_list = soup.find('ul', class_="recipe-ingredients").find_all('li')
print(ingredients_list)

