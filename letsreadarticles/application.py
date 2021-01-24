from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key= 'c5c2fb7b62764cd39bd26444ce9c5d70')

@app.route('/')
def index():
    
    #/v2/top headlines = newsapi.get_top_headlines()
    topheadlines = newsapi.get_top_headlines(sources='bbc-news, the-verge, cnn, bloomberg, washingtonpost, buzzfeed')
    
    #create a variable called aricles to house each component such as the img, desc, title etc
    articles = topheadlines['articles']

    img=[]
    desc=[]
    news=[]
    url=[]

    for i in range(len(articles)):
        myarticles = articles[i]
        img.append(myarticles['urlToImage'])
        desc.append(myarticles['description'])
        news.append(myarticles['title'])
        url.append(myarticles['url'])

    mycontent = zip(img,desc,news,url)

    return render_template("layout.html", context=mycontent)

@app.route('/tech')
def tech():
    newsapi = NewsApiClient(api_key= 'c5c2fb7b62764cd39bd26444ce9c5d70')
    
    topheadlines = newsapi.get_top_headlines(sources="techcrunch, thenextweb, wired,the-verge, Gizmodo, digitaltrends")

    articles = topheadlines['articles']

    img=[]
    desc=[]
    news=[]
    url=[]

    for i in range(len(articles)):
        myarticles = articles[i]


        img.append(myarticles['urlToImage'])
        desc.append(myarticles['description'])
        news.append(myarticles['title'])
        url.append(myarticles['url'])
    
    mycontent = zip(img,desc,news,url)

    return render_template("tech.html", context = mycontent)

@app.route('/Me')
def Me():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
