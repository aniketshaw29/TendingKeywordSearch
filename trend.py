import pandas as pd
from pytrends.request import TrendReq

pytrend=TrendReq(hl='en-US',tz=360)
trendy_keywords='Data Science'   
kw_list=[trendy_keywords]
kw=trendy_keywords

pytrend.build_payload(kw_list)
#payload function builds the search payload and accept a list as an argument
#We can build the payload for interest overtime and by the region

pytrend.interest_over_time()
pytrend.interest_by_region()
#related quries will be returned as disctionary value

related_queries_dict=pytrend.related_queries()

related_queries_rising = related_queries_dict.get(kw).get('rising')
# for top related queries
related_queries_top = related_queries_dict.get(kw).get('top')
print("****** RISING RELATED KEYWORDS ******")
print(related_queries_rising)
print("****** TOP RELATED KEYWORDS *******")
print(related_queries_top)
