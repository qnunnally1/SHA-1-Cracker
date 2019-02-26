# SHA-1-Cracker
### Quantonio Nunnally

## Installation
To use the SHA-1 Cracker, first download this repository by clicking 'Download' or clone this repository to a directory of your choosing in your local environment. Remember this location, as you will have to navigate here to further run the program.

## Running SHA-1 Cracker
To run this program, first, be sure to have Python 2.7 installed on your operating system. Any version higher will not be able to run this program. After verifying that Python 2.7 is installed on your device, use your terminal to navigate to the directory where the program was downloaded. Once there, make sure you have two files in that directory: 'cracker.py' and '10-million-password-list-top-1000000.txt'. If your device is a Mac, use 'ls'. If your device is Windows, use 'dir'. The first file contains the code used to crack hashes. The latter is used by the code to search through common passwords. 

Your terminal will be where you input your hash to be cracked. While in the same directory as the two previously mentioned files, type in 'python cracker.py' and append to this the hash you want to solve for. 

### Example
*python cracker.py 34302959e138917ce9339c0b30ec50e650ce6b40*


Let's begin with a few hashes!

### A. Testing Program Hash
* Input *python cracker.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3*
* The solution should resemble: **The cracked hash is: letmein. This took 16 guesses.**
* The elapsed time was **1.863s**

### B. Medium Hacker Hash
* Input *python cracker.py 801cdea58224c921c21fd2b183ff28ffa910ce31*
* The solution should resemble: **The cracked hash is: vjhtrhsvdctcegth. This took 999968 guesses.**
* The elapsed time was **4.882s**

### C. Leet Hacker Hash
* Input *python cracker.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1*
* The solution should resemble: **The cracked hash is: slayerharib. This took 546155 guesses.**
* The elapsed time was **6.111s**

### D. Graduate Student
* Input *python cracker.py 34302959e138917ce9339c0b30ec50e650ce6b40*
* The solution should resemble: **No results found for your hash.**
* The elapsed time was **11.804s**
