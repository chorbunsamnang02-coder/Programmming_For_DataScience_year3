### Part A
def electricity_bill(kwh):
    
    if kwh < 0:
        return None
    tier1_kwh = min(max(kwh, 0), 50)
    tier2_kwh = min(max(kwh - 50, 0), 150)
    tier3_kwh = max(kwh - 200, 0)
    
    cost = (tier1_kwh * 480) + (tier2_kwh * 610) + (tier3_kwh * 730)
    total_before_vat = cost + 2000
    final_bill = total_before_vat * 1.10
    return round(final_bill)


###  part B
test_cases = [0, 35, 50, 120, 200, 350]
USD_RATE = 4100


for kwh in test_cases:
    bill_riel = electricity_bill(kwh)
    bill_usd = bill_riel / USD_RATE
    print(f"{kwh:3} kWh -> {bill_riel:9,} riel  (≈ {bill_usd:6.2f} USD)")


### part C

try:
    user_kwh = float(input("Please enter your monthly consumption in kWh: "))
    bill = electricity_bill(user_kwh)
    
    if bill is None:
        print("Error: Consumption cannot be negative.")
    else:
        usd_val = bill / USD_RATE
        print(f"Your total bill is: {bill:,} riel (≈ {usd_val:,.2f} USD)")
except ValueError:
    print("Please enter a valid number.")
