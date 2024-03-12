from django.db import models
from django.contrib.auth.models import User
from eventsourcing.application import Application
from eventsourcing.domain import Aggregate, event
from uuid import uuid5, NAMESPACE_URL
from django.db import models
    
class VideoUploadedEvent(models.Model):
    url = models.URLField(null=True)
    title = models.CharField(max_length=255)
    category = models.TextField()

class PhotoUploadedEvent(models.Model):
    url = models.URLField(null=True)
    title = models.CharField(max_length=255)
    category = models.TextField()

class ArticleUploadedEvent(models.Model):
    url = models.URLField(null=True)
    title = models.CharField(max_length=255)
    category = models.TextField()


class upload(Aggregate):
    @event('Upload')
    def __init__(self, profileId):
        self.profileId=profileId
        self.recent = []

    @event('VideoAdded')
    def upload_video(self, url, title, category):
        Video = VideoUploadedEvent(url=url,title=title, category=category)
        Video.save()
        self.recent.append(Video)

    @event('PhotoAdded')
    def upload_photo(self, url, title, category):
        Photo = PhotoUploadedEvent(url=url,title=title,category=category)
        Photo.save()
        self.recent.append(Photo)
    
    @event('ArticleAdded')
    def upload_article(self, url, title, category):
        Article = ArticleUploadedEvent(url=url,title=title,category=category)
        Article.save()
        self.recent.append(Article)

    @staticmethod
    def create_id(profileId):
        return uuid5(NAMESPACE_URL, f'/upload/{profileId}')
    
class recentQuery(Application):
    def register_upload(self, profileId):
        Upload = upload(profileId)
        self.save(Upload)

    def add_video(self, url, profileId, title, category):
        Upload = self.repository.get(upload.create_id(profileId))
        Upload.upload_video(url, title, category)
        self.save(Upload)
    
    def add_photo(self, url, profileId, title, category):
        Upload = self.repository.get(upload.create_id(profileId))
        Upload.upload_photo(url, title, category)
        self.save(Upload)

    def add_article(self, url, profileId, title, category):
        Upload = self.repository.get(upload.create_id(profileId))
        Upload.upload_article(url, title, category)
        self.save(Upload)

    def get_events(self, profileId):
        Upload = self.repository.get(upload.create_id(profileId))
        return Upload.recent

    
class Interest(models.Model):
    interests = models.CharField(max_length=100, unique=True)


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    
    interests = models.ManyToManyField(Interest, blank=True)
