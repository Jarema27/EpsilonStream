from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from .models import Comment
from .models import Utwor
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from Comment.forms import UserForm, UserProfileForm

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

 
def register(request):
    # Like before, get the request's context.
    #context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

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
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'Comment/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
            )