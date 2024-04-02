#Question 5
catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

def combined_catalog(catalog1, catalog2):
    catalog = catalog1 + catalog2
    print(catalog)
    
combined_catalog(catalog1, catalog2)