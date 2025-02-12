from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='content_images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.5)
    author = models.CharField(max_length=100, default='Anonymous')

    class Meta:
        abstract = True

class MeditationTrack(BaseContent):
    audio_file = models.FileField(upload_to='meditation_tracks/')
    duration = models.IntegerField(help_text='Duration in minutes')

    def __str__(self):
        return self.title

class TopContent(BaseContent):
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Course(BaseContent):
    duration_weeks = models.IntegerField(help_text='Duration in weeks')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.title

class Workshop(BaseContent):
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max_participants = models.IntegerField(default=20)
    
    def __str__(self):
        return self.title

class Group(BaseContent):
    members_count = models.IntegerField(default=0)
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Event(BaseContent):
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    is_online = models.BooleanField(default=False)
    max_participants = models.IntegerField(default=100)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other')),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(_('First Name'), max_length=100, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=100, blank=True)
    birth_year = models.IntegerField(_('Birth Year'), null=True, blank=True)
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.user.username
