from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Expense

@login_required
def dashboard(request):
    expenses = Expense.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        Expense.objects.create(title=title, amount=amount, category=category, date=date)
        return redirect('dashboard')

    # 📊 Category-wise total
    categories = {}
    for expense in expenses:
        if expense.category in categories:
            categories[expense.category] += expense.amount
        else:
            categories[expense.category] = expense.amount

    return render(request, 'dashboard.html', {
        'expenses': expenses,
        'categories': categories
    })

def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('dashboard')

def edit_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == 'POST':
        expense.title = request.POST['title']
        expense.amount = request.POST['amount']
        expense.category = request.POST['category']
        expense.date = request.POST['date']
        expense.save()
        return redirect('dashboard')

    return render(request, 'edit.html', {'expense': expense})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})