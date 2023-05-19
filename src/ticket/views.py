from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from itertools import chain
from ticket.forms import TicketForm, ReviewForm
from .models import Ticket, Review

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

    context = {"form": form, }
    return render(request, "ticket/create-ticket.html", context=context)

@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    form = TicketForm(instance=ticket )
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {"form": form, }
    return render(request, "ticket/update-ticket.html", context=context)


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

@login_required
def posts(request):
    tickets = Ticket.objects.filter(user_id=request.user)
    reviews = Review.objects.filter(user_id=request.user)
    tickets_and_reviews = sorted(chain(tickets, reviews), key=lambda instance:
    instance.time_created, reverse=True)

    context = {
        "tickets": tickets,
        "reviews": reviews,
        "tickets_and_reviews": tickets_and_reviews,
    }
    
    return render(request, "ticket/posts.html", context=context)