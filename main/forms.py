from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["product_name", "price", "description", "rating", "image"]

    def clean_prosuct(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)