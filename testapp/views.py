from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import LoginView
from django.utils.dateparse import parse_date
from .forms import SignUpForm, create_event_form
from .models import Event_model, EventRegistration
import openpyxl

# Home page view
def home_page_view(request):
    return render(request, 'testapp/home.html')

# Signup view
def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login/')
    return render(request, 'testapp/signup.html', {'form': form})



# Logout view
@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('/')

# Create event view
@login_required
def create_events_view(request):
    form = create_event_form()
    if request.method == "POST":
        print(request.FILES)  # Shows uploaded files
        form = create_event_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    return render(request, 'testapp/create_events.html', {'form': form})

# View for user's registered events
@login_required
def my_events_view(request):
    registrations = EventRegistration.objects.filter(user=request.user)
    return render(request, 'testapp/my_events.html', {'registrations': registrations})

# View for listing all events
@login_required
def events_view(request):
    events_list = Event_model.objects.all()
    return render(request, 'testapp/events.html', {"events_list": events_list})

# Event registration view
@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event_model, id=event_id)
    # Check if user is already registered for the event
    if not EventRegistration.objects.filter(user=request.user, event=event).exists():
        EventRegistration.objects.create(user=request.user, event=event)
    return redirect('/myevents')

# Event unregistration view
@login_required
def unregister_from_event(request, event_id):
    event_registration = get_object_or_404(EventRegistration, user=request.user, event_id=event_id)
    event_registration.delete()  # Remove the registration entry
    return redirect('/myevents')

# View for filtering events by date
def events_by_date_view(request, date_str):
    date = parse_date(date_str)
    if date is None:
        return JsonResponse({'error': 'Invalid date'}, status=400)
    
    events = Event_model.objects.filter(date=date)
    events_list = list(events.values('id', 'eventname', 'date', 'location', 'type_of_event', 'image'))
    return JsonResponse({'events': events_list})
