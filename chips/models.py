from django.db import models

class NegativeSpending(models.Model):
    date = models.DateField()
    item = models.CharField(max_length=25)
    amount = models.IntegerField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} - {self.item} (${self.amount})"
    
class Transaction(models.Model):
    TYPE_CHOICES = [
        ('chip', 'Chip'), # Savings
        ('dip', 'Dip'), # Spendings
    ]

    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    # note = models.TextField(blank=True)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.date} - {self.type} - ${self.amount}"