from db.database_config import *
import datetime

def get_order_id():
    
    latest_order = active_orders.find_one(sort=[("order_id", -1)])
    if latest_order == None:
        order_id = 1
    else:
        order_id = latest_order['order_id'] + 1

    return order_id

def DateTime():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%A, %d %B %Y | %I:%M %p")
    return formatted_datetime



def initiate_order(order_type , order_guests , table_number):
    order_id = get_order_id()
    date = DateTime()

    document = {
        "dateTime": date,
        "order_id": order_id,
        "order_type": order_type,
        "order_status": "Preparing",
        "order_guests": order_guests,
        "table_number": table_number,
    }
    active_orders.insert_one(document)


    return order_id