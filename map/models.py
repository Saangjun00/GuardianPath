from django.db import models
from users.models import User

class UserRoute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.CharField(max_length=20)
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'}: {self.departure} -> {self.destination}"
    
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.departure} -> {self.destination}"