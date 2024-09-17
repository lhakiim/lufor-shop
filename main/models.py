import uuid
from django.db import models

class shopEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    descriptions = models.TextField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5