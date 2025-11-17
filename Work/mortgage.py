# mortgage.py

principal = 500000.0
rate = 0.05
payment_original = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    payment = payment_original
    if ((month>=extra_payment_start_month) & (month<=extra_payment_end_month)):
        payment = payment_original+extra_payment

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, total_paid, principal)
    month+=1

print('Total paid', total_paid)