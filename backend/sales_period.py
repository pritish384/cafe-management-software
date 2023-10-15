from datetime import datetime, date ,timedelta
def sales_period():
    # Calculate the first day of the current month
    current_date = date.today()
    first_day = current_date.replace(day=1)

    # Calculate the last day of the current month
    if current_date.month == 12:
        next_month = current_date.replace(year=current_date.year + 1, month=1, day=1)
        last_day = next_month - timedelta(days=1)
    else:
        next_month = current_date.replace(month=current_date.month + 1, day=1)
        last_day = next_month - timedelta(days=1)

    # Format the dates as strings
    first_day_str = first_day.strftime("%d %b %Y")
    last_day_str = last_day.strftime("%d %b %Y")
    
    sales_period = f"{first_day_str} - {last_day_str}"


    return sales_period