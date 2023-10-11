#We Park  Bikes and Cars
#Rate Per Bike is Rs 20
#Rate Per Car is Rs 40
#Input Number of Bike
#Input Number of Cars
#Can we create a program which will tell the owner the money that he has earned

total_bike = int(input("Enter Total Number of Bikes : - "))
total_car = int(input("Enter Total Number of Cars : - "))

bike_hour = int(input("Enter Total Hours of Bike"))
car_hour = int(input("Enter Total Hours of Car"))

bike_hour_total = bike_hour * int(20)
car_hour_total = car_hour * int(40)


bike_earning = total_bike * int(20)
car_earning = total_car * int(40)

total_earning_bike = bike_hour_total + bike_earning
total_earning_car = car_hour_total + car_earning

total_earning = total_earning_bike + total_earning_car

print("Your Total Earning of Bike is :- ", total_earning_bike)
print("Your Total Earning of Car is :- ", total_earning_car)
print("Your Total Earning is :- " , total_earning)

