from django.db import models

# Create your models here.

class Expense(models.Model):
    Category=[
        ('food','Food'),
        ('transport','Transport'),
        ('entertainment','Entertainment'),
        ('bills','Bills'),
        ('other','Other'),
    ]
    title=models.CharField(max_length=20)
    amount=models.IntegerField()
    category=models.CharField(max_length=20,choices=Category)
    date=models.DateField()
    description=models.TextField(blank=True)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}-{self.amount}"
    