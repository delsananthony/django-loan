from django.db import models
from datetime import date

from member.models import Member


class LoanProduct(models.Model):
    INTEREST_TYPES = (
        ("weekly", "Weekly"),
        ("montly", "Monthly"),
    )

    TERM_TYPES = (
        ("weekly", "Weekly"),
        ("montly", "Monthly"),
    )

    name = models.CharField(verbose_name="Name", max_length=255)
    interest_type = models.CharField(
        verbose_name="Interest Type", max_length=255, choices=INTEREST_TYPES
    )
    interest_rate = models.DecimalField(
        verbose_name="Interest Rate", max_digits=10, decimal_places=4
    )
    surcharge_rate = models.DecimalField(
        verbose_name="Surcharge Rate", max_digits=10, decimal_places=4
    )
    term_type = models.CharField(
        verbose_name="Term Type", max_length=255, choices=TERM_TYPES
    )
    terms = models.IntegerField(verbose_name="Terms")

    def __str__(self):
        return self.name


class MicroLoan(models.Model):
    LOAN_STATE = (
        ("draft", "Draft"),
        ("confirm", "Confirmed"),
        ("done", "Done"),
        ("cancel", "Cancelled"),
    )

    name = models.CharField(verbose_name="Name", max_length=255)
    member = models.ForeignKey(Member, verbose_name="Member", on_delete=models.PROTECT)
    transaction_date = models.DateField(
        verbose_name="Transaction Date", default=date.today
    )
    product = models.ForeignKey(
        LoanProduct, verbose_name="Loan Product", on_delete=models.PROTECT
    )
    loan_amount = models.DecimalField(
        verbose_name="Loan Amount", max_digits=10, decimal_places=2
    )
    amortization = models.DecimalField(
        verbose_name="Amortization", max_digits=10, decimal_places=2, default=0.00
    )
    state = models.CharField(
        verbose_name="State", max_length=255, choices=LOAN_STATE, default="draft"
    )
    # needed fields:
    # member_id = refers to the member who's gonna make a loan
    # clerk_id = refers to the one creating the loan transaction, literally the user
    # needs tracking for payment schedule
    # needs tracking for surcharges
    # needs tracking for savings account
    # loan type ? needs config
    # loan product ? needs config
    # loan amount = monetary? decimal?
    # interest type?
    # release date
    # first duedate
    # amortization
    # payment type

    def __str__(self):
        return self.name
