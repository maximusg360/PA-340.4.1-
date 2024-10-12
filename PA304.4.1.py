# Problem 1

x = 7
if x < 10:
    print("Less than 10")

# Change x to 15
x = 15

# Problem 2

x = 7
if x < 10:
    print("Less than 10")
else:
    print("Greater than 10")

# Change x to 15
x = 15

# Problem 3
x = 15
if x < 10:
    print("Less than 10")
elif 10 < x < 20:
    print("Between 10 and 20")
else:
    print("Greater than or equal to 20")

# Change x to 50
x = 50

# Problem 4
x = 15
if x < 10 or x > 20:
    print("Out of range")
else:
    print("In range")

# Change x to 5
x = 5

# Problem 5
score = int(input("Enter your score: "))
if score < 0 or score > 100:
    print("Score out of range")
elif 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")

# Problem 6
filing_status = input("Enter your filing status (Single, Married Filing Jointly, Married Filing Separately, Head of Household): ").strip()
income = float(input("Enter your taxable income: "))

tax = 0

if filing_status == "Single":
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 835 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 4675 + (income - 33950) * 0.25
    elif income <= 171550:
        tax = 16750 + (income - 82250) * 0.28
    elif income <= 373650:
        tax = 40800 + (income - 171550) * 0.33
    else:
        tax = 112500 + (income - 373650) * 0.35

elif filing_status == "Married Filing Jointly":
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 1670 + (income - 16700) * 0.15
    elif income <= 137050:
        tax = 9525 + (income - 67900) * 0.25
    elif income <= 208850:
        tax = 26250 + (income - 137050) * 0.28
    elif income <= 373650:
        tax = 46650 + (income - 208850) * 0.33
    else:
        tax = 100000 + (income - 373650) * 0.35

elif filing_status == "Married Filing Separately":
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 835 + (income - 8350) * 0.15
    elif income <= 68525:
        tax = 4675 + (income - 33950) * 0.25
    elif income <= 104425:
        tax = 13125 + (income - 68525) * 0.28
    elif income <= 186825:
        tax = 23325 + (income - 104425) * 0.33
    else:
        tax = 50000 + (income - 186825) * 0.35

elif filing_status == "Head of Household":
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 1195 + (income - 11950) * 0.15
    elif income <= 117450:
        tax = 6445 + (income - 45500) * 0.25
    elif income <= 190200:
        tax = 23675 + (income - 117450) * 0.28
    elif income <= 373650:
        tax = 42275 + (income - 190200) * 0.33
    else:
        tax = 100000 + (income - 373650) * 0.35

print(f"Your tax is: ${tax:.2f}")