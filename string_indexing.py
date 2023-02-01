# [start : end : step]
#start zawiera liczbę zaczynającą
#end nie zawiera liczby kończącej

credit_number = "1234-5678-9012-3456"

#print(credit_number[4]) #liczymy od zera przy indeksowaniu

#print(credit_number[0:4]) or print(credit_number[:4])

#print(credit_number[5:9]) or print(credit_number[5:])

#jeśli podamy indeks na - będzie liczył od tyłu np. print(credit_number[-1]) wyjdzie 6 w tym przykładzie

#jeśli chcesz tylko step wpisujesz cyfrę po dwóch : np. print(credit_number[::6]) pokazuję co drugą cyfrę z credit_number

#last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")

#jeśli chcemy odwrócić ciąg liczb:
credit_number = credit_number[::-1]
print(credit_number)