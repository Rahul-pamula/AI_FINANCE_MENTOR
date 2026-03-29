from django.db import models

class UserFinancialData(models.Model):
    income = models.FloatField()
    expenses = models.FloatField()
    savings = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FinancialData (Income: {self.income})"
