"""
URL configuration for letsmeet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from testapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name='home'),  # Home page
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    path('signup/', views.signup_view, name='signup'),  # Sign up page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('create/', views.create_events_view, name='create_event'),  # Create event page
    path('myevents/', views.my_events_view, name='my_events'),  # My events page
    path('events/', views.events_view, name='events'),  # Events list page
    # path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),  # Register for event
    path('unregister/<int:event_id>/', views.unregister_from_event, name='unregister_from_event'),
    path('events/<str:date_str>/', views.events_by_date_view, name='events_by_date'),
    path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),
  # path('export-registrations/<int:event_id>/', views.export_registrations_to_excel, name='export_registrations'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



