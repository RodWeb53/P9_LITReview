from django import forms
from ticket.models import Ticket, Review, UserFollows
from authentication.models import CustomeUser

    
class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image', ]


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body', ]


class FollowUserForm(forms.ModelForm):
    followed_user = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
        attrs={"placeholder": "Saisir un utilisateur"})
        )
    
    def clean_followed_user(self):
        data = self.cleaned_data["followed_user"]

        followed_user = CustomeUser.objects.get(username__exact=data)
        return followed_user
    
    class Meta:
        model = UserFollows
        fields = ['followed_user', ]