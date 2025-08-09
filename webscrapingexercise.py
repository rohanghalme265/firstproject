#Task(1): Import any libraries you think you'll need to scrap a website

import requests
import bs4




#Task(2): Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HTML text from the homepage

res = requests.get('http://quotes.toscrape.com')
print(res.text)



#Task(3): Get the names of all the authors on the first page

soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup.select('.author'))

authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)

#Task(4): Create a list of all the quotes on the first page
quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)
print(quotes)

#Task(5): Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right
#from the home page(e.g Love,inspirational,life,etc...).HINT:Keep in mind there are also tags underneath each quote,try to find
#a class only present in the top right tags,perhaps check the span

print(soup.select('.tag-item'))
print(len(soup.select('.tag-item')))

for item in soup.select('.tag-item'):
    print(item.text)



#Task(6): Notice how there is smore than one page,and subsequent pages look like this http://quotes.toscrape.com/page/2/.
#Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors
# on the website.keep in mind there are many ways to achive this,also note that you will need to somehow figure out how
# to check that your loop is on the page with quotes.For debugging purposes,I will let you know that there are only 10
# pages is http://quotes.toscrape.com/page/10/,but try to create a loop that is robust enough that it wouldn't matter to
#know the amount of pages beforehand,perhaps use try/except for this,its up to you!

url = 'http://quotes.toscrape.com/page/'

authors = set()
for page in range(1,10):

    page_url = url+str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text,"lxml")

    for name in soup.select(".author"):
        authors.add(name.text)

print(authors)












































































































































































































