# from requests import HTMLSession 

#import what we need
from requests_html import HTMLSession
session = HTMLSession()


# USE THIS TO AVOID THE COOKIE CONSENT MESSAGE

# 'https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB%3Aen',
# params={
# 'custom_google': 'true',
# 'premium_proxy': 'true',
# 'country_code':'gb',
# 'wait': '1500' # Waiting for the content to load (1.5 seconds)
# },
# cookies= {'CONSENT': 'YES+'})




#use session to get the page
r = session.get('https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en', params={
'custom_google': 'true',
'premium_proxy': 'true',
'country_code':'gb',
'wait': '1500' # Waiting for the content to load (1.5 seconds)
},
cookies= {'CONSENT': 'YES+'})

#render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
r.html.render(sleep=1, scrolldown=2)

#find all the articles by using inspect element and create blank list
articles = r.html.find('article')
newslist = []

#loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        title = newsitem.text
        link = newsitem.absolute_links
        newsarticle = {
            'title': title,
            'link': link 
        }
        newslist.append(newsarticle)
    except:
       pass

#print the length of the list
print(len(newslist))

print(r.html)