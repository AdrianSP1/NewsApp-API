from django.shortcuts import render
import requests
# Create your views here.
API_KEY = ''

def home(request):
    country= request.GET.get('country')
    category= request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={API_KEY}'
        response =requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&category=business&apiKey={API_KEY}'
        response =requests.get(url)
        data = response.json()
        articles = data['articles']
        






    context={
        'articles':articles
    }

    return render(request, 'news_api/home.html', context)
