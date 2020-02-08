from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import DeleteView
from products.models import Category, product, ProductBooked
from .forms import UserRegistrationForm, UserUpdate, ProfileUpdate
from products.forms import AddNotesForm, ContactForm
from products.models import UserNotes


def main_index(request):
    categories = Category.objects.exclude(category_name='Uncategorized')
    prod = product.objects.all()
    context = {
        'categories': categories,
        'product': prod

    }
    return render(request, 'users/index.html', context)


def login(request):
    return render(request, 'users/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You can Login now as {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def dashboard(request):
    if request.method == 'POST':
        note_form = AddNotesForm(request.POST or None)
        if note_form.is_valid():
            note_form.instance.notes_user = request.user
            note_form.save()
            messages.success(request, 'Your Notes has been saved!')
            return redirect('dashboard')
    else:
        note_form = AddNotesForm(instance=request.user)

    orders = ProductBooked.objects.filter(user=request.user)
    notes = UserNotes.objects.filter(notes_user=request.user)
    context = {
        'orders': orders,
        'Noteform': note_form,
        'userNotes': notes
    }
    return render(request, 'users/dashboard.html', context)


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserNotes
    success_url = '/dashboard'

    def test_func(self):
        notes = self.get_object()
        if self.request.user == notes.notes_user:
            return True
        else:
            return False

@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdate(request.POST, instance=request.user)
        profile_update_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        print('invalid')
        user_update_form = UserUpdate(instance=request.user)
        profile_update_form = ProfileUpdate(instance=request.user.profile)

    context = {
        'User_update_form': user_update_form,
        'profile_update_form': profile_update_form,

    }
    return render(request, 'users/profile.html', context)


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message is submitted successfully')
    else:
        contact_form = ContactForm(request.POST)
    return render(request, 'users/contact.html', {'contactForm': contact_form})
