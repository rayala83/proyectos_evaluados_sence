from django.db import models
from django.contrib.auth.models import AbstractUser

class Currency(models.Model):
    currency_name = models.CharField(max_length=50, unique=True)
    currency_symbol = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'moneda'
        verbose_name_plural = 'monedas'

    def __str__(self):
        return f"{self.currency_name} ({self.currency_symbol})"
    

class User(AbstractUser):
    email = models.EmailField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, related_name="user")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'nombre'

    def __str__(self):
        return f"{self.first_name} - {self.email}"
    
class Contact(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def __str__(self):
        return f"{self.name} ({self.email})"
    

class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transaction', null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_transaction', null=True, blank=True)
    contact = models.ForeignKey(Contact,on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'transaccion'
        verbose_name_plural = 'transacciones'


    def __str__(self):
        return f"{self.sender} - {self.receiver} - {self.amount}"
    





    
