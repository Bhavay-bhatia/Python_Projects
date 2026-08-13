print("welcome to millionaire game \n You will get +$100 for every correct answer but game will end if you enter incorrect answer")

questions=[
    ["who is sharukh khan?","WWE Wrestler","Actor","Plumber","influencer",2],
    ["what is the capital of France?","Rome","Berlin","London","Paris",4],
    ["which planet is called as red planet?","Mars","Earth","Venus","Jupiter",1],
    ["which is the largest animal?","Elephant","Blue Whale","Giraffe","Shark",2],
    ["who wrote Romeo and Juliet?","Chalres Dickens","Jane Austen","William shakespeare","Homer",3],
    ["what is the square root of 256?","16","8","15","26",1],
    ["which country is known as the land of rising sun?","China","South korea","India","Japan",4],
    ["who painted the Mona Lisa?","Vincent Van Gogh","Leonardo da vinci","Pablo Picasso","Claude Monet",2],
    ["which is the fastest animal among these?","Cheetah","Lion","Ostrich","Horse",1],
    ["whihc ocean is the largest?","Atlantic Ocean","Indian Ocean","Artic Ocean","Pacific Ocean",2],
    ["what is the smallest country in the world?","vatican City","San Marino","Vietnam","monaco",4]
]
prize=0
for question in questions:
    print(question[0])
    print(f"1.{question[1]} \n 2.{question[2]} \n 3.{question[3]} \n 4.{question[4]}")

    # checking the answer 
    ans=int(input("enter the answer in number : "))
    if(question[5]==ans):
        print("WOW! Correct answer moving to next question")
        prize+=100
    else:
        print(f"Incorrect answer , correct answer is {question[5]}")
        break
print(f"you have won ${prize}")