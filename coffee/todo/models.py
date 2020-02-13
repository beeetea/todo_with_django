from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=100, null=False, help_text="이 부분은 필수입니다.")
    is_done = models.BooleanField(default=False)