from django import forms
from .models import product, ProductBooked, UserNotes, Contact


class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'with-border'})
        self.fields['category'].widget.attrs.update({'class': 'selectpicker with-border', 'title': "Select Category"})
        self.fields['min_qty'].widget.attrs.update({'class': 'with-border', 'placeholder': "Min"})
        self.fields['max_qty'].widget.attrs.update({'class': 'with-border', 'placeholder': "Max"})
        # self.fields['slug'].widget.attrs.update({'class': 'with-border', 'placeholder': "Product Slug"})
        self.fields['max_user'].widget.attrs.update({'class': 'with-border', 'placeholder': "Enter no of Users"})
        self.fields['scale'].widget.attrs.update(
            {'class': 'selectpicker with-border', 'title': "Select Measuring Scale"})
        self.fields['price'].widget.attrs.update({'class': 'with-border', 'placeholder': "Price per piece"})
        self.fields['tags'].widget.attrs.update(
            {'class': 'keyword-input with-border', 'placeholder': "e.g. meat, drinks, vegetables"})
        self.fields['desc'].widget.attrs.update({'class': 'with-border', 'placeholder': "Describe you product..."},
                                                rows='5', cols='30')
        self.fields['image'].widget.attrs.update({'class': 'uploadButton-input', 'type': "file", 'id': "upload"})
        self.fields['pub_date'].widget.attrs.update({'class': 'uploadButton-input'})

    class Meta:
        model = product
        fields = (
            'title', 'price', 'category', 'min_qty', 'max_qty', 'tags', 'desc', 'scale', 'max_user', 'image',
            'pub_date')


class ProductBookedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class': 'with-border', 'placeholder': 'Enter quantity'})

    class Meta:
        model = ProductBooked
        fields = ('quantity',)


class AddNotesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['notes_priority'].widget.attrs.update(
            {'class': 'selectpicker with-border default margin-bottom-20', 'title': 'Priority', 'data - size': "7"})
        self.fields['notes_text'].widget.attrs.update(
            {'class': 'with-border', 'placeholder': 'Your Note text', 'cols': "10"})

    class Meta:
        model = UserNotes
        fields = ('notes_priority', 'notes_text')


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'with-border', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'with-border', 'placeholder': 'Your Email'})
        self.fields['subject'].widget.attrs.update({'class': 'with-border', 'placeholder': 'Subject'})
        self.fields['message'].widget.attrs.update(
            {'class': 'with-border', 'placeholder': 'Your Message', 'cols': "40", 'rows': "5"})

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')


class filterProduct(forms.Form):
    category = forms.CharField(widget=forms.CheckboxSelectMultiple(attrs={

        'class': "selectpicker",
        'multiple data-selected-text-format': "count",
        'data-size': "7", 'title': "All Categories"

    }))
    # price = forms.CharField(widget=forms.CharField(attrs={
    #
    #     'class': "range-slider",
    #     'data-slider-min': "1500",
    #     'data-slider-max': "15000",
    #     'data-slider-step': "100",
    #     'data-slider-value':"[1500,15000]"
    #
    # }))
