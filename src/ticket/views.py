from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from itertools import chain
from ticket.forms import TicketForm, ReviewForm, FollowUserForm
from .models import Ticket, Review, UserFollows

@login_required
def home(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    tickets_and_reviews = sorted(chain(tickets, reviews), key=lambda instance:
    instance.time_created, reverse=True)
   

    return render(request, 'ticket/home.html', locals())

@login_required
def add_ticket(request, ticket_id=None):
    form = TicketForm(
        request.POST if request.method == 'POST' else None,
        request.FILES if request.method == 'POST' else None,
        instance=Ticket.objects.get(pk=ticket_id) if ticket_id is not None else None
    )
    if request.method == 'POST' and form.is_valid():
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.save()
        return redirect('home')
    return render(request, "ticket/create_ticket.html", locals())

@login_required
def delete_ticket(request, ticket_id=None):
    if request.method == 'POST':
        ticket_id = request.POST.get("ticket_id")
        ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
        ticket.delete()
        return redirect('posts')
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    return render(request, "ticket/delete_ticket.html", locals())

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
    return render(request, "ticket/create_review.html", context=context)

@login_required
def update_review(request, review_id=None):
    form = ReviewForm(
        request.POST if request.method == 'POST' else None,
        instance=Review.objects.get(pk=review_id) if review_id is not None else None
    )
    if request.method == 'POST' and form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        return redirect('home')
    review = get_object_or_404(Review, id=review_id, user=request.user)
    return render(request, "ticket/update_review.html", locals())

@login_required
def delete_review(request, review_id=None):
    if request.method == 'POST':
        review_id = request.POST.get("review_id")
        review = get_object_or_404(Review, id=review_id, user=request.user)
        review.delete()
        return redirect('posts')
    review = get_object_or_404(Review, id=review_id, user=request.user)

    return render(request, "ticket/delete_review.html", locals())

@login_required
def create_review_in_ticket(request, ticket_id=None):
    form = TicketForm(
        request.POST if request.method == 'POST' else None,
        request.FILES if request.method == 'POST' else None,
        instance=Ticket.objects.get(pk=ticket_id) if ticket_id is not None else None
    )
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket_id = form.instance.pk
            review.save()
            return redirect('home')
        
    return render(request, "ticket/create_review_in_ticket.html", locals())

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


@login_required
def followers(request):
    users_following = UserFollows.objects.filter(user_id=request.user)
    users_by_follow = UserFollows.objects.filter(followed_user=request.user)
    
    error_message =""
    
    if request.method == 'POST':
        form =FollowUserForm(request.POST)
        
        try:
            if form.is_valid():
                user = form.save(commit=False)
                user.user = request.user
                user.save()
                return redirect('followers')
        except ObjectDoesNotExist:
            error_message = "L'utilsateur n'est pas connu"
        except IntegrityError:
            error_message = "Cet utilsateur fait déja parti de vos abonnés"
    else:
        form = FollowUserForm(request.POST)
    
    return render(request, "ticket/follows.html", locals())


@login_required
def unfollow(request, user_id=None):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = get_object_or_404(UserFollows, id=user_id, user=request.user)
        user.delete()
        return redirect("followers")
    user = get_object_or_404(UserFollows, id=user_id, user=request.user)
    
    return render(request, "ticket/unfollow.html", locals())

