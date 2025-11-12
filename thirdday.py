motors= ["lexus", "Toyota", "Camry", "Benz"]
motors[0]= "KIA"
print(motors)

motors= ["lexus", "Toyota", "Camry", "Benz"]
motors.sort(reverse=False)
print(motors)

#index
motors= ["lexus", "Toyota", "Camry", "Benz"]
print(motors[3])

motors= []
motors.append('Camry')
motors.append('lexus')
motors.append('KIA')
motors.append('GLK')
motors.append('Toyota')
print(motors)

#Remove
fruits =["apple","banana", "Berry", "Orange"]
fruits.remove("banana")
print(fruits)

#using index to remove
fruits =["apple","banana", "Berry", "Orange"]
fruits.pop(2)
print(fruits)

#printing list in a loop
fruits =["apple","banana", "Berry", "Orange"]
for a in range (len(fruits)):
    print(fruits[a])

#copy
fruits =["apple","banana", "Berry", "Orange"]
myfruits =fruits.copy()
print(myfruits)

#slicing 
fruits =["apple","banana", "Berry", "Orange"]
myfruits =fruits[2 : 3]
print(myfruits)

#clear
fruits =["apple","banana", "Berry", "Orange"]
fruits.clear()
print(fruits)










