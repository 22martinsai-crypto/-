username = "   "
password = "   "
score = 0
count = 0
username=input("Enter your username:")
password=input("Enter your password:")
while password!= "124378":
    password=input("Enter your password again!!")
    count=count+1
    print("You have entered the wrong password",count,"times")
if username == "Youzernaim" and password == "124378":
    print("You have successfully logged in!")
    answer1 = input("How many times have Chelsea won the UCL? \na. 0 \nb. 1 \nc. 2 \nd. 3 \nAnswer:")
    if answer1 == "c" or answer1 == "2":
        score+=1
        print("Well done you got it correct")
        print("score: ", score)
        print("\n")
    answer2 = input("Who was the last Chelsea player to win the Premier League golden boot? \na. England \nb. Poland \nc. Spain \nAnswer:")
    if answer2 == "c" or answer2 == "Spain":
        score+=1
        print("Well done you got it correct")
        print("score: ",score)
        print("\n")
    answer3 = input("What team do I support? \na. Spurs \nb. Arsenal \nc. Sheffield United \nAnswer:")
    if answer3 == "a" or answer3 == "Spurs":
        score+=1
        print("Well done you got it correct")
        print("score: ",score)
        print("\n")
    answer4 = input("How many UCLS do Chelsea FC have? \na. 2 \nb. 6 \nc. 10 \nAnswer:")
    if answer4 == "a" or answer4  == "2":
        score+=1
        print("Well done you got it correct")
        print("score: ",score)
        print("\n")
    answer5 = input("Are Liverpool going to win the Premier League 2025? \na. Yes \nb. No \nc. Maybe \nAnswer:")
    if answer5 == "b" or answer5  == "No":
        score+=1
        print("Well done you got it correct")
        print("score: ",score)
        print("\n")
    answer6 = input("Who won the World Cup 1974? \na. France \nb. Germany \nc. West Germany \nAnswer:")
    if answer6 == "c" or answer5  == "West Germany":
        score+=1
        print("Well done you got it correct")
        print("score: ",score)
        print("\n")
    answer7 = input("When was the first champions league game held? \na. 2005/06 \nb. 1955/56 \nc. 2034/35 \nAnswer:")
    if answer7 == "b" or answer7 == "1955/56"
        score+=1
        print("Well done you got it correct")
        print("score: ",score)
        print("\n")
