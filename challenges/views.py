from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
# Create your views here.


c_dict={
    'january':'make new wishes',
    'february':'find a valentine',
    'march':'drink more water',
    'april':'dont get fooled',
    'may':'spcls classes on',
    'june':'legends are born',
    'july':'here comes hurricane',
    'august':'remeber the freedom fighters',
    'september':'onam comming',
    'october':'its 10th month',
    'november':'dont ever think of shaving',
    'december': None
}
def index(request):
    months=list(c_dict.keys())

    return render(request,"challenges/index.html",{
        "months":months
    })


def m_challenges(request,month):
    try:
        m=c_dict[month]
        #response_data=render_to_string("challenges/challenge.html") #f"<h1>{m}</h1>"
        #return HttpResponse(response_data)
        return render(request,"challenges/challenge.html",{
            "text":m,
            "text1":month
        })
    except:
        return HttpResponseNotFound("month not supported")   

def m_int(request,month):
    try:
        m=list(c_dict.keys())
        n=m[month-1]
        return HttpResponseRedirect(n)
    except:
        return HttpResponseNotFound("month not supported")
    