from django.db import models

class Token (models.Model):
    id = models.CharField(max_length=255, blank=False, primary_key=True)
    unique_hash = models.TextField(blank= False)
    tx_hash = models.TextField(blank= False)
    media_url = models.TextField(blank= False)
    owner = models.CharField(max_length= 46, blank= False)
