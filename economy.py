op = input("Choose which formula you will use (PIB, EVA, FBCF): ")
if op == "PIB":
    n1 = float(input("Enter the ΣVA: "))
    n2 = float(input("Enter the IPSN: "))
    result = n1 + n2
    print(f"The result is: {result}")
elif op == "FBCF":
    n1 = float(input("Enter the PIB: "))
    n2 = float(input("Enter the DCF: "))
    n3 = float(input("Enter the ACOV: "))
    n4 = float(input("Enter the DEN: "))
    result = n1 - n2 - n3 - n4
    print(f"The result is: {result}")
elif op == "EVA":
    n1 = float(input("Enter the VA.Agricole: "))
    n2 = float(input("Enter the VA.Non Agricole: "))
    result = n1 + n2
    print(f"The result is: {result}")
else:
    print(f"{op} is not a valid formula")

