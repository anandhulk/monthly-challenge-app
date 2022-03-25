from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    'december':'drink the last bottle of bear'
}
def index(request):
    month_list=""
    months=list(c_dict.keys())

    for month in months:
        month_list+=f"<li><a href='{month}'>{month.capitalize()}</a></li>"
    
    reponse=f"<ul>{month_list}</ul>"
    return HttpResponse(reponse)


def m_challenges(request,month):
    try:
        m=c_dict[month]
        response_data=f"<h1>{m}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("month not supported")   

def m_int(request,month):
    try:
        m=list(c_dict.keys())
        n=m[month-1]
        return HttpResponseRedirect(n)
    except:
        return HttpResponseNotFound("month not supported")
    