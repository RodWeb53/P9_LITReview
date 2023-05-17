from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ticket.forms import TicketForm, ReviewForm
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

@login_required
def create_review(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket_id = ticket.id
            review.save()
            return redirect('home')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()
    
    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }
    return render(request, "ticket/create-review.html", context=context)

