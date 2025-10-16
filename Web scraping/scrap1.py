# # # # from bs4 import BeautifulSoup
# # # # import requests

# # # # url = "https://www.swedbank.se"
# # # # req = requests.get(url)

# # # # soup = BeautifulSoup(req.content, "lxml")
# # # # for link in soup.find_all("a"):


# # # #     print(link.get("href"))

# # # # from bs4 import BeautifulSoup
# # # # import requests

# # # # url = "https://github.com/Stremio/stremio-web"
# # # # ask = requests.get(url)
# # # # soup = BeautifulSoup(ask.content, 'html.parser')
# # # # for link in soup.find_all("a"):
# # # #     print(link.get("href"))

# # # # from bs4 import BeautifulSoup
# # # # import requests


# # # # with open("index.html") as fp:
# # # #     soup = BeautifulSoup(fp, "html.parser")

# # # # print(soup)

# # # from bs4 import BeautifulSoup
# # # import requests

# # # html = '''
# # # <html>
# # #    <head>
# # #       <title>Hello World</title>
# # #    </head>
# # #    <body>
# # #       <h1 style="text-align:center;">Hello World</h1>
# # #    </body>
# # # </html>
# # # '''
# # # soup = BeautifulSoup(html, "html.parser")

# # # print(soup)
# # # #--------------------------------------

# # # # from bs4 import BeautifulSoup

# # # # html = '''
# # # # <html>
# # # #    <head>
# # # #       <title>Hello World</title>
# # # #    </head>
# # # #    <body>
# # # #       <h1 style="text-align:center;">Hello World</h1>
# # # #    </body>
# # # # </html>
# # # # '''
# # # # soup = BeautifulSoup(html, 'html.parser')

# # # # print(soup)

# # from bs4 import BeautifulSoup

# # soup = BeautifulSoup('<b class="boldest">TutorialsPoint</b>', 'lxml')

# # tag = soup.html 

# # print(type(tag))

# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<b class="boldest">TutorialsPoint</b>', 'lxml')

# tag = soup.html 

# print(tag.name)

# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<b class="boldest">TutorialsPoint</b>', 'lxml')

# tag = soup.html 
# tag.name = "trong"

# print(tag)
# from bs4 import BeautifulSoup

# with open(home.html)
# content = "html_file".read()

# print(content)

#----------------------------

# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<b class="boldest">TutorialsPoint</b>', "lxml")

# tag = soup.html 

# print(tag.name)

# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<b class="boldest">TutorialsPoint</b>', "lxml")

# tag = soup.html 
# tag.name= "strong"
# print(tag)
#----------------------------

# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<input type="text" name="name" value="Raju">', "lxml")

# tag = soup.input

# print(tag.attrs)

#--------------------------------

# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<input type="text" name="name" value="Raju">', "lxml")

# tag = soup.input
# print(tag.attrs)
# tag["valu"] = "Ravi"
# print(soup)

#---------------------------------

# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<input type="text" name="name" value="Raju">', "lxml")

# tag = soup.input

# tag["id"]= "nm"
# del tag["value"]
# print(soup)

#----------------------------------

# from bs4 import BeautifulSoup

# css_soup = BeautifulSoup('<p class="body"></p>', "lxml")

# print("css_soup.p[class]:", css_soup.p["class"])

# css_soup = BeautifulSoup('<p class="body bold"></p>', 'lxml')

# print("css_soup.p[class]", css_soup.p["class"])

#--------------------------------

# import requests

# url = "https://www.amazon.se"
# response = requests.get(url)

# print(response.status_code)
# print(response.text[500])

#----------------------------------
# from bs4 import BeautifulSoup
# import requests

# page = 1
# while True:
#     url = f"https://quotes.toscrape.com/page/{page}/"
#     response = requests.get(url)
#     if "Not quotes found" in response.text:
#         break
        
#         soup = BeautifulSoup(response.text, lxml)
#         quotes = [q.text for q in soup.find_all("span", class_="text")]
#         print(f"Page {page}: {len(quotes)} quotes")
#         page += 1

#----------------------------------------
# from bs4 import BeautifulSoup
# import requests
# page = 1
# while True:
#     url = f"https://quotes.toscrape.com/page/{page}/"
#     response = requests.get(url)
#     if "No quotes found!" in response.text:
#         break
#     soup = BeautifulSoup(response.text, 'lxml')
#     quotes = [q.text for q in soup.find_all("span", class_="text")]
#     print(f"Page {page}: {len(quotes)} quotes")
#     page += 1

#----------------------------------------------------------

# from bs4 import BeautifulSoup

# css_soup = BeautifulSoup('<p class="body "></p>', 'lxml')
# print("css_soup.p[class]:", css_soup.p["class"])

# css_soup = BeautifulSoup('<p class="body bold"></p>', 'lxml')

# print("css_soup.p[class]:", css_soup.p["class"])

#----------------------------------------------

from bs4 import BeautifulSoup

id_soup = BeautifulSoup('<p id="body bold"></p>', 'lxml')

print("id_soup.p[id]:", id_soup.p["id"])

print("type(id_soup.p[id])", type(id_soup.p["id"]))