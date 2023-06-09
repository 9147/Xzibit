from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from home.models import News
from .forms import NewsForm
from .ml_models import check_news
from . import webScraper

# Create your views here.

def index(request):
    context = {
        'variable': "This is variable"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")

def data(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        
        news = NewsForm(request.POST)
        # print(form)
        
        # check whether it's valid:
        if news.is_valid():
        #     # process the data in form.cleaned_data as required
            news_content = news.cleaned_data['newsContent']
            news_url = news.cleaned_data['sourceURL']
            # print("news : ", news_content, "\nsourceURL : ", news_url)
            # print(news_url)
            # if not news_url:
            #     news_url ="https://news.google.com/"
            #
            # webContent = webScraper.process_news_object(news_url, news_content)
            a = check_news(news_url, news_content)
            accuracy = "false"
            if a>=50:
                accuracy = "true"
            return render(request,"data.html",{"sourceURL":news_url,"newsContent": news_content, "score": a, "accuracy": accuracy})
            # return render(request, "data.html", {"sourceURL":news_url,"newsContent": news_content, "webContent": webContent})
        #     # ...
        #     # redirect to a new URL:
        #     return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        news = NewsForm()
    
    
    return render(request, "data.html", {"news": news})
    

def about(request):
    return render(request, 'about.html')
