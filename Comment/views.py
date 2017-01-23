from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from .models import Comment
from .models import Utwor
from .models import UtwordoListy
from .models import Lista
from .models import Gatunek
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from Comment.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect

def post_list(request):
   utwors = Utwor.objects.all()
   gatuneks = Gatunek.objects.all().exclude(utwor__isnull=True)
   return render(request, 'Comment/post_list.html', {'utwors':utwors,'gatuneks':gatuneks})

def logowanie(request):
	return render(request, 'Comment/logowanie.html', {})


def dodaj(request, pk):
    lists = Lista.objects.filter(Q(Klient=request.user))
    
    return render(request, 'Comment/dodaj.html', {'lists':lists, 'sid':pk})

def utwor(request):
    title = request.GET.get('title', 'k')
    utwors = Utwor.objects.all()
    return render(request, 'Comment/utwor.html', {'utwors':utwors,'tytul':title})

def utwor(request, pk):
    song = get_object_or_404(Utwor, pk=pk)
    song.IloscWyswietlen += 1
    song.save()

    songs = Utwor.objects.filter(Q(gatunek=song.gatunek) | Q(author__contains=song.author)).exclude(pk=song.pk)
    return render(request, 'Comment/utwor.html', {'utwor':song, 'utwory':songs})

def playList(request, pk, sid):
    lista = get_object_or_404(Lista, pk=pk)
    utwory = lista.songs.all()
    utwor = utwory[int(sid)]
    utworypozostale = utwory[int(sid)+1:]
    return render(request, 'Comment/playList.html', {'utwor':utwor, 'utwory':utworypozostale, 'lista':lista, 'sid':(int(sid)+1)})

def edit(request, pk):
    lista = get_object_or_404(Lista, pk=pk)
    utwory = lista.songs.all()
    return render(request, 'Comment/edit.html', {'utwory':utwory, 'lista':lista})

def listy(request):
    utwors = Utwor.objects.all()
    lists = Lista.objects.filter(Q(Klient = request.user))    
    polaczenie = UtwordoListy.objects.all()
    return render(request, 'Comment/listyOd.html', {'utwors':utwors,'lists':lists,'polaczenie':polaczenie})

def search_songs(request):
	find_string = request.GET.get('q', '')
	utwors = Utwor.objects.filter(Q(author__contains=find_string) | Q(title__contains=find_string))
	return render(request, 'Comment/post_list.html', {'utwors':utwors})

def nowa_lista_ba(request):
    find_string = request.GET.get('create', 'k')
    lis = Lista(NazwaL = find_string,Klient = request.user)
    lis.save()
    lists = Lista.objects.all()
    return redirect(listy)

def nowa_lista(request, sid):
    find_string = request.GET.get('create', 'k')
    lis = Lista(NazwaL = find_string, Klient = request.user)
    lis.save()
    lists = Lista.objects.all()
    return redirect(dodaj_do_listy, lis.pk, sid)

def dodaj_do_listy(request, lid, sid):
    utwo = get_object_or_404(Utwor, pk=sid)
    lista = get_object_or_404(Lista, pk=lid)
    if(not UtwordoListy.objects.filter(Q(IdUtwor=utwo.pk)& Q(IdLista=lista.pk))):
        dl = UtwordoListy()
        dl.IdUtwor = utwo
        dl.IdLista = lista
        dl.save()
        check = False
    else:
        check = True
        lists = Lista.objects.filter(Q(Klient = request.user))
        return render(request, 'Comment/dodaj.html',  {'lists':lists, 'sid':sid, 'check':check})
    lists = Lista.objects.all()
    return redirect(utwor, sid)

def remove(request):
    id = request.POST.get('rem', '')
    lista = get_object_or_404(Lista, pk=id)
    lista.delete()
    return redirect(listy)

def remove_song(request, pk):
    sid = request.POST.get('rem', '')
    pol = UtwordoListy.objects.get(Q(IdUtwor=sid) & Q(IdLista=pk))
    pol.delete()
    return redirect(edit, pk)

def registration(request):
    return render(request, 'Comment/registration.html')

def registration_complete(request):
    return render_to_response('Comment/registration_complete.html')

 
def register(request):
    # Like before, get the request's context.
    #context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False
    exist = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            exist = True

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'Comment/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'exist': exist}
            )
def user_login(request):
    # Like before, obtain the context for the user's request.
    

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)
        print(username)
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Eclipse account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('Comment/logowanie.html', {})

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')