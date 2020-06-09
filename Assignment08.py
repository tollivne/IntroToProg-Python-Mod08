# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# N. Tolliver,6.3.2020, Created script from Assignment 6
# N. Tolliver, 6.3.2020 Changed "Task" to "Name"; Changed "Priority" to "Price"
# N. Tolliver, 6.3.2020 Changed "lstTable" to "lstOfProductObjects"
# N. Tolliver, 6.3.2020 Removed code that removes an item from the list
# N. Tolliver, 6.3.2020 Renumbered menu items
# N. Tolliver, 6.3.2020 Removed option to reload data from file and renumbered menu
# N. Tolliver, 6.4.2020 Added definitions of product name and product price classes
# N. Tolliver, 6.7.2020 Added Error handling
# N. Tolliver 6.7.2020 Converted from reading & writing dictionaries to lists
# N. Tolliver, 6.7.2020 Converted from lists of data to lists of products
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
import sys
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    product_name(self) -> Product name in title case
    def product_name(self, value: str)
    def product_price(self): O=-> Produce price in floating point
    def product_price(self, value: float):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
       N. Tolliver, 6.6.2020, Added getter & setter code for product name & product price
    """

    # -- Fields --

    product_name = ""
    product_price = 0.0

    # -- Constructor --

    def __init__(self, product_name: str, product_price: float):
        """ Set name and price of a new object """
        # -- Attributes --
        try:
            self.product_name = str(product_name)
            self.product_price = float(product_price)
        except Exception as e:
            raise Exception ("Error setting initial values: \n" + str(e))

    # TODO: Add Code to the Product class

        # -- Properties --
        # Product Name
        @property # DON'T USE NAME for this directive!
        def product_name(self): # (getter or accessor)
            return str(self.__product_name).title() # Title case

        @product_name.setter # The NAME MUST MATCH the property's!
        def product_name(self, value: str): # (setter or mutator)
            if str(value).isnumeric()== False:
                self.__product_name = value
            else:
                raise Exception("Names cannot be numbers")

        # Product Price
        @property  # DON'T USE NAME for this directive!
        def product_price(self):  # (getter or accessor)
            return float(self.__product_price)  # cast to float

        @product_price.setter  # The NAME MUST MATCH the property's!
        def product_price(self, value: float):  # (setter or mutator)
            if str(value).isnumeric():
                self.__product_price = float(value)
            else:
                raise Exception("Prices must be numbers")

        # -- Methods --

    def __str__(self):
        """ Converts product name and price into aa comma separated string for writing to file
        :param produce_name string attribute
        :param produce_price floating point attribute to be converted to string
        """
        return self.product_name + "," + str(self.product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

        add_data_to_list (product, price, list_of_rows)

    changelog: (When,Who,What)
        N. Tolliver, 6.6.2020 Added code for all three methods

    """
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """
        Desc - Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows, Status
        """
        try:
            file = open(file_name, "r")
        except FileNotFoundError as e:
            print("Please make sure the file by the name of : " + file_name + " exists!")
            print("If using the CMD window, change directory to the folder you're working in "
                 "by typing the following command cd c:\_Name of Path")
            sys.exit()

        for line in file:
            product_name, product_price = line.split(",")
            row = Product(product_name, float(product_price))
            list_of_product_objects.append(row)
        file.close()
        return list_of_product_objects, "Data was read from file!"

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ This function writes the product list to a text file
        :param: File Name, Product List
        :return: Product List, Status
        """
        try:
            objFile = open(file_name, "w")

        except Exception as e:
            print("Error Writing to File")

        for row in list_of_product_objects:  # Write each product to the file
            objFile.write(str(row) + "\n") # calls __str__()
            print(str(row))
        objFile.close()
        return list_of_product_objects, "Data Saved to File!"

    @staticmethod
    def add_data_to_list (product_object, list_of_product_objects):
        """ This function adds a Product Name and Price to the Table
        param: Product Name and Price
        return: Updated list Table, Status
        """
        # row = [product, price]
        list_of_product_objects.append(product_object)  # Add the new row to the list/table
        return list_of_product_objects, "Product has been added!"

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    class FileProcessor:
        """Processes data to and from a file and a list of product objects:

        methods:
            print_menu_products:
            input_menu_choice: -> (menu choice)
            print_current_products_in_list(list_of_rows):
            input_new_product_and_price: ->  (product name and product price)
            input_press_to_continue(optional_message)
            input_yes_no_choice(message): -> (y or n answer)

        changelog: (When,Who,What)
            N. Tolliver, 6.6.2020 Added code for all static methods

        """
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_products():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new item.
        2) Save Data to File
        3) Display Current Data
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_products_in_list(list_of_product_objects):
        """ Shows the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The products items are: *******")
        for product_object in list_of_product_objects:
            print(product_object.product_name + " $" + str(product_object.product_price))
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_price ():
        """ This function prompts the user to enter the product & price
        param: none
        return: Product Name & Product price
        """
        objP1 = Product("", 0.0) # Create new object instance
        objP1.product_name = str(input("What is the product name? - ")).strip()  # Get product from user
        if objP1.product_name.isnumeric():
            raise Exception("Product names cannot be numbers")
        objP1.product_price = str(input("What is the price? - ")).strip()  # Get price from user
        if objP1.product_price.isnumeric()== False:
            raise Exception("Price has to be a number")
        print()  # Add an extra line for looks
        return(objP1)

    @staticmethod
    def input_press_to_continue(optional_message):
        """ Pause the program and display a message before continuing
        param: optional_message:  An optional message to display to the user
        return: nothing
        """
        print(optional_message)
        input("Press the [Enter] key to return to menu.")

    @staticmethod
    def input_yes_no_choice(message):
        """  Get a yes or no choice from the user
             param: Question to be asked of the user
             return: y or n answer
        """
        return str(input(message)).strip().lower()

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts

lstOfProductObjects, strStatus = FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

# Show user a menu of options
try:
    while(True):
        # Step 2 - Display a menu of choices to the user

        IO.print_menu_products()  # Shows menu

    # Get user's menu option choice

        strChoice = IO.input_menu_choice()  # Get menu option

        # Let user add data to the list of product objects
        if(strChoice.strip() == '1'): # Add a new product

            # Ask user for new product and price

            objP1 = IO.input_new_product_and_price()
            lstOfProductObjects, strStatus = FileProcessor.add_data_to_list(objP1, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
            continue  # to show the menu

        # let user save current data to file and exit program

        elif(strChoice == '2'):

            # Show the current items in the table
            IO.print_current_products_in_list(lstOfProductObjects)  # Show current data in the list/table

           # Ask if user if they want save that data
            if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

                lstOfProductObjects, strStatus = FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
                IO.input_press_to_continue(strStatus)

            else:  # Let the user know the data was not saved

                IO.input_press_to_continue("New data was NOT Saved, but previous data still exists!")

            continue  # to show the menu

        elif (strChoice == '3'):
            IO.print_current_products_in_list(lstOfProductObjects)  # Show current data in the list/table
            IO.input_press_to_continue("Data has been displayed")
            continue

        # Step 3.4 - Exit the program
        elif (strChoice == '4'):
            print("Goodbye")
            break  # and Exit

        else: print("Choice Must be 1, 2, 3, or 4")

#    Main Body of Script  ---------------------------------------------------- #

except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
