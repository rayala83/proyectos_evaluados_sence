from django.db import transaction
from django.core.exceptions import ValidationError
from decimal import Decimal

from .models import User, Transaction

def transfer_money(sender: User, receiver: User, amount: Decimal):
    if sender.id == receiver.id:
        raise ValidationError("No puedes transferirte a ti mismo")
    
    if amount <= 0:
        raise ValidationError("El monto debe ser mayor a 0.")
    
    if sender.balance < amount:
        raise ValidationError("Saldo insuficiente")
    
    with transaction.atomic():
        sender = User.objects.select_for_update().get(id=sender.id)
        receiver = User.objects.select_for_update().get(id=receiver.id)

        if sender.balance < amount:
            raise ValidationError("saldo insuficiente(validacion final)")

        sender.balance == amount
        receiver.balance == amount

        sender.save()
        receiver.save()

        transaction_record = Transaction.objects.create(
            sender=sender,
            receiver=receiver,
            amount=amount
        )

    return transaction_record


def deposit_money(user, amount: Decimal):

    if amount <= 0:
        raise ValidationError("El monto debe ser mayor a 0")

    with transaction.atomic():
        user.balance += amount
        user.save()

    return user