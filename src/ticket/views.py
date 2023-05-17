from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ticket.forms import TicketForm
from .models import Ticket

@login_required
def home(request):
    return render(request, 'ticket/home.html')


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    else:
        form = TicketForm()

    context = {"form": form,}
    return render(request, "ticket/create-ticket.html", context=context)

