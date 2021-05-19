from django.shortcuts import render
from django.http import HttpResponse
from .a2 import get_cands

# Create your views here.

def index(request):
    context={"deneme":27}
    return render(request,'index.html',context)

def the_func(request):

    ed1 = request.POST.get("ed1")
    exp1 = request.POST.get("exp1")
    pn1 = request.POST.get("pn1")
    pn1 = int(pn1)
    excomp1 = request.POST.get("excomp1")
    skill1 = request.POST.get("skill1")
    lang1 = request.POST.get("lang1")
    loc1 = request.POST.get("loc1")

    the_df = get_cands(ed1, exp1, excomp1, skill1, skill1, lang1, loc1, pn1)

    return HttpResponse(the_df.to_html())