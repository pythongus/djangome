from django.db import models

class Entry(models.Model):
    EXPENSE = 'E'
    INCOME = 'I'
    ENTRY_TYPE_CHOICES = [
        (EXPENSE, 'Expense'),
        (INCOME, 'Income'),
    ]
    category = models.CharField(max_length=50, null=True, blank=True)
    entry_date = models.DateTimeField('entry date')
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    origin = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=200)
    entry_type = models.CharField(max_length=1,
                                  default=EXPENSE,
                                  choices=ENTRY_TYPE_CHOICES)
    balance = models.DecimalField(max_digits=9,
                                  decimal_places=2,
                                  null=True,
                                  blank=True)

    def __str__(self):
        neg = '-$' if self.entry_type == 'E' else '$'
        return f'[{self.category}] {self.description}: {neg}{self.amount}'
