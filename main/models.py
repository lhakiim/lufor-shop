import uuid
from django.db import models
from django.contrib.auth.models import User

class shopEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    descriptions = models.TextField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5