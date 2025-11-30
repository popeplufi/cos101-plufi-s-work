print("Choose a formula:")
print("a → v = (d1 + d2) / (t1 + t2)  (Average Speed)")
print("b → a = (v1 + v2) / t          (Average Acceleration)")
print("c → ρ = (m1 + m2) / (V1 + V2)   (Density)")
print("d → P = (F1 + F2) / A           (Pressure)")
print("e → f = (N1 + N2) / t           (Frequency)")

choice = input("Enter a, b, c, d, or e: ").lower()


if choice == "a":
    print("\nFormula selected: v = (d1 + d2) / (t1 + t2)")
    d1 = float(input("Enter distance d1: "))
    d2 = float(input("Enter distance d2: "))
    t1 = float(input("Enter time t1: "))
    t2 = float(input("Enter time t2: "))
    v = (d1 + d2) / (t1 + t2)
    print("Average Speed =", v, "m/s")


elif choice == "b":
    print("\nFormula selected: a = (v1 + v2) / t")
    v1 = float(input("Enter velocity v1: "))
    v2 = float(input("Enter velocity v2: "))
    t = float(input("Enter time t: "))
    a = (v1 + v2) / t
    print("Average Acceleration =", a, "m/s²")


elif choice == "c":
    print("\nFormula selected: ρ = (m1 + m2) / (V1 + V2)")
    m1 = float(input("Enter mass m1: "))
    m2 = float(input("Enter mass m2: "))
    V1 = float(input("Enter volume V1: "))
    V2 = float(input("Enter volume V2: "))
    rho = (m1 + m2) / (V1 + V2)
    print("Density =", rho, "kg/m³")


elif choice == "d":
    print("\nFormula selected: P = (F1 + F2) / A")
    F1 = float(input("Enter force F1: "))
    F2 = float(input("Enter force F2: "))
    A = float(input("Enter area A: "))
    P = (F1 + F2) / A
    print("Pressure =", P, "N/m²")


elif choice == "e":
    print("\nFormula selected: f = (N1 + N2) / t")
    N1 = float(input("Enter cycles N1: "))
    N2 = float(input("Enter cycles N2: "))
    t = float(input("Enter time t: "))
    f = (N1 + N2) / t
    print("Frequency =", f, "Hz")

else:
    print("Invalid option. Please try the code again.")
