from django.shortcuts import render
import requests
# Create your views here.
API_KEY = '89253bef34204bfa83812b218dc4553e'

def home(request):
    url = f'https://newsapi.org/v2/everything?q=tesla&from=2021-09-05&sortBy=publishedAt&apiKey={API_KEY}'
    response =requests.get(url)
    data = response.json()
    
    articles = data['articles']

    context={
        'articles':articles
    }

    return render(request, 'news_api/home.html', context)