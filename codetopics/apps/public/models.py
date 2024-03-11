from eventsourcing.application import Application
from eventsourcing.domain import Aggregate, event
from uuid import uuid5, NAMESPACE_URL
from django.db import models
    
class VideoUploadedEvent(models.Model):
    title = models.CharField(max_length=255)
    category = models.TextField()

class PhotoUploadedEvent(models.Model):
    title = models.CharField(max_length=255)
    category = models.TextField()

class ArticleUploadedEvent(models.Model):
    title = models.CharField(max_length=255)
    category = models.TextField()


class upload(Aggregate):
    @event('Upload')
    def __init__(self, url):
        self.url=url
        self.recent = []

    @event('VideoAdded')
    def upload_video(self, title, category):
        Video = VideoUploadedEvent(title=title, category=category)
        Video.save()
        self.recent.append(Video)

    @event('PhotoAdded')
    def upload_photo(self, title, category):
        Photo = PhotoUploadedEvent(title=title,category=category)
        Photo.save()
        self.recent.append(Photo)
    
    @event('ArticleAdded')
    def upload_article(self, title, category):
        Article = ArticleUploadedEvent(title=title,category=category)
        Article.save()
        self.recent.append(Article)

    @staticmethod
    def create_id(url):
        return uuid5(NAMESPACE_URL, f'/upload/{url}')
    
class recentQuery(Application):
    def register_upload(self, url):
        Upload = upload(url)
        self.save(Upload)

    def add_video(self, url, title, category):
        Upload = self.repository.get(upload.create_id(url))
        Upload.upload_video(title, category)
        self.save(Upload)
    
    def add_photo(self, url, title, category):
        Upload = self.repository.get(upload.create_id(url))
        Upload.upload_photo(title, category)
        self.save(Upload)

    def add_article(self, url, title, category):
        Upload = self.repository.get(upload.create_id(url))
        Upload.upload_article(title, category)
        self.save(Upload)

    def get_events(self, url):
        Upload = self.repository.get(upload.create_id(url))
        return Upload.recent

    