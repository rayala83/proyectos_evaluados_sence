from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.db.models import Q
from .forms import ContactForm

from .models import User, Transaction, Contact
from .services import transfer_money, deposit_money

@login_required
def transfer_view(request):

    contacts = Contact.objects.filter(owner=request.user)
    form = ContactForm()

    if request.method == "POST":

        # 🟣 Crear contacto
        if "create_contact" in request.POST:
            form = ContactForm(request.POST)

            if form.is_valid():
                contact = form.save(commit=False)
                contact.owner = request.user
                contact.save()

                messages.success(request, "Contacto agregado")
                return redirect("transfer")

        # 🔵 Transferir
        elif "transfer" in request.POST:
            contact_id = request.POST.get("receiver")
            amount = request.POST.get("amount")

            try:
                contact = Contact.objects.get(id=contact_id)

                # 🔥 Buscar usuario real por email
                receiver = User.objects.get(email=contact.email)

                amount = Decimal(amount)

                transfer_money(request.user, receiver, amount)

                messages.success(request, "Transferencia realizada 💸")
                return redirect("transfer")

            except User.DoesNotExist:
                messages.error(request, "El contacto no tiene cuenta en la plataforma")

            except Exception as e:
                messages.error(request, str(e))

    return render(request, "wallet/transfer.html", {
        "contacts": contacts,
        "form": form
    })

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "credenciales invaidas")

    return render(request, "wallet/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard_view(request):

    
    transactions = Transaction.objects.filter(
        Q(sender=request.user) | Q(receiver=request.user)
    ).order_by('-transaction_date')[:5]  # últimas 5

    context = {
        "transactions": transactions
    }

    return render(request, "wallet/dashboard.html", context)


@login_required
def transactions_view(request):
    transactions = Transaction.objects.filter(
        sender=request.user
    ) | Transaction.objects.filter(
        receiver=request.user
    )

    return render(request, "wallet/transactions.html", {
        "transactions": transactions.order_by('-transaction_date')
    })


def deposit_view(request):

    if request.method == "POST":
        amount = request.POST.get("amount")

        try:
            amount = Decimal(amount)
            deposit_money(request.user, amount)

            messages.success(request, "Depósito realizado 💰")
            return redirect("dashboard")

        except Exception as e:
            messages.error(request, str(e))

    return render(request, "wallet/deposit.html")


           


