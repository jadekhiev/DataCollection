# News API
# This script pulls data from various news sources
# Written by Jesse & Jade


#import newsapi
import requests     

def NewsFromBBC():

    #j = 1   
    # BBC news api

   # for j in range(6):
    main_url = " https://newsapi.org/v2/everything?sources=bbc-news&pageSize=100&page=2&apiKey=abd1cde781dc46b385045b20e214a7e8"
    #main_url = "https://newsapi.org/v2/everything?country=ca&pageSize=100&page=1&apiKey=abd1cde781dc46b385045b20e214a7e8"
    
    
    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will contain all trending news
    titles = []
    description = []
    url = []
    
    for ar in article:
        titles.append(ar["title"])
        description.append(ar["description"])
        url.append(ar["url"])        
         
    for i in range(len(titles)):
        # printing all trending news
        print(i + 1, "|", titles[i], "|", description[i], "|",url[i] )                 
       # print(i + 1, description[i])       

# Driver Code
if __name__ == '__main__': 
    # function call
    NewsFromBBC() 

