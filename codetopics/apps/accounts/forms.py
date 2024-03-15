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

categories = [
    ('1', '.NET'),
    ('2', 'Node JS'),
    ('3', 'Django'),
    ('4', 'React'),
    ('5', 'Android'),
    ('6', 'IOS'),
    ('7', 'Operating Systems'),
    ('8', 'Assembly'),
    ('9', 'Command Line'),
    ('10', 'Processor'),
    ('11', 'Lists'),
    ('12', 'Graphs'),
    ('13', 'Trees'),
    ('14', 'Hash'),
    ('15', 'Stack'),
    ('16', 'Dynamic Programming'),
    ('17', 'Backtracking'),
    ('19', 'Java'),
    ('20', 'Python'),
    ('21', 'C'),
    ('22', 'HTML'),
    ('23', 'CSS'),
    ('24', 'Assembly'),
    ('25', 'JavaScript'),
]

class UploadForm(forms.Form):
    URL = forms.URLField(label="Enter URL")
    title = forms.CharField(max_length=50, label="Enter title")
    media = forms.ChoiceField(choices=Medias, label="Choose media")
    topic = forms.ChoiceField(choices=Choices, label="Choose topic")
    category = forms.ChoiceField(choices=categories, label="Choose category")

