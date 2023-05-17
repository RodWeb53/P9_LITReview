from django import forms
from ticket.models import Ticket
from authentication.models import CustomeUser

    
class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image', ]