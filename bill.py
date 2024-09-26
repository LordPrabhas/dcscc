def calculate_bill(previous_reading, current_reading, rate_per_unit):
    # Calculate the difference in readings
    units_consumed = current_reading - previous_reading
    # Calculate the bill
    bill_amount = units_consumed * rate_per_unit
    return units_consumed, bill_amount

def main():
    # Get user input for previous and current readings
    previous_reading = float(input("Enter previous meter reading (in kWh): "))
    current_reading = float(input("Enter current meter reading (in kWh): "))
    
    # Define the rate per unit (you can change this value as needed)
    rate_per_unit = 0.12  # Example rate in dollars per kWh
    
    # Validate the readings
    if current_reading < previous_reading:
        print("Error: Current reading cannot be less than previous reading.")
        return
    
    # Calculate the bill
    units_consumed, bill_amount = calculate_bill(previous_reading, current_reading, rate_per_unit)
    
    # Display the results
    print(f"\nUnits Consumed: {units_consumed} kWh")
    print(f"Electricity Bill: ${bill_amount:.2f}")

if __name__ == "__main__":
    main()
