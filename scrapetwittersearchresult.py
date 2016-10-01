#
# Instalar bibliotecas 
#   pip install lxml
#   pip install requests
#
# Tutorial sobre scraping com Python
#   http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests

# Mais sobre a lib 'requests' em:
# http://docs.python-requests.org/en/master/
page = requests.get('https://twitter.com/hashtag/vemprarua')

# Mais sobre a lib 'lxml' em:
# http://lxml.de/index.html#documentation
tree = html.fromstring(page.content) # tree = head + body

# Mais sobre xpath em:
# http://www.w3schools.com/xsl/xpath_intro.asp
xpath = '//*[@id="page-container"]/div[1]/h1'

headers = tree.xpath(xpath)

for header in headers:
	print("Atributos=%s Texto=[%s]" % (header.attrib.items(), header.text))
