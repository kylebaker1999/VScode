import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print the current
# day of the week and the current time.
#print(f"{current_date_and_time:%A %I:%M %p}")
NAME_INDEX = 0
QUANTITY_INDEX = 1
PRODUCT_CODE_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def main():
    try:
        mydict = read_dict("products.csv", 0)

        print("Items")
        discount = 0.1
        with open("request.csv", 'rt') as requested:
            reader = csv.reader(requested)
            next(reader)
        
            numbers_item = 0
            subtotal = 0.0
            taxes = .06
            total = 0.0

            for row_list in reader:
                mainvar = row_list[0]
                product_quantity = int(row_list[1])
                row_list = mydict[mainvar]
                description = row_list[1]
                price = float(row_list[2])

                numbers_item += product_quantity
                
                subtotal += (price*product_quantity)

                amttax = taxes * subtotal
                total = amttax + subtotal
                
                print(f"{description}: {product_quantity} @ ${price}")
    
            print(f"Amount of Items: {numbers_item}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Tax: ${amttax:.2f}")
            print(f"Total: ${total:.2f}")
            
        
        print("Thank'sfor visiting My Awesome Store!!!")
        print(f"{current_date_and_time:%a %b %I:%M %p}")
        
        
 
            
    except FileNotFoundError as not_found_err:
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"{mydict} does not exist.")
        print("Run again with the name of a legible file.")
        
    except PermissionError as perm_err:
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"Cant read {mydict}.")
        print("Run again with the name of a legible file.")
        
    except KeyError as error:
        print(type(error).__name__, error, sep=": ")
        print(f"Error: unknown product ID in the request.csv file '{mainvar}'")
        

        

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    return_dictionary = {}
    
    with open(filename, 'rt') as mydict:
        reader = csv.reader(mydict)
        #This skips to the row '1'  and not look at the row '0'
        next(reader)
        
        for row in reader:
            return_dictionary[row[0]] = row
            
    return return_dictionary

if __name__ == '__main__':
    main()
























