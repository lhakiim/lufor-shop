from django.db import models

class shopEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    descriptions = models.TextField()
    # mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5