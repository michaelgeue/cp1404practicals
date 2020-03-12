TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    print("Electricity bill estimator 2.0")
    tariff = int(input("Which tariff? 11 or 31: "))

    while tariff != 11 and tariff != 31:
        print("Invalid tariff")
        tariff = int(input("Which tariff? 11 or 31: "))

    if tariff == 11:
        tariff_price = TARIFF_11
    else:
        tariff_price = TARIFF_31

    kwh_daily_use = float(input("Enter daily use in kWh: "))
    number_of_billing_days = int(input("Enter number of billing days: "))
    bill_price = number_of_billing_days * kwh_daily_use * tariff_price
    print("Estimated bill: $" + format(bill_price, '.2f'))


main()
