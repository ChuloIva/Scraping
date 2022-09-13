from pygooglenews import GoogleNews

# default GoogleNews instance

gn = GoogleNews(lang = 'en', country = 'UK')

#Get things by title

def get_titles(search):
    gn = GoogleNews(lang = 'en', country = 'UK')
    search= gn.search(search)
    newsitem= search['entries']
    for item in newsitem:
        print(item.title)
    return

# get_titles("Queen")

# Get things by link

def get_titles_links(search):
    stories = []
    gn = GoogleNews(lang = 'en', country = 'UK')
    search= gn.search(search)
    newsitem= search['entries']
    for item in newsitem:
        story = {
            'title': item.title,
            'link': item.link
        }
        stories.append(story)
    return print(stories)

# get_titles_links("Queen")



# Top news - entries separarted 
# 
# top = gn.top_news(proxies=None, scraping_bee = None)



# Top news - entries separarted 

def Top_news():
    gn = GoogleNews(lang = 'en', country = 'UK')
    search= gn.top_news()
    newsitem= search['entries']
    for item in newsitem:
        print(item.title)
    return

# print(top)

Top_news()

# Stories by Topic
# business = gn.topic_headlines('BUSINESS', proxies=None, scraping_bee = None)
# The returned object contains feed (FeedParserDict) and entries list of articles found with all data parsed.

# Accepted topics are:

# WORLD
# NATION
# BUSINESS
# TECHNOLOGY
# ENTERTAINMENT
# SCIENCE
# SPORTS
# HEALTH

# # gn = GoogleNews('uk', 'UA')
# kyiv = gn.geo_headlines('kyiv', proxies=None, scraping_bee = None)
# # or 
# kyiv = gn.geo_headlines('kiev', proxies=None, scraping_bee = None)
# # or
# kyiv = gn.geo_headlines('киев', proxies=None, scraping_bee = None)
# # or
# kyiv = gn.geo_headlines('Київ', proxies=None, scraping_bee = None)
# The returned object contains feed (FeedParserDict) and entries list of articles found with all data parsed.

# All of the above variations will return the same feed of the latest news about Kyiv, Ukraine:

# geo['feed'].title

# # 'Київ - Останні - Google Новини'
# It is language agnostic, however, it does not guarantee that the feed for any specific place will exist. For example, if you want to find the feed on LA or Los Angeles you can do it with GoogleNews('en', 'US').

# The main (en, US) Google News client will most likely find the feed about the most places.