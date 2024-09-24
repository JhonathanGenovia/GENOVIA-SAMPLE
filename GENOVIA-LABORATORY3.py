def check_loan_eligibility():
    
        print("Welcome To Bank")
        # Input: Monthly salary and loan amount requested
        monthly_salary = float(input("Enter your monthly salary: "))
        loan_amount = float(input("Enter the loan amount you are requesting: "))
        
        # Eligibility criteria
        min_salary = 30000
        max_loan = 10 * monthly_salary
        
        # Determine eligibility
        if monthly_salary < min_salary:
            print("You are not qualified for a loan because your salary is to low.")
        if loan_amount > max_loan:
            print(f"You are not qualifed for a loan because the requested amount exceeds the maximum allowed of {max_loan:.2f}.")
        else:
            # If eligible, ask for payment duration and calculate total amount with interest
            months_to_pay = int(input("How many months do you want to pay the loan over? "))
            total_amount_with_interest = loan_amount * 1.10  # Adding 10% interest
            
            # Calculate monthly payment
            monthly_payment = total_amount_with_interest / months_to_pay
            
            print(f"You are approved for the loan!")
            print(f"Total amount to be paid with interest: {total_amount_with_interest:.2f}")
            print(f"Monthly payment over {months_to_pay} months: {monthly_payment:.2f}")


# Run the loan eligibility check
check_loan_eligibility()