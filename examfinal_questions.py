# this python code is used to generate practice questions for final
# must have access to lecture notes 1 to 14 to review questions

def q1(): # example question
    print ("Question 1 ch 11 q 5")
    print ("Given the following string literal, which can break the string literal into a Python list of characters?")
    print ("s = \"cash\"")
    
def randomquestion():
    import random as q

    for i in range (1, 8):
        ch = q.randint(11,14)
        qn = q.randint(1,10)
        print ( "practice question", i, "chapter", ch, "question", qn)
        
    for i in range (8, 11):
        print ( "practice question", i, "chapter", q.randint(1,10), "question", q.randint(1,10) )
        
def main():
    print ( "set 1" )
    randomquestion()
    q1()

if __name__=="__main__":
    main()
    
''' # sample output
set 1
practice question 1 chapter 11 question 5
practice question 2 chapter 11 question 6
practice question 3 chapter 12 question 1
practice question 4 chapter 13 question 5
practice question 5 chapter 13 question 5
practice question 6 chapter 11 question 7
practice question 7 chapter 14 question 6
practice question 8 chapter 3 question 10
practice question 9 chapter 10 question 5
practice question 10 chapter 3 question 7
Question 1
Given the following string literal, which can break the string literal into a Python list of  characters?
s = "cash"
'''
