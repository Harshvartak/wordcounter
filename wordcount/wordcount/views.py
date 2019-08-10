from django.http import HttpResponse
from django.shortcuts import render
import operator
import re

def home(request):
	return render(request,'home.html')

def count(request):
	fulltext=request.GET['fulltext']
	wordlist=fulltext.split()		

	wordcounter={}

	wordlist2=[re.sub(r'[^A-Za-z0-9]+', '', word) for word in wordlist]


	for word in wordlist2:
		if word in wordcounter:
			#Increase the counter for word
			wordcounter[word]+=1
		else:
			wordcounter[word]=1

	wordcounter2=sorted(wordcounter.items(), key=operator.itemgetter(1), reverse=True)		
			

	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist2),'wordcounter':wordcounter2})

def about(request):
	return render(request,'about.html')		