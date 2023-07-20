"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #7 - X’s and O’s (xo.py)


Author: Andrew Scott White

Difficulty Level: 5/10

Prompt: Jonas and Shraddha are playing a card game, 
but Jonas keeps cheating by drawing extra cards. Shraddha
bought a device that tracks how many cards are drawn and who took them. 
She has asked you to write a script to ensure he isn’t cheating. The device
stores Jonas’ draws as X and Shraddha’s as O. 

Create a Python function that accepts a string. This 
function should count the number of Xs and the number of Os in the string.
It should then return a boolean value of either True or False. If the count of
Xs and Os are equal, then the function should return True. Otherwise, the function 
should return False.

Test Cases:
Input: XXXO Output: False

Input: XXXOOO Output: True

Input: xO Output: False

"""


class Solution:
    def count_XO(self, string):
            #type string: string
            #return type: boolean
            
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            return string.count("O") == string.count("X")
                
def main():
    input1=input()
    tc1 = Solution()
    ans = tc1.count_XO(input1)
    print(ans)

if __name__ == "__main__":
    main()
    