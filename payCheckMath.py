def calculate_paycheck():
    # Comprehensive state tax rates (approximate, adjust as needed)
    state_tax_rates = {
        'Alabama': 5.0, 'Alaska': 0.0, 'Arizona': 4.5, 'Arkansas': 5.9,
        'California': 9.3, 'Colorado': 4.4, 'Connecticut': 6.99, 'Delaware': 6.6,
        'Florida': 0.0, 'Georgia': 5.75, 'Hawaii': 8.25, 'Idaho': 6.0,
        'Illinois': 4.95, 'Indiana': 3.23, 'Iowa': 8.53, 'Kansas': 5.7,
        'Kentucky': 5.0, 'Louisiana': 4.25, 'Maine': 7.15, 'Maryland': 5.75,
        'Massachusetts': 5.0, 'Michigan': 4.25, 'Minnesota': 9.85, 
        'Mississippi': 5.0, 'Missouri': 5.4, 'Montana': 6.75, 'Nebraska': 6.84,
        'Nevada': 0.0, 'New Hampshire': 0.0, 'New Jersey': 10.75, 
        'New Mexico': 5.9, 'New York': 8.82, 'North Carolina': 4.75,
        'North Dakota': 2.9, 'Ohio': 3.99, 'Oklahoma': 5.0, 'Oregon': 9.9,
        'Pennsylvania': 3.07, 'Rhode Island': 5.99, 'South Carolina': 7.0,
        'South Dakota': 0.0, 'Tennessee': 0.0, 'Texas': 0.0, 'Utah': 4.95,
        'Vermont': 8.75, 'Virginia': 5.75, 'Washington': 0.0,
        'West Virginia': 6.5, 'Wisconsin': 7.65, 'Wyoming': 0.0,
        'District of Columbia': 8.5, 'Other': 5.0  # Default for unknown states
    }

    # Constants for federal taxes
    federal_tax_rate = 12.0  # Example flat federal tax rate
    medicare_tax_rate = 1.45  # Medicare tax rate
    social_security_tax_rate = 6.2  # Social Security tax rate
    standard_work_weeks = 40  # Number of work weeks in a year

    # Gather input
    print("Welcome to the Paycheck Calculator!")
    state = input("Enter your state: (First letter must be a capital letter) ").strip()
    pay_type = input("Are you paid hourly or salary? (hourly/salary): ").strip().lower()

    if pay_type == 'hourly':
        hourly_rate = float(input("Enter your hourly rate ($): "))
        hours_worked = float(input("Enter the number of hours worked: "))
        gross_pay = hourly_rate * hours_worked
    elif pay_type == 'salary':
        annual_salary = float(input("Enter your annual salary ($): "))
        hours_worked = (annual_salary / (40 * standard_work_weeks))  # Estimate hours worked weekly
        gross_pay = annual_salary / 24  # Bi-weekly paycheck
    else:
        print("Invalid pay type entered. Please restart the program.")
        return

    # Calculate taxes
    tax_rate = state_tax_rates.get(state, state_tax_rates['Other'])
    state_tax = (tax_rate / 100) * gross_pay
    federal_tax = (federal_tax_rate / 100) * gross_pay
    medicare_tax = (medicare_tax_rate / 100) * gross_pay
    social_security_tax = (social_security_tax_rate / 100) * gross_pay

    # Calculate net pay
    total_tax = state_tax + federal_tax + medicare_tax + social_security_tax
    net_pay = gross_pay - total_tax

    # Display results
    print("\nPaycheck Details:")
    print(f"State: {state}")
    print(f"Gross Pay (Bi-weekly): ${gross_pay:.2f}")
    if pay_type == 'salaried':
        print(f"Estimated Hours Worked (Bi-weekly): 80 hours")
    else:
        print(f"Hours Worked: {hours_worked:.2f} hours")
    print(f"State Tax ({tax_rate}%): ${state_tax:.2f}")
    print(f"Federal Tax (12%): ${federal_tax:.2f}")
    print(f"Medicare Tax (1.45%): ${medicare_tax:.2f}")
    print(f"Social Security Tax (6.2%): ${social_security_tax:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

# Run the program
if __name__ == "__main__":
    calculate_paycheck()
    