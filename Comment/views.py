from django.shortcuts import render
from django.utils import timezone
from .models import Comment
from .models import Utwor
	

def post_list(request):
	utwors = Utwor.objects.all()
	return render(request, 'Comment/post_list.html', {'utwors':utwors})
def logowanie(request):
	return render(request, 'Comment/logowanie.html', {})
# Create your views here.
