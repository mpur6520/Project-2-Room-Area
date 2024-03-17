#Maru Puran
#October 5, 2023
#to fully become familiar with mathematics and calculations within python, create a code calculating an irregular shape (geometry) based on user input

#get the user inputs and store them into assigned created variables, convert to integers for math
sideA = int(input("Enter side A: "))
sideB = int(input("Enter side B: "))
sideC = int(input("Enter side C: "))
sideD = int(input("Enter side D: "))
sideE = int(input("Enter side E: "))

big_rec_area = (sideB * sideA) #calculate area of big rectangle
small_rec_area = (sideA-sideC)*(sideD-sideB-sideE) #calculate area of small rectangle
small_tri_area = (sideE)*0.5*(sideA-sideC) #calculate area of the triangle

total_area = big_rec_area + small_rec_area + small_tri_area #add all areas together to get area of total shape

print("\nRoom Area: " + str(total_area)) #output the room area for the user