from django import forms
from .models import Product


def _build_choice_field(label, choices=None, required=False):
    empty_choice = (("", "------------"),)
    field = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control"}),
        label=label,
        choices=empty_choice,
        required=required,
    )
    if choices:
        field.choices += choices
    return field


class SearchForm(forms.Form):
    color = _build_choice_field(_("color"))
    name = _build_choice_field(_("name"))
    small="do 1000"
    medium = "do 5000"
    large = "more than 5k"
    Product_price = ((small, _("Small")), (medium, _("Medium")), (large, _("Large")))
    price = _build_choice_field(_("price"), Product_price )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["color"].choices += tuple(
            Product.objects.filter(pet__active=True).order_by("name").values_list("id", "name").distinct()
        )
        self.fields["color"].choices += tuple(Product.objects.values_list("id", "kind"))








class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('pic', 'name', 'color', 'description', 'price', )