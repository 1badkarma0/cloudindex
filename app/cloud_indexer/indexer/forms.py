from django import forms

class IndexStorageForm(forms.Form):
    STORAGE_CHOICES = [
        ('s3', 'S3'),
        ('onedrive', 'OneDrive'),
        ('webdav', 'WebDAV'),
        ('sftp', 'SFTP'),
    ]
    storage_type = forms.ChoiceField(choices=STORAGE_CHOICES)
    storage_path = forms.CharField(max_length=255)

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255)