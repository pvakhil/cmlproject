from django.db import models



class District(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Registration(models.Model):
    Name = models.CharField(max_length=250)
    dob = models.DateField
    age = models.CharField(max_length=5)
    Gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female','Female')], default="", blank=True)
    phone_number = models.CharField(max_length=12)
    email_id = models.EmailField
    address = models.TextField(max_length=300)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    account_type = models.CharField(max_length=30, choices=[('savings', 'Savings'), ('current', 'Current')], default='savings')
    materials_provide = models.CharField(max_length=30,  choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')], default="", blank=True)

    def __str__(self):
        return self.name




