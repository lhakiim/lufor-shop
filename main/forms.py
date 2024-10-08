from django.forms import ModelForm
from main.models import shopEntry
from django.utils.html import strip_tags

class ShopEntryForm(ModelForm):
    class Meta:
        model = shopEntry
        fields = ["name", "price", "descriptions"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_descriptions(self):
        descriptions = self.cleaned_data["descriptions"]
        return strip_tags(descriptions)