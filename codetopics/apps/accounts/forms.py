from django import forms

Choices = [
    ('1', 'Web'),
    ('2', 'Mobile'),
    ('3', 'Embedded'),
    ('4', 'Data Structures & Algorithms'),
    ('5', 'Languages')
]

Medias = [
    ('1', 'Video'),
    ('2', 'Photo'),
    ('3', 'Article')
]

class UploadForm(forms.Form):
    URL = forms.URLField(label="Enter URL")
    title = forms.CharField(max_length=50, label="Enter title")
    media = forms.ChoiceField(choices=Medias, label="Choose media")
    category = forms.ChoiceField(choices=Choices, label="Choose category")
