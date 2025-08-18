#WEB SCRAPING:- Web  Scraping is general term for techniques involving automating the gathering of data from a website

'''
#*main things we need to understand:-
    1].Rules of web Scraping
    2].Limitation odf web Scraping
    3].Basic HTML and CSS
'''

'''
#*RULES OF WEB SCRAPING:-
      i].Always try t get permissionn before Scraping!
      ii].If you make too many scraping attempts or requests your IP Address could get blocked!
      iii].Some sites automatically block scraping software.
      
'''

'''
#*LIMITATIONN  OF WEB SCRAPING
       i].In general every website is unique,which means every web scraping script is unique.
       ii].A slight change or update to a website may completely break your web scraping script.
       
'''

'''
*HTML is used nto create the basic structure and content of a webpage
*CSS is used for the design and style of a web page,where elements sre placed and how it looks
*JavaScript is used to define the interactive elements of webpage
'''

'''
*HTML is Hypertext Markup Language and is present on every website on the internet
*You can right-click on a website and select "Veiw Page Source" to get an example
*HTML contains the information


<!DOCTYPE html>      #this heading is telling is that this is a html document
<html>     ----->this is a starting tag 
    <head>   #this head body contains certain high level information of webpage
     <title>Title on Browser Tab</title>
    </head>
    <body>
        <h1> Website Header </h1>
        <p> Some Paragraph </p>
    <body>
</html>   -------> this ia a closing tag
'''

'''
*CSS stands for Cascading Style Sheets.
*CSS gives a "style" to a website,such as changing colours and fonts.
*CSS uses tags to define what html elements will be styled.
*CSS contains the styling

<!DOCTYPE html>      #this heading is telling is that this is a html document
<html>     ----->this is a starting tag 
    <head>   #this head body contains certain high level information of webpage
     <link rel="stylesheet" href="styles.css">
     <title>Some Title</title>
    </head>
    <body>
        <p id='para2'> Some Text </p>
    <body>
</html>

'''
# import requests

# result = requests.get("http://www.example.com")
# print(type(result))
# print(result.text)
#
# import requests
# import bs4

# soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)

'''
#Beatiful soup:- it is a  python package for parsing HTML and XML documents
'''

# import  requests
# result = requests.get("http://ww.example.com")
# print(type(result))


import requests
# result = requests.get("http://www.example.com")
# print(type(result))
# print(result.text)
#
import bs4
# soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)
# print(soup.select('title')[0].getText())
# site_paragraphs = soup.select("p")
# print(site_paragraphs[0].getText())


#Grabbing a class:-
'''
Syntax                                                             Match Results

soup.select('div)                                           All elements with 'div' tag
soup.select('#some_id')                                   Elements containinng id='some_id'
soup.select('.some_class')                                Elements containing id='some_id'
soup.select(''div span')                              Any elements named span within a div element.
soup.select('div>span')                        Any elements named span directly within a div element with nothing in between.
    
'''

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,"lxml")
# print(soup)

# print(type(soup.select('.vector-toc-numb')))      #<class 'bs4.element.ResultSet'>
# print(soup.select('.vector-toc-numb'))
# print(soup.select('.vector-toc-numb')[0])
# for span in soup.find_all('span'):    # This prints all <spam> tags - even those without a class
#     print(span)
#
#
# for span in soup.find_all('span')[3]:    #If you looking for text
#     print(span)
#
# print(soup.select('span')[3]) #information with tags
# first_item = soup.select('span')[0]
# print(first_item)


'''
*Beautiful Soup can scan a page, locate the <img> tags and grab these URLs.
*then we can download the URLs as images and write them to the computer
'''

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,'lxml')

print(soup.select('img'))
print(soup.select('img')[0])
print(soup.select('.mw-default-size'))

computer = soup.select('.mw-default-size')[0]
print(type(computer))
print(computer)
print(computer['class'])
# print(computer['src'])

# from PIL import Image
# import requests
# from io import BytesIO
#
# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/250px-Deep_Blue.jpg"
# response = requests.get(url)
# img = Image.open(BytesIO(response.content))
# print(img.show())

#WORKING WITH MULTIPLE PAGES AND ITEMS:-

#GOAL: Get title of every book with a 2 star rating

import requests
import bs4
print('http://books.toscrape.com/catalogue/page-2.html')
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
page_num = 12
print(base_url.format(page_num))
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup)
print(soup.select(".product_pod"))
print(len(soup.select(".product_pod")))

products = soup.select(".product_pod")
example = products[0]
# print(example)
print(str(example))
print('star-rating Two' in str(example))
print('star-rating Three' in str(example))
# print(example)
print(example.select(".star-rating.Three"))
print(example.select(".star-rating.two"))
# [] == example.select(".star-rating.Two")

print(example)
print(example.select('a'))
print(example.select('a')[0])
print(example.select('a')[1])
print(example.select('a')[1]['title'])

# We can check if something is 2 stars (string call in, example.select(rating))
# example.select('a')[1]['title'] to grab the book title

two_star_titles = []

for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")

    for book in books:

        if len(book.select('.star-rating.Two')) !=0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)































































































































































































