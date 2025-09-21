questions = [
    [
        "capital of india?","mumbai","delhi","new delhi","kolkata",3
    ],
     [
        "capital of india?","mumbai","delhi","new delhi","kolkata",3
    ],
     [
        "capital of india?","mumbai","delhi","new delhi","kolkata",3
    ],
     [
        "capital of india?","mumbai","delhi","new delhi","kolkata",3
    ],
     [
        "capital of india?","mumbai","delhi","new delhi","kolkata",3
    ],
     [
        "capital of india?","mumbai","delhi","new delhi","kolkata",3
    ],
     [
        "capital of india?","mumbai","delhi","new delhi","kolkata",3
    ],
    
]
levels = [1000,2000,3000,5000,10000,20000,50000]
money =0
for i in range(len(questions)):
    print(f"for Rs.{levels[i]}")
    print(questions[i][0])
    print("1.",questions[i][1])
    print("2.",questions[i][2])
    print("3.",questions[i][3])
    print("4.",questions[i][4])
    ans = int(input("enter your answer:"))
    if ans == questions[i][5]:
        money = levels[i]
        print(f"your answer is correct and you won Rs.{money}")
    else:
        print("your answer is wrong")
        break
    