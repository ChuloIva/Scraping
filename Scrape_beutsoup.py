import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

my_url = 'https://personal.vanguard.com/us/FundsAllHoldings?FundId=0623&FundIntExt=INT&tableName=Equity&tableIndex=0&sort=SHARES&sortOrder=web.funds.profile.view.FundsAllHoldingsSort$SortOrder@9c2485f&APP=PE'

# opening url and grabbing the web page
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')



# grabbing all containers with class name = item-container
containers = page_soup.findAll('div', {'table, id="columnContainer" '})

df = pd.DataFrame(containers) #convert to dataframe 

print(df)

# filename = "products.csv"
# f = open(filename, 'w')

# headers = "brands, product_name, shipping\n"

# f.write(headers)

# container = containers[1]

# for container in containers:
#     brand = container.div.div.a.img['title']
#     title_container = container.findAll('a', {'class':'item-title'})
#     product_name = title_container[0].text
#     ship_container = container.findAll('li', {'class':'price-ship'})
#     # use strip() to remove blank spaces before and after text
#     shipping = ship_container[0].text.strip()

#     print("brand:" + brand)
#     print("product_name:" + product_name)
#     print("shipping:" + shipping)

#     f.write(brand + ',' + product_name.replace(',' , '|') + ',' + shipping + '\n')

# f.close()