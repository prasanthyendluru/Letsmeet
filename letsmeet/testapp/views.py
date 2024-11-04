from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from testapp.forms import create_event_form
from testapp.models import Event_model
# Create your views here.

def home_page_view(request):
    return render(request,'testapp/home.html')
@login_required
def create_events_view(request):
    form=create_event_form()
    if request.method=="POST":
        form=create_event_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'testapp/create_events.html',{'form':form})
@login_required
def my_events_view(request):
    registrations = EventRegistration.objects.filter(user=request.user)
    return render(request,'testapp/my_events.html', {'registrations': registrations})

@login_required
def events_view(request):
    events_list=Event_model.objects.all()
    return render(request,'testapp/events.html',{"events_list":events_list})
def signup_view(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request,'testapp/signup.html',{'form':form})
from django.contrib.auth import logout as auth_logout

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('/')
from django.shortcuts import render, redirect, get_object_or_404
from .models import EventRegistration


# @login_required
# def register_for_event(request, event_id):
#     event = get_object_or_404(Event_model, id=event_id)
#     # Check if the user is already registered for the event
#     if not EventRegistration.objects.filter(user=request.user, event=event).exists():
#         EventRegistration.objects.create(user=request.user, event=event)
#     return redirect('/myevents')
@login_required
def unregister_from_event(request, event_id):
    event_registration = get_object_or_404(EventRegistration, user=request.user, event_id=event_id)
    event_registration.delete()  # Remove the registration entry
    return redirect('/myevents')
import openpyxl
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from django.utils.dateparse import parse_date

def events_by_date_view(request, date_str):
    date = parse_date(date_str)
    if date is None:
        return JsonResponse({'error': 'Invalid date'}, status=400)

    events = Event_model.objects.filter(date=date)
    events_list = list(events.values('id', 'eventname', 'date', 'location', 'type_of_event', 'image'))
    return JsonResponse({'events': events_list})
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event_model, EventRegistration

@login_required
@require_POST
def register_for_event(request, event_id):
    event = get_object_or_404(Event_model, id=event_id)
    if not EventRegistration.objects.filter(user=request.user, event=event).exists():
        EventRegistration.objects.create(user=request.user, event=event)
        return JsonResponse({'message': 'Registered successfully!'})
    return JsonResponse({'message': 'Already registered.'}, status=400)
