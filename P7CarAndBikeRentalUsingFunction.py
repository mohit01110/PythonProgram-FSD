#WAP of Car Rental using list function
rate = [20,40] #[Bikes,Car]
num_vehical=[int(input(f"Enter the number of {vehical} parked ")) for vehical in ['Bike','Car']]
total=sum([num_vehical[i]*rate[i] for i in range(len(rate))])
print(total)