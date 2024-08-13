# SE-DL-Lab Practicals

## Practical 1 - 1.py
Hey there! In this assignment, you will be writing a Python program to store marks scored in the subject "Fundamental of Data Structure" by N students in the class. You will also write functions to compute the following:

Average Score of the Class
Highest and Lowest Scores of the Class
Count of Students Absent for the Test
Display Marks with the Highest Frequency
Detailed Instructions
To successfully complete this assignment, follow the steps below:

Input Collection:

Take the marks of at least 10 students as input.
Use a list to store the marks. You can create an empty list and then use a loop to input the marks of each student.
Average Score Calculation:

Write a function to calculate the average score of the class. You can do this by summing up all the marks and then dividing by the total number of students.
Highest and Lowest Scores:

Create a function to find the highest and lowest scores in the class. You can do this by iterating through the list of marks and keeping track of the highest and lowest scores.
Count of Absent Students:

Write a function to count the number of students who were absent for the test. You can do this by checking for any marks that indicate absence (e.g., -1).
Display Marks with Highest Frequency:

Implement a function to display the mark(s) with the highest frequency in the class. You can achieve this by using a dictionary to count the frequency of each mark. (or Using Mode function)

## Practical 2 - 2.py
In this assignment, you will write a Python program using functions to compute various aspects of sports participation among the students in the second year computer engineering class. You will need to consider the groups A, B, and C, where students play cricket, badminton, and football respectively.

Task Overview
Your program should be able to compute the following:

List of students who play both cricket and badminton
List of students who play either cricket or badminton but not both
Number of students who play neither cricket nor badminton
Number of students who play cricket and football but not badminton
Number of students who do not play any game
List of students who play at least one game
List of students who play all three games
Writing the Python Program
To accomplish this task, you will need to create functions for each of the computations listed above. Here are some guidelines to help you complete the assignment:

you have to take following inputs: Total number of students in class, List of students playing Cricket, List of students playing Badminton, List of students playing Football.

1. List of students who play both cricket and badminton
You will need to create a function that takes the lists of students playing cricket and badminton as input and returns a list of students who play both sports.

2. List of students who play either cricket or badminton but not both
Create a function that takes the lists of students playing cricket and badminton as input and returns a list of students who play either cricket or badminton but not both.

3. Number of students who play neither cricket nor badminton
Develop a function that takes the lists of students playing cricket and badminton as input and returns the number of students who play neither cricket nor badminton.

4. Number of students who play cricket and football but not badminton
Create a function that takes the lists of students playing cricket and football as input and returns the number of students who play cricket and football but not badminton.

5. Number of students who do not play any game
You will need to create a function that takes the lists of students playing cricket, badminton, and football as input and returns the number of students who do not play any game.

6. List of students who play at least one game
Develop a function that takes the lists of students playing cricket, badminton, and football as input and returns a list of students who play at least one game.

7. List of students who play all three games
Create a function that takes the lists of students playing cricket, badminton, and football as input and returns a list of students who play all three games.

Remember to avoid duplicate entries while realizing the groups and refrain from using the SET built-in functions as per the instructions.

By following these guidelines, you will be able to create a comprehensive Python program to compute the various aspects of sports participation among the students in the second year computer engineering class.

## Practical 3 - 3.py,3-new.py
In this assignment, you will write a Python program to perform various operations on matrices. You will check whether a given matrix is upper triangular, compute the summation of diagonal elements, compute the transpose of the matrix, add and multiply two matrices, determine the location of a saddle point, and check if the matrix is a magic square.



Instructions
Check Upper Triangular Matrix

You will start by writing a function to check whether a given matrix is an upper triangular matrix or not. An upper triangular matrix is a square matrix in which all the elements below the main diagonal are zero.
To check if a matrix is upper triangular, you will need to iterate through the elements of the matrix and compare their positions to determine if they meet the criteria for an upper triangular matrix.
Compute Summation of Diagonal Elements

Next, you will implement a function to compute the summation of the diagonal elements of a matrix. The diagonal elements of a matrix are the elements where the row number is equal to the column number.
You will need to iterate through the diagonal elements and calculate their sum.
Compute Transpose of Matrix

You will then write a function to compute the transpose of a matrix. The transpose of a matrix is obtained by flipping the matrix over its main diagonal, which means interchanging the row and column indices of the matrix.
You will need to create a new matrix to store the transposed elements and populate it by iterating through the original matrix.
Add and Multiply Two Matrices

After that, you will implement functions to add and multiply two matrices. Matrix addition and multiplication follow specific rules, and you will need to iterate through the matrices to perform these operations.
Determine Saddle Point

You will then write a function to determine the location of a saddle point in a matrix, if one exists. A saddle point in an m x n matrix is an entry a[i][j] that is the smallest value in row i and the largest value in column j.
To find the saddle point, you will need to compare the elements in each row and column to identify the saddle point based on the given criteria.
Check for Magic Square

Finally, you will create a function to check if the given matrix is a magic square. A magic square is an n x n matrix of the integers 1 to n^2 such that the sum of each row, column, and diagonal is the same.
You will need to calculate the sum of each row, column, and diagonal, and then compare these sums to determine if the matrix is a magic square.

## Practical 5 - 5.py
a) Write a Python program to store roll numbers of student in array who attended training program in random order. Write function for searching whether particular student attended training program or not using linear search and sentinel search.

b) Write a Python program to store roll numbers of student array who attended training program in sorted order. Write function for searching whether particular student attended training program or not using binary search and Fibonacci search.

## Practical 7 - 7.py,8.py
Write a python program to represent polynomials using One-D array  and 2-D array  and perform operations. Write function
a) To input and output polynomials represented as bmxem+ bm-1xem-1 +….. +b0xe0.
b) Evaluates a polynomial at given value of x
c) Add two polynomials
d) Multiplies two polynomials

## Practical 8 - 9.py
Introduction
In this assignment, you will write a Python program to work with sparse matrix representation and perform various operations on it. The operations include finding the transpose, fast transpose, and addition of two matrices. There is also an optional task to implement the multiplication of two sparse matrices.

Sparse Matrix Representation
A sparse matrix is a matrix in which most of the elements are zero. Instead of storing all the elements, we only store the non-zero elements along with their row and column indices. This helps in saving memory and computational resources.

To represent a sparse matrix, you can use a list of lists . Each non-zero element will be represented by its value and its corresponding row and column indices.

Task 1: Simple Transpose of a Sparse Matrix
The transpose of a matrix is obtained by interchanging the rows and columns. In the context of a sparse matrix, the transpose operation involves swapping the row and column indices of the non-zero elements.

To complete this task, you will need to write a function that takes a sparse matrix as input and returns its transpose.

Task 2: Fast Transpose of a Sparse Matrix
The fast transpose is an optimized version of the transpose operation for a sparse matrix. It involves finding the number of non-zero elements in each column of the original matrix and then using this information to efficiently construct the transpose.

For this task, you will implement a function to perform the fast transpose operation on a given sparse matrix.

Task 3: Addition of Two Sparse Matrices
Adding two sparse matrices involves adding the corresponding elements of the matrices. If a cell in one matrix is empty (zero), the value from the other matrix is used.

You will write a function to add two given sparse matrices and return the resulting matrix.
