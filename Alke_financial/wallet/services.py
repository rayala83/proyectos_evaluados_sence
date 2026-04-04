from django.db import transaction
from django.core.exceptions import ValidationError
from decimal import Decimal

from .models import User, Transaction

def transfer_money(sender: User, receiver: User = None, contact=None, amount: Decimal = 0):

    if amount <= 0:
        raise ValidationError("Monto inválido")

    if receiver and sender.id == receiver.id:
        raise ValidationError("No puedes transferirte a ti mismo")

    if sender.balance < amount:
        raise ValidationError("Saldo insuficiente")

    with transaction.atomic():

        sender = User.objects.select_for_update().get(id=sender.id)

        sender.balance -= amount
        sender.save()

        # 🔥 si el usuario existe
        if receiver:
            receiver = User.objects.select_for_update().get(id=receiver.id)
            receiver.balance += amount
            receiver.save()

        Transaction.objects.create(
            sender=sender,
            receiver=receiver,
            contact=contact,
            amount=amount
        )



def deposit_money(user, amount: Decimal):

    if amount <= 0:
        raise ValidationError("El monto debe ser mayor a 0")

    with transaction.atomic():
        user.balance += amount
        user.save()

        # 🔥 registrar movimiento
        Transaction.objects.create(
            sender=None,
            receiver=user,
            amount=amount
        )

    return user