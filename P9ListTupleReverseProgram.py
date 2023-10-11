#List

#List is a collection of ordered data type
#Can change the value define one
list1=[4,'Mohit',6.4]

#print(list1[1])
#print(list1.count(4))
list1.reverse()
print(list1)



#tuple program
#Tuple is ordered collection of data
#Not change the value define one
#Append , Pop will not work
#THERE IS NOT REVERSE in tuple
tuple1 = (4,'Mohit',6.4)
print(type(tuple1)) 


#sets
#Unoordered collection data
#It does not have any indexing
#This is also mutable
#it cannot have duplicate elements

set1 = {3,6,'Hello',7.6,3}
print(set1)
set1.add('male')
print(set1)
set1.pop()
print(set1)


#Dictionary 
#No duplicate value allow
#No count method over here
person1 = {
    'name' : 'mohit',
    'age': 28,
    'company' : 'google',
    'gender' : 'male',
    'experience' : 6,
}

person1.update({'hobby' : 'cricket'})
person1.pop('gender')
print(person1)

print(person1.get('name'))
