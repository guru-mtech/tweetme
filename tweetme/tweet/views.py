from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .models import Tweet
# to render HomePage
def home_page(request , *args , **kwargs):
    return render(request,"pages/index.html",context={},status=200)

def tweet_detial_view(request , tweet_id ,*args , **kwards):
    status = 200
    data = {
        "status" : status,
        "id" : tweet_id,
    }
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.contant
    except:
        data["message"] = "Notfound"
        status = 404
    return JsonResponse(data)   


def tweet_list(request,*args,**kwargs): 
    querySet = Tweet.objects.all()

    allTweets = [{"id" : item.id,"content" : item.contant} for item in querySet]

    data = {
        "responce" : allTweets,
        "status": 200,
    }

    return JsonResponse(data)