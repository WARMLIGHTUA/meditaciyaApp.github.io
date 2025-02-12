from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import MeditationTrack, TopContent, Course, Workshop, Group, Event
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm

# Create your views here.

class MeditationListView(ListView):
    model = MeditationTrack
    template_name = 'meditation/meditation_list.html'
    context_object_name = 'tracks'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_content'] = TopContent.objects.filter(featured=True)
        context['courses'] = Course.objects.all()[:5]
        context['workshops'] = Workshop.objects.all()[:5]
        context['groups'] = Group.objects.all()[:5]
        context['events'] = Event.objects.all()[:5]
        return context

class MeditationDetailView(DetailView):
    model = MeditationTrack
    template_name = 'meditation/meditation_detail.html'

class TopContentListView(ListView):
    model = TopContent
    template_name = 'meditation/top_content_list.html'
    context_object_name = 'content'
    ordering = ['-created_at']

class TopContentDetailView(DetailView):
    model = TopContent
    template_name = 'meditation/top_content_detail.html'

class CourseListView(ListView):
    model = Course
    template_name = 'meditation/course_list.html'
    context_object_name = 'courses'
    ordering = ['-created_at']

class CourseDetailView(DetailView):
    model = Course
    template_name = 'meditation/course_detail.html'

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'meditation/workshop_list.html'
    context_object_name = 'workshops'
    ordering = ['date']

class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'meditation/workshop_detail.html'

class GroupListView(ListView):
    model = Group
    template_name = 'meditation/group_list.html'
    context_object_name = 'groups'
    ordering = ['-created_at']

class GroupDetailView(DetailView):
    model = Group
    template_name = 'meditation/group_detail.html'

class EventListView(ListView):
    model = Event
    template_name = 'meditation/event_list.html'
    context_object_name = 'events'
    ordering = ['date']

class EventDetailView(DetailView):
    model = Event
    template_name = 'meditation/event_detail.html'

@method_decorator(login_required, name='dispatch')
class MeditationTrackCreate(CreateView):
    model = MeditationTrack
    template_name = 'meditation/meditation_form.html'
    fields = ['title', 'description', 'duration', 'image', 'audio_file', 'author']
    success_url = reverse_lazy('meditation:track_list')

@method_decorator(login_required, name='dispatch')
class MeditationTrackUpdate(UpdateView):
    model = MeditationTrack
    template_name = 'meditation/meditation_form.html'
    fields = ['title', 'description', 'duration', 'image', 'audio_file', 'author']
    success_url = reverse_lazy('meditation:track_list')

@method_decorator(login_required, name='dispatch')
class CourseCreate(CreateView):
    model = Course
    template_name = 'meditation/course_form.html'
    fields = ['title', 'description', 'duration_weeks', 'price', 'image', 'video_url', 'author']
    success_url = reverse_lazy('meditation:course_list')

@method_decorator(login_required, name='dispatch')
class CourseUpdate(UpdateView):
    model = Course
    template_name = 'meditation/course_form.html'
    fields = ['title', 'description', 'duration_weeks', 'price', 'image', 'video_url', 'author']
    success_url = reverse_lazy('meditation:course_list')

@method_decorator(login_required, name='dispatch')
class WorkshopCreate(CreateView):
    model = Workshop
    template_name = 'meditation/workshop_form.html'
    fields = ['title', 'description', 'date', 'location', 'price', 'max_participants', 'image', 'video_url', 'author']
    success_url = reverse_lazy('meditation:workshop_list')

@method_decorator(login_required, name='dispatch')
class WorkshopUpdate(UpdateView):
    model = Workshop
    template_name = 'meditation/workshop_form.html'
    fields = ['title', 'description', 'date', 'location', 'price', 'max_participants', 'image', 'video_url', 'author']
    success_url = reverse_lazy('meditation:workshop_list')

@method_decorator(login_required, name='dispatch')
class GroupCreate(CreateView):
    model = Group
    template_name = 'meditation/group_form.html'
    fields = ['title', 'description', 'is_private', 'image', 'author']
    success_url = reverse_lazy('meditation:group_list')

@method_decorator(login_required, name='dispatch')
class GroupUpdate(UpdateView):
    model = Group
    template_name = 'meditation/group_form.html'
    fields = ['title', 'description', 'is_private', 'image', 'author']
    success_url = reverse_lazy('meditation:group_list')

@method_decorator(login_required, name='dispatch')
class EventCreate(CreateView):
    model = Event
    template_name = 'meditation/event_form.html'
    fields = ['title', 'description', 'date', 'location', 'is_online', 'max_participants', 'image', 'author']
    success_url = reverse_lazy('meditation:event_list')

@method_decorator(login_required, name='dispatch')
class EventUpdate(UpdateView):
    model = Event
    template_name = 'meditation/event_form.html'
    fields = ['title', 'description', 'date', 'location', 'is_online', 'max_participants', 'image', 'author']
    success_url = reverse_lazy('meditation:event_list')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, _('Successfully logged in!'))
                return redirect('meditation:home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'meditation/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            login(request, user)
            messages.success(request, _('Registration successful!'))
            return redirect('meditation:home')
    else:
        user_form = CustomUserCreationForm()
        profile_form = UserProfileForm()
    
    return render(request, 'meditation/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
