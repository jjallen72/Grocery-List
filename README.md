# Grocery-List

•	Summarize the project and what problem it was solving.
In this project, I needed to create a program that would read as input a file containing a list of grocery items and then display a menu to the user that would allow the user to view the information in different ways.  1) To view a list of unique items and the nubmer of times they appeared in the list, 2) to view one item (chosen by the user) as well as the number of times it appeared in the list and 3) to visually represent the list and the frequencies as a text-based histogram.

•	What did you do particularly well?
Particulary, I liked the way I formateed the column lenghts and made it so that each histogram line of asterisks started at the exact same horizontal level so that the entire histogram would be easier to read.

•	Where could you enhance your code? How would these improvements make your code more efficient, secure, and so on?
The code could be enhanced by not writing and reading to and from the frequency.dat file and instead just using the dictionary that held the frequencies to create the histogram.  This would add efficienty as it would cut the overhead costs of file input/output operations. 

•	Which pieces of the code did you find most challenging to write, and how did you overcome this? What tools or resources are you adding to your support network?
The piece of code I found most challenging was the portion in which I needed to keep track of the longest product name and then pass it around to each function through parameters and return values.  The tool I added to accomplish was making use of returning tuples.  

•	What skills from this project will be particularly transferable to other projects or course work?
I anticipate that the usage of dictionaries will be very useful in the future and will be easily transferable to other projects.  

•	How did you make this program maintainable, readable, and adaptable?
I made this program maintainable by using many comments and also breaking down the code into as small (but useful) chunks as possible so that if a change did need to be made, it would be easy to find the place where the change should occur, because the entire program was compartmentalized.  
