from django import forms
from ticket.models import Ticket, Review
from authentication.models import CustomeUser

    
class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image', ]


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body', ]