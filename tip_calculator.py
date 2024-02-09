def calculate_tip(total_bill, num_people, tip_percentage=15):
    try: 
        total_bill = float(total_bill)
        num_people = int(num_people)
        tip_percentage = float(tip_percentage)
        tip_amount = (total_bill * (tip_percentage / 100)) / num_people
        return round(tip_amount, 2)
    except ValueError as e:
        raise ValueError("Invalid input. Please enter numeric values for bill amount, number of people, and tip percentage.") from e