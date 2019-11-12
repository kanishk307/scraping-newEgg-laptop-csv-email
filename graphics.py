from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


myurl="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#Grabs each product
containers = page_soup.findAll("div",{"class","item-branding"})
# print(containers[0])

# titlecontainers = page_soup.findAll("a",{"class","item-title"})

# pricewas = page_soup.findAll("li",{"class","price-was"})
# print(pricewas[3].span.text)

# pricecurrent = page_soup.findAll("li",{"class","price-current"})
# # print(pricecurrent[3].strong.text)
# print(namecontainers[0].text)

# innercontainer = containers[0].findAll("div",{"class","item-branding"})
# print(innercontainer[0].a.img["title"])


filename = "graphicscard.csv"
f = open(filename,"w")
headers = "product_name, currentprice \n"
f.write(headers)

count = 0;
for container in containers:
	count += 1
# for container in containers:
# 	brand = container.a.img["title"]
# 	print(brand)

for i in range(0,count):
	titlecontainer = page_soup.findAll("a",{"class","item-title"})
	product_name = titlecontainer[i].text
	print(product_name)

	pricecurrent = page_soup.findAll("li",{"class","price-current"})
	pricecurrent_item = pricecurrent[i].strong.text
	print(pricecurrent_item)

	f.write(product_name.replace(",","|") + "," + pricecurrent_item.replace(",",".") + "\n")
	# f.write(brand+"\n")


# for titlecontainer in titlecontainers:
	# titlecontainer = page_soup.findAll("a",{"class","item-title"})
	# title = titlecontainer.text
	# print(title)
	# f.write(title + "\t" + "\n")
# for container in containers:
# 	container.findAll("div",{"class","item-branding"})
# 	for innercontainer in container:
# 		print(innercontainer)

# for pricewas_item in pricewas:
# 	wasprice = pricewas_item.span
# 	print(wasprice)

# for pricecurrent_item in pricecurrent:
# 	currentprice = pricecurrent_item.strong.text
# 	print(currentprice + "\n")
# 	f.write(currentprice + "\n")

# f.close()