def calculate_total_money():
    """Prompts the user for coin counts and calculates the total amount."""
    print("Please enter the count for each coin denomination:")
    try:
        count_10 = int(input("Rs 10 coins: "))
        count_5 = int(input("Rs 5 coins: "))
        count_2 = int(input("Rs 2 coins: "))
        count_1 = int(input("Rs 1 coins: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers.")
        return
    total_amount = (count_10 * 10) + (count_5 * 5) + (count_2 * 2) + (count_1 * 1)
    
    print(f"\nThe total amount of money in the piggy bank is Rs {total_amount}.")
if __name__ == "__main__":
    calculate_total_money()
