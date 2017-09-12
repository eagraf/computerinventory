from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class EditComputerForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(EditComputerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-editcomputerform'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))

    serial = forms.CharField(
        label = "Serial #",
        max_length = 80,
        required = False,
    )

    manufacturer = forms.CharField(
        label = "Manufacturer",
        max_length = 80,
        required = False,
    )

    comments = forms.CharField(
        widget = forms.Textarea(),
        label = "Comments",
        max_length = 1024,
        required = False,
    )
