# Solution to Exercise3.4
bill_before_tax=float(input("Enter the bill amount before tax:$ "))
service_tax=float(input("Enter the service tax percentage: "))
amount_to_be_paid= bill_before_tax + bill_before_tax * service_tax/100
print(f"The amount to be paid: ${amount_to_be_paid}")
