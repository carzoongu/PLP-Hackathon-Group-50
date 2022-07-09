#Storing career options in a list
career_options = []
while True:
    career = input("Enter the career: ")
    career_options.append(career)
    no_of_careers= input("Want to stop? if yes press yes if no press any other key: ")
    if no_of_careers.lower() == "yes":
        break
    print(career_options)
        
#Storing Career Questions
career_questions = ['career' ,'qualification']
career = input("What career do you like from the above list ? ")
qualification = input("Are Qualified in your choice career? ")

#Storing Career Advices
career_advices = ['You can venture into this career', 'You need to study on this career first']

#Determining the career one should venture in
if qualification.lower()  == "yes":
    print(career_advices[0])
    print("You can venture into this Career", career)
elif qualification.lower() == "no":
    print(career_advices[1])
    another_career = input("Want to try another career? If yes press yes if no press any other key ")
    while another_career == "yes":
        if qualification.lower()  == "yes":
            print(career_advices[0])
            print("You can venture into this Career", career)
        else:
            print(career_advices[1])
else:
    print("Invalid Input")
    
