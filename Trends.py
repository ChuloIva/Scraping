from pytrends.request import TrendReq

# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['pizza', 'bagel'])

# # Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.head())

# Interest by Region
interest_by_region_df = pytrend.interest_by_region()
print(interest_by_region_df.head())

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(related_queries_dict)

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()
print(trending_searches_df.head())

# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
print(today_searches_df.head())

# Get Google Top Charts
top_charts_df = pytrend.top_charts(2018, hl='en-US', tz=300, geo='GLOBAL')
print(top_charts_df.head())

# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='pizza')
print(suggestions_dict)

# Get Google Realtime Search Trends

realtime_searches = pytrend.realtime_trending_searches(pn='IN')
print(realtime_searches.head())

#plot the data 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt


df2 = interest_over_time_df

# df = pd.to_datetime(df2['date'])

# df2.info()
# sns.set_style('darkgrid')
# plt.figure(figsize=(10,5)) 
# sns.lineplot(df2.index, df2["pizza"], alpha=0.8,  palette="Blues_d")
# plt.title('Pizza search')
# plt.ylabel('Search percentage', fontsize=12)
# plt.xlabel('Date', fontsize=12)
# plt.show()

#plotted stuff bar plot wohooo                   