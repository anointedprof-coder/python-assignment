#slicing 
fruits =["apple","banana", "Berry", "Orange"]
myfruits =fruits[2 : 3]
print(myfruits)

#clear
fruits =["apple","banana", "Berry", "Orange"]
fruits.clear()
print(fruits)

#cinsert
fruits =["apple","banana", "Berry", "Orange"]
fruits.insert(1, "Mango")
print(fruits)

#copy
fruits =["apple","banana", "Berry", "Orange"]
myfruits =fruits.copy()
print(myfruits)

#using index to remove
fruits =["apple","banana", "Berry", "Orange"]
fruits.pop(2)
print(fruits)

#Remove
fruits =["apple","banana", "Berry", "Orange"]
fruits.remove("banana")
print(fruits)

#extend
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

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