from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)


class RoomBookingForm(forms.Form):
    room = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    date = forms.CharField(max_length=15)
    no_of_adults = forms.IntegerField()
    no_of_children = forms.IntegerField()
    no_of_rooms = forms.IntegerField()
    no_of_extra_beds = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea, required=False)