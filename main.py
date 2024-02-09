# main.py

from tip_calculator import calculate_tip

def main():
    print("Welcome to Tip Calculator")
    total_bill = input("Enter the total bill amount: ")
    num_people = input("Enter the number of people splitting the bill: ")
    tip_percentage = input("Enter tip percentage (default is 15%): ")
    tip_percentage = tip_percentage or 15
    tip_amount = calculate_tip(total_bill, num_people, tip_percentage)
    print(f"Each person should pay: {tip_amount}")

if __name__ == "__main__":
    main()