from django.forms import ModelForm
from gadgets.models import Brand


# Create the form class.
class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
