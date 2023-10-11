#Takes the input form the user and assign it or put it into the list
 #Range built in function used in this program
#Append function also use in this


num_learners = int(input("Enter the number of users"))
learners= []

for i in range(num_learners):
    learner_name = input(f"Enter name of the learner {i+1}: ")
    learners.append(learner_name)
    
print("List of learners: ")
print(learners)