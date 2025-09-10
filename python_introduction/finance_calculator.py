monthly_incomme = input ("Enter your monthly income: ")
monthly_expense = input("Enter your monthly expense: ")
mmonthly_saving = monthly_incomme - monthly_expense
projected_saving = (mmonthly_saving) * 12 + (mmonthly_saving * 12 * 0.05)
print("Your projected saving after one year is:", projected_saving)