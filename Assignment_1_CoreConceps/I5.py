# Prog to compute Simple Interest

prin=float(input("Enter the Principal Loan Amount: "))
rate=float(input("Enter the Rate of Interest: "))
time=float(input("Enter the Loan Period (in Years): "))

s_int = (prin*rate*time)/100
print("\nTotal Simple Interest Earned: ",s_int)