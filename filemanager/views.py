from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from sys import path
import os,time

# Create your views here.
def index(request):
	files=os.listdir(os.getcwd())
	filesdict=dict()
	filesdict1=dict()
	for file in files:		
		filesdict1[file] = time.ctime(os.stat(file)[8])
	filesdict['files'] = filesdict1
	print filesdict
	return render(request, 'filemanager/index.html', filesdict)