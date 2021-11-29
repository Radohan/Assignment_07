#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# RadoslawHankiewicz, 2021-Nov-21, Updated File (functions added)
#------------------------------------------#

# -- DATA -- #

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


import pickle

# -- PROCESSING -- #

class DataProcessor:
    # DONE add functions for processing here

    @staticmethod
    def adding_function(dictionary, table, strID, strTitle, strArtist):
        
        """Function to add data to the table.

        Appends a new row/rows of data (dictionary) to the 2D table list. It registers data added by user (ID, Title, Artist).

        Args:
            dictionary: name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            A table.
        """
   
        try:
            intID = int(strID)
            dictionary = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
            table.append(dictionary)
            return table
        except Exception as e:
            print("The value entered is not an integer")
            print("Information about the error:")
            print(e)
            print(type(e))
            print(e.args)
            print(e.__doc__)
            print(e.__str__())
            
    @staticmethod
    def removing_function(table):
        
        """Function to remove data to the table.

        Deletes a row/rows of data frome the 2D table based on the ID indicated by user.

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            Information that the CD indicated by user was successfully deleted or that it couldn't be identified.
        """
        

        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del table[intRowNr]
                blnCDRemoved = True
                break
            if blnCDRemoved:
                print('The CD was removed')
            else:
                print('Could not find this CD!')
            
            

class FileProcessor:
    
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            table.clear()  # this clears existing data and allows to load data from file
            with open(file_name, "rb") as fileObj:
                table = pickle.load(fileObj)
            return table
            
        except Exception as e:
            print("The file doesn't exist. Please create the CDInventory.txt file.")
            print("Information about the error:")
            print(e)
            print(type(e))
            print(e.args)
            print(e.__doc__)
            print(e.__str__())

    @staticmethod
    def write_file(file_name, table):
        
        """Function to save data to the file.

        Saves data to the file.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """

        # DONE Add code here
        with open(file_name, "wb") as fileObj:
            pickle.dump(table, fileObj)
        
        
    @staticmethod
    def load_function(file_name, table):
            
        """Function to loda data from the file.

        Saves data to the file.

        Args:
        file_name (string): name of file used to read the data from
        table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
                Question if user wants to continue.If yes it returns saved data from the file.
        """
        
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            table = FileProcessor.read_file(file_name, table)
            IO.show_inventory(table)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(table)


# -- PRESENTATION (Input/Output) -- #

class IO:
    
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
            
        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # DONE add I/O functions as needed
    
    @staticmethod
    def user_input():
        
        """Function ebable user to add data about a new CD. It asks user for input (ID, Title, Artist).

        Args:
            None.

        Returns:
            strID, strTitle, strArtist.
        """

        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        input_result = strID, strTitle, strArtist
        return input_result

# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        FileProcessor.load_function(strFileName, lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # DONE move IO code into function
        # 3.3.2 Add item to the table
        # DONE move processing code into function
        strID, strTitle, strArtist = IO.user_input()
        DataProcessor.adding_function(dicRow, lstTbl, strID, strTitle, strArtist)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        # DONE move processing code into function
            DataProcessor.removing_function(lstTbl)
            IO.show_inventory(lstTbl)
        except Exception as e:
                    print("The value entered is not an integer")
                    print("Information about the error:")
                    print(e)
                    print(type(e))
                    print(e.args)
                    print(e.__doc__)
                    print(e.__str__())
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # DONE move processing code into function
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
