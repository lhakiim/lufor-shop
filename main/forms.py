from django.forms import ModelForm
from main.models import shopEntry

class ShopEntryForm(ModelForm):
    class Meta:
        model = shopEntry
        fields = ["name", "price", "descriptions"]