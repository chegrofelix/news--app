from flask import render_template
from app import app
from newsapi import NewsApiClient




@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="c7414509761344ce8321cc7ae296ade4")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")

    articles = topheadlines['articles']
    
    
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)



    return render_template('index.html', context= mylist)


@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="c7414509761344ce8321cc7ae296ade4")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
    mylist = zip(news, desc, img)
 
    return render_template('bbc.html', context=mylist)

@app.route('/buzzfeed')
def buzzfeed():
    newsapi = NewsApiClient(api_key="c7414509761344ce8321cc7ae296ade4")
    topheadlines = newsapi.get_top_headlines(sources="Buzzfeed")
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
    mylist = zip(news, desc, img)
 
    return render_template('buzzfeed.html', context=mylist)

@app.route('/aljazeera')
def aljazeera():
    newsapi = NewsApiClient(api_key="c7414509761344ce8321cc7ae296ade4")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
    mylist = zip(news, desc, img)
 
    return render_template('aljazeera.html', context=mylist)