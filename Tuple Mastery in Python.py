#Question 1
#Task 1
list_of_tuple = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
def lists_itinerary(input_list):
    for index, itinerary in enumerate(input_list):
        print(f"Itinerary {index + 1}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}.")



lists_itinerary(list_of_tuple)
