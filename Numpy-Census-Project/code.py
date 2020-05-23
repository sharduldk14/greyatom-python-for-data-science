# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",",skip_header=1)
census=np.concatenate([data,new_record])


# --------------
#Code starts here
age=census[:,0]
max_age=age.max()
print(max_age)
min_age=age.min()
age_mean=np.mean(age)
age_std=np.std(age)



# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

len_=[len_0,len_1,len_2,len_3,len_4]
minority_race=len_.index(min(len_))  
print(minority_race)



# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
print(senior_citizens)

working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))



# --------------
#Code starts here
import numpy as np 
high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=high[:,7].mean()
print(avg_pay_high)
avg_pay_low=low[:,7].mean()
print(avg_pay_low)






