#Question 3
#Task 1
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def average_closing_price(stocks, stock_name):
    total_sum = sum(stock[2] for stock in stocks if stock[0] == stock_name)
    count = 0
    for stock in stocks:
        count += stock.count(stock_name)
    if count != 0:  
        average = total_sum/count
        print(f"The average closing cost is: ${average: .2f}.")
    else:
        print(f"{stock_name} is not in the list.")
    
average_closing_price(stock_data, "AAPL")
average_closing_price(stock_data, 123)

#Task 2
attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]

def event_attendees(attendees, event):
    attended = [guests for guests in attendees if guests[1].lower() == event.lower()]
    print(f'{event.title()} attendees: ')
    for guest in attended: 
        print(f"{guest[0]}")

def count_attendees(attendees, event):
    count = 0
    for x in attendees:
        count += x.count(event.title())
    print(f"There were {count} attendees to the {event.title()}.")

count_attendees(attendees, 'pYthon COnference')
            

event_attendees(attendees, 'python conference')