def give_options(x,y,z):
    print("a):", x)
    print("b):", y)
    print("c):", z)
    
print("Hello! Welcome to my Quiz" "\n" "All Questions carries 10 marks each")
ans = input("Are you ready to answer (yes/no): ")
a ="Note: wrtie answers! do not write option."
score = 0
total_questions = 4

correct_ans =["python", "steve jobs", "artificial intelligence", "bitcoin"]

if ans.lower() == "yes":
    print(a)
    print("Question- What is the best Programming Language? ")
    give_options("Python", "C", "Java" )
    ans=input("> ")
    if ans.lower() == correct_ans[0]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- Who is the Founder of Apple Inc? ")
    give_options("Mark Zuckerberg", "Warren Buffet", "Steve jobs")
    ans = input("> ")
    if ans.lower() == correct_ans[1]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What can make the machine intelligent? ")
    give_options("Data Science", "Artificial Intelligence", "Digital Marketing")
    ans = input("> ")
    if ans.lower() == correct_ans[2]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")
    print(a)
    print("Question- What is more volatile investment? ")
    give_options("Share Capital", "Mutual Funds", "Bitcoin")
    ans = input("> ")
    if ans.lower() == correct_ans[3]:
        score=score+1
        print("Correct")
    else:
        print("Incorrect")

i = score*10
if i < 30:
    print("Low, your score ",i,"/ 40 better luck next time.")
elif i ==30:
    print("High! you scored ",i,"/ 40 you are ok.")
else:
    print("Congratulations! it's a perfect ",i,"/ 40 you are Perfect.")
    