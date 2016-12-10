from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from .models import Comment
from .models import Utwor
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

def post_list(request):
	utwors = Utwor.objects.all()
	return render(request, 'Comment/post_list.html', {'utwors':utwors})

def logowanie(request):
	return render(request, 'Comment/logowanie.html', {})

def search_songs(request):
	find_string = request.GET.get('q', '')
	utwors = Utwor.objects.filter(Q(author__contains=find_string) | Q(title__contains=find_string))
	return render(request, 'Comment/post_list.html', {'utwors':utwors})

def registration(request):
    return render(request, 'Comment/registration.html')

def registration_complete(request):
    return render_to_response('Comment/registration_complete.html')

 
