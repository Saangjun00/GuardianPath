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
    
class ElevatorLocation(models.Model):
    SubEleExitID = models.IntegerField(primary_key=True)
    SubEleExitKind = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()


    class Meta:
        managed = False  # 기존 테이블과 직접 연동할 경우 False로 설정
        db_table = 'elevator_location'  # 데이터베이스 테이블 이름 

    def str(self):
        return f"{self.latitude}, {self.longitude}"

class EscalatorLocation(models.Model):
    esc_ID = models.IntegerField(primary_key=True)
    esc_latitude = models.FloatField()
    esc_longitude = models.FloatField()

    class Meta:
        managed = False  # 기존 테이블과 직접 연동할 경우 False로 설정
        db_table = 'escalator_location'  # 데이터베이스 테이블 이름

    def str(self):
        return f"{self.esc_latitude}, {self.esc_longitude}"