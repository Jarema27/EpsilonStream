from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from .models import Comment
from .models import Utwor


def post_list(request):
	utwors = Utwor.objects.all()
	return render(request, 'Comment/post_list.html', {'utwors':utwors})

def logowanie(request):
	return render(request, 'Comment/logowanie.html', {})
# Create your views here.

def search_songs(request):
	find_string = request.GET.get('q', '')
	utwors = Utwor.objects.filter(Q(author__contains=find_string) | Q(title__contains=find_string))
	return render(request, 'Comment/songs.html', {'utwors':utwors})
