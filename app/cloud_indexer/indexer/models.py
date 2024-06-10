from django.db import models

class IndexedFile(models.Model):
    file_name = models.CharField(max_length=255)
    file_path = models.TextField()
    storage_type = models.CharField(max_length=50)
    indexed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

class SearchQuery(models.Model):
    query_text = models.CharField(max_length=255)
    executed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_text
