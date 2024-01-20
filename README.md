# cuckoo_hashing
Cuckoo Hashing Algorithm Visualization
**CSE4094 Advanced Data Structures**




1-	How to execute: 
Run the program from your IDE and black screen will be appear. In the terminal you must enter table size and table number. After you entered inputs tables will be drawn and screnn will be meaningful (Cuckoo hashing program). You will see tables and buttons (Insert, delete, search, exit) and you must enter the number in the white textbox and click the buttons. After each insertion load factor and collision counter printed in the terminal.
Important Note: After each operation you must delete the number in the textbox otherwise it takes still written number. 
 
Pygame Window


2-	Hash Functions: 
In this project we used 5 hash functions:
a-	Hash1() (Division Method) : This function simply takes the modulus of the input value with the number of slots in the table. It is simple to compute and works well when the number of slots is a prime number.  

b-	Hash2() (Multiplication Method):  This function uses the multiplication method, which is a well-known technique for generating hash functions. The value of A is chosen such that it gives a good distribution of values.  

c-	Hash3() (Universal hashing): This function uses a technique called universal hashing which provides a good distribution of values and a low number of collisions.  


d-	Hash4() (Jenkins Hash): The Jenkins Hash is a well-known, relatively simple and efficient hash function. It uses bitwise operations and addition to combine the input value with a set of fixed values, producing a well-distributed output.  
e-	Hash5() (Bit shifting): This function uses bit shifting, it is relatively efficient and works well when the input values are large integers.
 
