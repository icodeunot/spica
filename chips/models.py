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