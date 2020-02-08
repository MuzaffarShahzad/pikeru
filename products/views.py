from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from taggit.models import Tag
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from .models import product, ProductBooked, Category, Order
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .forms import AddProductForm, ProductBookedForm, AddNotesForm, filterProduct


# @login_required
# def post_product(request):
#     if request.method == 'POST':
#         product_form = AddProductForm(request.POST, request.FILES, instance=request.user)
#         if product_form.is_valid():
#             product_form.save()
#             messages.success(request, 'Product has been saved successfully')
#             return redirect('post_product')
#     else:
#         product_form = AddProductForm(instance=request.user)
#     return render(request, 'products/post_product.html', {'p_form': product_form})


# class productView(DetailView):
#     model = product
#     template_name = 'shop/prodView.html'
#
#     def get(self, *args, **kwargs):
#         product_name = product.objects.get(slug=self.slug)
#         context = {
#             'object': product_name}
#         return render(self.request, 'products/product_view.html', context)
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = product
    form_class = AddProductForm
    common_tags = product.tags.most_common()[:4]

    def form_valid(self, form):  # to automatically fill login user to add in post author table
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = product
    fields = [
        'title', 'price', 'category', 'min_qty', 'max_qty', 'tags', 'desc', 'scale', 'max_user', 'image', 'pub_date']

    def form_valid(self, form):  # to automatically fill login user to add in post author table
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):  # to avoid users to edit other users post
        prod = self.get_object()
        if self.request.user == prod.user:  # to get the current login user
            return True
        else:
            return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = product
    success_url = '/'

    def test_func(self):
        prod = self.get_object()
        if self.request.user == prod.user:
            return True
        else:
            return False


class ProductListView(ListView):
    model = product
    form_class = filterProduct
    template_name = 'products/product_list.html'  # <app>/<model>_<viewType>.html
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.exclude(category_name='Uncategorized')
        return context


# def tagged(request, slug):
#     tag = get_object_or_404(Tag, slug=slug)
#     # Filter posts by tag name
#     posts = product.objects.filter(tags=tag)
#     context = {
#         'tag':tag,
#         'posts':posts,
#     }
#     return render(request, 'products/product_view.html', context)
#

def productView(request, slug):
    product_booked = get_object_or_404(product, slug=slug)
    if request.method == 'POST':
        product_booked_form = ProductBookedForm(request.POST)
        qty = request.POST.get('quantity')

        if product_booked_form.is_valid():
            duplicate_product_booked = ProductBooked.objects.filter(user=request.user)
            if not duplicate_product_booked:
                product_booked_form = ProductBooked(user=request.user, items=product_booked, quantity=qty)
                product_booked_form.save()
                subject = product_booked.title + ' ' + 'booked on pikeru',
                user_email = product_booked.user.email
                message = 'Thank you for your order on Pikeru.com, your product' + ' ' + product_booked.title + ' ' + 'has been booked.'
                email = EmailMessage(subject, message, to=[user_email, ])
                email.send()
                return redirect('checkout')
            else:
                messages.error(request, 'You already booked this product.')


    else:
        print('invalid')
        product_booked_form = ProductBookedForm()
    product_name = get_object_or_404(product, slug=slug)
    product_booked = ProductBooked.objects.filter(items=product_name)
    context = {
        'object': product_name,
        'form': product_booked_form,
        'pro_booked': product_booked
    }
    return render(request, 'products/product_view.html', context)


class UserProductList(ListView):
    model = product
    template_name = 'products/user_product_listing.html'  # <app>/<model>_<viewType>.html
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        return product.objects.filter(user=self.request.user).order_by('-pub_date')



class CategoryListView(ListView):
    model = product
    template_name = 'products/category_view.html'  # <app>/<model>_<viewType>.html
    context_object_name = 'products'

    def get_queryset(self):
        cat = get_object_or_404(Category, category_name=self.kwargs.get('cat_name'))
        return product.objects.filter(category=cat).order_by('-pub_date')


def categoryView(request, cat_name):
    categories = product.objects.filter(category=cat_name)

    context = {
        'category': categories
    }
    return render(request, 'products/category_view.html', context)


@login_required
def checkout(request):
    book_products = ProductBooked.objects.filter(user=request.user, payment=False)
    total = 0
    for item in book_products:
        total += item.quantity * item.items.price

    return render(request, 'products/checkout.html', {'pro_book': book_products, 'totalQty': total})


def process_payment(request):
    book_products = ProductBooked.objects.filter(user=request.user, payment=False)
    items = []
    for item in book_products:
        items += [item.items.title]
        order_id = item.id
    print(items)
    total = 0
    for item in book_products:
        total += item.quantity * item.items.price
    # order_id = request.session.get('order_id')
    # order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': total,
        'item_name': items,
        'invoice': order_id,
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'products/process_payment.html', {'form': form})


@csrf_exempt
def payment_done(request):
    return render(request, 'products/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'products/payment_cancelled.html')
