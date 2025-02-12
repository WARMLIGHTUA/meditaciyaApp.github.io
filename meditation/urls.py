from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'meditation'

urlpatterns = [
    path('', views.MeditationListView.as_view(), name='home'),
    
    # Meditation Tracks
    path('tracks/', views.MeditationListView.as_view(template_name='meditation/track_list.html'), name='track_list'),
    path('track/<int:pk>/', views.MeditationDetailView.as_view(), name='track_detail'),
    path('track/create/', views.MeditationTrackCreate.as_view(), name='track_create'),
    path('track/<int:pk>/edit/', views.MeditationTrackUpdate.as_view(), name='track_edit'),
    
    # Top Content
    path('top/', views.TopContentListView.as_view(), name='top_list'),
    path('top/<int:pk>/', views.TopContentDetailView.as_view(), name='top_detail'),
    
    # Courses
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', views.CourseCreate.as_view(), name='course_create'),
    path('courses/<int:pk>/edit/', views.CourseUpdate.as_view(), name='course_edit'),
    
    # Workshops
    path('workshops/', views.WorkshopListView.as_view(), name='workshop_list'),
    path('workshops/<int:pk>/', views.WorkshopDetailView.as_view(), name='workshop_detail'),
    path('workshops/create/', views.WorkshopCreate.as_view(), name='workshop_create'),
    path('workshops/<int:pk>/edit/', views.WorkshopUpdate.as_view(), name='workshop_edit'),
    
    # Groups
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('groups/create/', views.GroupCreate.as_view(), name='group_create'),
    path('groups/<int:pk>/edit/', views.GroupUpdate.as_view(), name='group_edit'),
    
    # Events
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('events/create/', views.EventCreate.as_view(), name='event_create'),
    path('events/<int:pk>/edit/', views.EventUpdate.as_view(), name='event_edit'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='meditation:home'), name='logout'),
] 