from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext=request.GET['fulltext']#fulltext es el nombre del text area.
    wordlist=fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:

            worddictionary[word]+=1

        else:
            worddictionary[word]=1

    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True) # items() retorna pares(key,value) del dict. itemgetter(1) esto te dice
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':worddictionary.items()})
