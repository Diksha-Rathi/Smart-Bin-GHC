from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

class ToDoForm(forms.Form):
    from_date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
    to_date = forms.DateTimeField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))