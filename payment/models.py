from django.db import models
from datetime import date
from loan.models import MicroLoan


class PaymentSchedule(models.Model):
    loan = models.ForeignKey(MicroLoan, verbose_name="Loan", on_delete=models.PROTECT)
    amortization = models.DecimalField(
        verbose_name="Amortization", max_digits=10, decimal_places=2
    )
    due_date = models.DateField(verbose_name="Due Date", default=date.today)
    principal = models.DecimalField(
        verbose_name="Principal", max_digits=10, decimal_places=2
    )
    interest = models.DecimalField(
        verbose_name="Interest", max_digits=10, decimal_places=2
    )
    principal_balance = models.DecimalField(
        verbose_name="Principal Balance", max_digits=10, decimal_places=2
    )
    interest_balance = models.DecimalField(
        verbose_name="Interest Balance", max_digits=10, decimal_places=2
    )
    surcharge = models.DecimalField(
        verbose_name="Surcharge", max_digits=10, decimal_places=2, default=0.0
    )
    is_paid = models.BooleanField(verbose_name="Paid", default=False)
