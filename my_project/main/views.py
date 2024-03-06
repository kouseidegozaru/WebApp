# views.py
from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def customer_list(request):
    customer_items = Customer.objects.all()
    return render(request, 'customer_list.html', {'customer_items': customer_items})

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

@login_required
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect('customer_list')

@login_required
def search(request):
    keyword = request.GET.get('keyword', '')
    # すべてのフィールドに対してキーワードで検索する
    customer_items = Customer.objects.filter(
        Q(first_name__icontains=keyword) |
        Q(last_name__icontains=keyword) |
        Q(email__icontains=keyword) |
        Q(phone_number__icontains=keyword) |
        Q(age__icontains=keyword) |
        Q(gender__icontains=keyword)
    )
    return render(request, 'customer_list.html', {'customer_items': customer_items})
