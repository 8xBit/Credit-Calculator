import math
import argparse

arguments = 0

# formula for i
def formula_i(credit_interest):
    i = (credit_interest / 100) / (12 / 100) / 100
    return i

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Declaration of arguments
    parser.add_argument("--type", help="Type of credit", required=False, default=None)                      # type of payment
    parser.add_argument("--principal", help="Principal of credit", type=int, required=False, default=None)  # credit principal
    parser.add_argument("--periods", help="Periods of credit", type=int, required=False, default=None)      # count of periods
    parser.add_argument("--payment", help="Payment of credit", type=int, required=False, default=None)      # monthly payment
    parser.add_argument("--interest", help="Interest of credit", type=float, required=False, default=None)  # interest rate

    args = parser.parse_args()

    # Annuity payment
    if args.type == "annuity":

        arguments += 1 if args.type != None else arguments == arguments - 1
        arguments += 1 if args.principal != None else arguments == arguments - 1
        arguments += 1 if args.periods != None else arguments == arguments - 1
        arguments += 1 if args.payment != None else arguments == arguments - 1
        arguments += 1 if args.interest != None else arguments == arguments - 1

        if args.interest is None:
            print("Incorrect parameters")
        elif arguments != 4:
            print("Incorrect parameters")

        # User wants args.periods
        elif args.principal != None and args.payment != None and args.interest != None and args.periods is None:

            P = args.principal
            A = args.payment
            i = formula_i(args.interest)

            # formula for n
            n = math.ceil(math.log(A / (A - i * P)) / math.log(1 + i))

            count_years = math.floor(n / 12)
            count_months = n % 12

            payment = math.ceil(n * A)

            if count_years == 0:
                print(f"You need {count_months} months to repay this credit!")
            elif count_years > 0 and count_months == 0:
                print(f"You need {count_years} years to repay this credit!")
            elif count_years > 0 and count_months > 0:
                print(f"You need {count_years} years and {count_months} months to repay this credit!")

            overpayment = int(math.fabs(P - payment))
            print(f"Overpayment = {overpayment}")

        # User wants args.payment
        elif args.principal != None and args.periods != None and args.interest != None and args.payment is None:

            P = args.principal
            n = args.periods
            i = formula_i(args.interest)

            # formula for A
            A = math.ceil(P * (i * (1 + i) ** n) / ((1 + i) ** n - 1))

            payment = math.ceil(n * A)

            print(f"Your annuity payment = {A}!")

            overpayment = int(math.fabs(P - payment))
            print(f"Overpayment = {overpayment}")

        # User wants args.principal
        elif args.payment != None and args.periods != None and args.interest != None and args.principal is None:

            A = args.payment
            n = args.periods
            i = formula_i(args.interest)

            # formula for P
            P = math.floor(A / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))

            payment = math.ceil(n * A)

            print(f"Your credit principal = {P}!")

            overpayment = int(math.fabs(P - payment))
            print(f"Overpayment = {overpayment}")

    # Differrentiated payment
    elif args.type == "diff":

        arguments += 1 if args.type != None else arguments == arguments - 1
        arguments += 1 if args.principal != None else arguments == arguments - 1
        arguments += 1 if args.periods != None else arguments == arguments - 1
        arguments += 1 if args.payment != None else arguments == arguments - 1
        arguments += 1 if args.interest != None else arguments == arguments - 1

        if args.interest is None:
            print("Incorrect parameters")
        elif arguments != 4:
            print("Incorrect parameters")

        if args.principal != None and args.periods != None and args.interest != None:

            m = 0
            payment = 0
            P = args.principal
            n = args.periods
            i = formula_i(args.interest)

            for x in range(n):
                m += 1
                Dm = math.ceil(P / n + i * (P - (P * (m - 1) / n)))
                payment += Dm
                print(f"Month {m}: paid out {Dm}")

            overpayment = int(math.fabs(P - payment))
            print(f"Overpayment = {overpayment}")

    elif args.type is None:
        print("Incorrect parameters")