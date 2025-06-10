from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    
    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    try:
        # Ask user for number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Add days using timedelta
        future_date = current_date + timedelta(days=days_to_add)
        
        # Format and display the future date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    
    except ValueError:
        print("Please enter a valid integer.")

# ---- Main Execution ----
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
