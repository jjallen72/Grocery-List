#This script was created by Janece Gates


#from venv import __main__


def loadfile():
    #open and read the input file
    f = open("CS210_Project_Three_Input_File.txt", "r")
    #f = open("C:\\Users\\Veteran\\Documents\\SNHU CLASSES\\Intro to C++\\CS210_Project_Three_Input_File.txt", "r")
    products = {}  # create a empty dictionary that will store the products and their frequencies
    longestLen = 0 # keep track of the longest product name for purposes of sizing the histogram column
    for line in f.readlines():
        # remove the newline from each line of the file
        line = line.strip()
        if len(line) > longestLen:
            longestLen = len(line)  # update the longest length variable as necessary
        if line in products.keys(): # check if the latest product name is already in the dictionary and update accordingly
            products[line] += 1
        else:
            products[line] = 1
    f.close()
    return products, longestLen


def displayMenu():
    #give choice variable an initial value
    choice = '0'

    #repeat the menu until the user chooses a valid option
    while not  ( '1' <= choice <= '4'):
        print("1.  Display frequencies of all itmes")
        print("2.  Display frequency of a single item")
        print("3.  Display histogram of items and frequencies ")
        print("4.  Quit.")
        choice = input("Enter you choice:")

    return int(choice)

def respondToUser(choice, products_dict, col_min_width):
    if choice == 1:
        # display all frequencies
        f = open("frequency.dat", "w")

        # iterate through the keys of the products dictionary
        for prod in products_dict.keys():
            # print out each product along with the corresponding frequency .  Also add to file
            print(('{0:>' + str(col_min_width) + '}').format(prod) + '|', products_dict[prod])
            f.write(('{0:>' + str(col_min_width) + '}').format(prod) + '|'+ str(products_dict[prod]) + "\n")
        f.close()

    if choice == 2:
        # ask user for which product they want to see data for
        prodToReport = input("for which product do you want to see frequency info for?")

        #check if user response is in the dictionary
        if prodToReport in products_dict.keys():
            print(prodToReport, products_dict[prodToReport])
        else:
            print(prodToReport + " was not found.")

    if choice == 3:
        #open and read the file of frequencies
        f = open("frequency.dat", "r")
        for line in f.readlines():
            line = line.split("|")
            prod = line[0].strip()  # extract the product name
            freq = int(line[1])     # extract the product frequency
            hist_line = "*"*freq    # create the histogram bar that corresponds to the frequency
            print(('{0:<' + str(col_min_width) + '}').format(prod) + '|' + hist_line)


#if "__name__" == __main__:
def main():
    # load in the information from the file
    prod_dict, longestLen = loadfile()
    while True:
        # display the menu to the user and get their choice
        user_choice = displayMenu()

        #check if user chose to exit program
        if user_choice == 4:
            break
        else:
            # do appropriate action based on user choice
            respondToUser(user_choice, prod_dict, longestLen)

main()


'''
1.  The benefit of using C++ over python is that C++ is a much granular language which means I am
able to exercise more control over the features and more effectively handle errors and formatting (Note,
these can also be done in python too, however).  The granularity of C++ is a double-edged sword, because 
despite the advantages is offers, it also mean that certain tasks that Python can accomplish very quickly
will take much more time.  

2.  One big benefit of Python over C++ is the ease of which it can process large files quickly.  The 
python I/O library offers many tools to efficiently do this, however this is a bit more cumberson in 
C++.  One drawback is that if you'd like to fine-tune certain details in Python, the process becomes 
a bit complicated.  

3.  During this project, I exclusively used Python because after setting up the C++/Python interface 
in Visual Studio, the executable file corresponding to my code that was supposed to be created upon
successful compilation was not being generated.   
'''