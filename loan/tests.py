from django.test import TestCase
from .models import LoanProduct, MicroLoan
from member.models import Member
from payment.models import PaymentSchedule


class LoanCalculationTest(TestCase):
    def setUp(self):
        self.member = Member.objects.create(
            firstname="John", lastname="Doe", middlename="Lee"
        )

        self.product = LoanProduct.objects.create(
            name="Individual",
            interest_type="monthly",
            interest_rate=0.025,
            surcharge_rate=0.015,
            term_type="weekly",
            terms=20,
        )

        self.loan = MicroLoan.objects.create(
            name="ML000001",
            member=self.member,
            product=self.product,
            loan_amount=80000.00,
        )

    def _get_compound_interest(self):
        return self.product.interest_rate * (self.product.terms / 4)

    def _get_loan_amount(self):
        interest = self.loan.loan_amount * (self._get_compound_interest())

        return self.loan.loan_amount, interest

    def _get_amortization(self):
        return sum(self._get_loan_amount()) / self.product.terms

    def test_total_loan_amount(self):
        self.assertEqual(sum(self._get_loan_amount()), 90000.0)

    def test_amortization_amount(self):
        self.assertEqual(self._get_amortization(), 4500.0)

    def test_paysched(self):
        principal, interest = self._get_loan_amount()
        payscheds = []
        for term in range(0, self.product.terms):
            payscheds.append(
                PaymentSchedule(
                    loan=self.loan,
                    amortization=self._get_amortization(),
                    principal=principal / self.product.terms,
                    interest=interest / self.product.terms,
                    principal_balance=principal / self.product.terms,
                    interest_balance=interest / self.product.terms,
                )
            )
        PaymentSchedule.objects.bulk_create(payscheds)

        paysched = PaymentSchedule.objects.filter(loan__id=self.loan.id)

        self.assertEqual(len(paysched), 20)

    def tearDown(self):
        PaymentSchedule.objects.all().delete()
        self.loan.delete()
        self.member.delete()
        self.product.delete()
