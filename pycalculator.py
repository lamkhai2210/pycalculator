
import matplotlib.pyplot as plt
import os
while True:
  print("1. Speed_check. ")
  print("")
  print("2. Shapes 2D and 3D.")
  print("")
  print("3. Triangle.")
  print("")
  print("4. Graphs Visualization.")
  print("")
  print("5. Fraction calculator")
  print("")
  
  choice = input("Enter your choice (1-5): ")
  
  
  if choice == "1":
    os.system("cls")
    def speed_limit(distance,time_taken):
      speed = distance/time_taken
      print("Speed: " + str(speed) )
    userDistance = int(input("Enter distance(meter): "))
    userTime = int(input("Enter time taken(minutes): "))
    speed_limit(userDistance,userTime)
    input("Press enter to continue")
  #---------------------------------------------------------------------
  
  elif choice == "2":
    os.system("cls")
    pi = 3.14159265359
    def perimeter_square(length):
       return 4 * length
  
    def area_square(length):
      return length * length
  
    def perimeter_rectangle(length,width):
      return 2 * length + 2 * width
  
    def area_rectangle(length,width):
      return length * width
  
    def perimeter_circle(radius):
      return 2* pi * radius
  
    def area_circle(radius):
      return pi * radius * radius
  
    def area_cube(length):
      return 6 * (length * length)
  
    def volume_cube(length):
      return length * length * length
  
    def area_cuboid(length, width, height):
      return 2 * (height * length + width * height + length * width)
  
    def volume_cuboid(length, width, height):
      return length * width * height
  
    while True:
       print("")
       print("Shape Calculator")
       print("")
       print("2D Shapes")
       print("1. Square")
       print("2. Rectangle")
       print("3. Circle")   
       print("")
       print("3D Shapes")
       print("4. Cube")
       print("5. Cuboid")   
       print("")
      
       choice_2 = input("Enter your choice (1-5): ")
  
       if choice_2 == "1":
         os.system("cls")
         length = int(input("Enter Length: "))
         print("Area of the square: ", str(area_square(length)))
         print("Perimeter of the square: ", str(perimeter_square(length)))
         input("Press enter to continue")
         os.system("cls")
         
       elif choice_2 == "2":
         os.system("cls")
         length = int(input("Enter Length: "))
         width = int(input("Enter Width: "))
         print("Area of the rectangle: ", str(area_rectangle(length, width)))
         print("Perimeter of the rectangle: ", str(perimeter_rectangle(length, width)))
         input("Press enter to continue")
         os.system("cls")
         
       elif choice_2 == "3":
         os.system("cls")
         radius = int(input("Enter Radius: "))
         print("Area of circle: ", str(area_circle(radius)))
         print("Perimeter of circle: ", str(perimeter_circle(radius)))
         input("Press enter to continue")
         os.system("cls")
         
       elif choice_2 == "4":
         os.system("cls")
         length = int(input("Enter Length: "))
         print("Area of cube: ", str(area_cube(length)))
         print("Volume of cube: ", str(volume_cube(length)))
         input("Press enter to continue")
         os.system("cls")
         
       elif choice_2 == "5":
         os.system("cls")
         length = int(input("Enter Length:"))
         width = int(input("Enter Width: "))
         height = int(input("Enter Height: "))
         print("Area of cuboid: ", str(area_cuboid(length, width, height)))
         print("Volume of cuboid: ", str(volume_cuboid(length, width, height)))
         input("Press enter to continue")
         os.system("cls")

       else: 
        os.system("cls")
        print("Invalid Input!")
        input("Press enter to continue")
        print("")
         
      
    
  
  #----------------------------------------------------------------------
  elif choice == "3":
    print("1. Half triangle")
    print("2. Full triangle")
    print("")
    choice_3 = input("Choose 1 or 2: ")
    
    if choice_3 == "1":
      os.system('cls')
      for i in range(1,6):
        print(i * "#")
      input("Press enter to continue")
  
    elif choice_3 == "2":
      os.system('cls')
      length3 = int(input("Enter your length")) 
      space = length3 - 1
      for i in range(1,length3 + 1):
        print((space * " ") + (i * "#") + (i * "*"))
        space -= 1
      input("Press enter to continue")

     
    else: 
      os.system("cls")
      print("Invalid Input!")
      print("")
      
  #------------------------------------------------------------------
  if choice == "4":
    os.system('cls')
    while True: 
      print("--------------------------")
      print("Data Visualization Program")
      print("--------------------------")
      print("1. Line Graph Visualization")
      print("2. Bar Graph Visualization")
      print("3. Pie Chart Visualization")
      print("--------------------------")
      choice_4 = input("Enter your choice 1-3:")
  
      if choice_4 == "1":
        os.system("cls")
        print("--------------------------")
        print("Line Graph Visualization")
        print("--------------------------")
        line_labels = []
        line_datas = []
        title = input("What is the graph title? ")
        length = int(input("How many data to display? "))
        print("")
        for i in range(length):
          label = input(f"Enter label no. {i+1}: ")
          data = input(f"Enter data no. {i+1}: ")
          line_labels.append(label)
          line_datas.append(data)
          print(f"Data no. {i+1} has been added!")
          print("")
        input("Press enter to continue...")
        plt.plot(line_labels, line_datas)
        plt.title(title)
        plt.show()
        os.system("cls")
  
  
      elif choice_4 == "2":
        os.system("cls")
        print("--------------------------")
        print("Bar Graph Visualization")
        print("--------------------------")
        bar_labels = []
        bar_datas = []
        title = input("What is the graph title? ")
        length = int(input("How many data to display? "))
        print("")
        for i in range(length): 
          label = input(f"Enter label no. {i+1}: ")
          data = input(f"Enter data no. {i+1}: ")
          bar_labels.append(label)
          bar_datas.append(data)
          print(f"Data no. {i+1} has been added!")
          print("")
        input("Press enter to continue...")
        plt.bar(bar_labels, bar_datas)
        plt.title(title)
        plt.show()
        os.system("cls")
    
    
      elif choice_4 == "3":
        os.system("cls")
        print("------------------------")
        print("Pie Chart Visualization")
        print("-----------------------")
        pie_labels = []
        pie_datas = []
        title = input("What is the graph title? ")
        length = int(input("How many data to display? "))
        print("")
        for i in range(length):
          label = input(f"Enter label no. {i+1}: ")
          data = input(f"Enter data no. {i+1}: ")
          pie_labels.append(label)
          pie_datas.append(data)
          print(f"Data no. {i+1} has been added!")
          print("")
        input("Press enter to continue...")
        plt.pie(pie_datas,labels = pie_labels)
        plt.title(title)
        plt.show()
        os.system("cls")
    
      else: 
        os.system("cls")
        print("Invalid Input!")
        print("")
  #------------------------------------------------------------------
  if choice == "5":
    os.system('cls')
    print("1. Check HCF")
    print("2. Fraction Addition")
    print("3. Fraction Subtract")
    print("")
    choice_5 = int(input("Choose 1-3: "))
    
    def check_HCF():
      numerator = int(input("Enter numerator: "))
      denominator = int(input("Enter denominator: "))
      smaller = 0
      if numerator < denominator:
        smaller = numerator
      else:
        smaller = denominator
      HCF = 1
      for i in range(1, smaller + 1):
        if (numerator % i == 0) and (denominator % i == 0):
          HCF = i
  
      print("HCF : " + str(HCF))
      
      print ("The lowest numerator is: " + str(numerator/HCF))
      print("The lowest denominator is: " + str(denominator/HCF))  
  
    def plus_fraction(): 
      n1 = int(input("Enter first numerator: "))
      d1 = int(input("Enter first denominator: "))
      n2 = int(input("Enter second numerator: "))
      d2 = int(input("Enter second denominator: "))
      new_numerator = 0
      new_denominator = 0
      if d1 == d2:
        new_numerator = n1 + n2
        new_denominator = d1
      else:
        new_denominator = d1 * d2
        n1 = n1 * d2
        n2 = n2 * d1
        new_numerator = n1 + n2
  
      print("Numerater Result: " + str(new_numerator))
      print("Denominator Result: " + str(new_denominator))
  
    def subtract_fraction(): 
      n1 = int(input("Enter first numerator: "))
      d1 = int(input("Enter first denominator: "))
      n2 = int(input("Enter second numerator: "))
      d2 = int(input("Enter second denominator: "))
      new_numerator = 0
      new_denominator = 0
      if d1 == d2:
        new_numerator = n1 - n2
        new_denominator = d1
      else:
        new_denominator = d1 * d2
        n1 = n1 * d2
        n2 = n2 * d1
        new_numerator = n1 - n2
  
      print("Numerater Result: " + str(new_numerator))
      print("Denominator Result: " + str(new_denominator))
    
    if choice_5 == "1":
      check_HCF()
      input("Press enter to continue")
    
    elif choice_5 == "2":
      plus_fraction()
      input("Press enter to continue")
    
    elif choice_5 == "3":
      subtract_fraction()
      input("Press enter to continue")


    else:
      os.system("cls")
      print("Invalid Input!")
      print("")
      
  #--------------------------------------------------------------
  else: 
      os.system("cls")
      print("Invalid Input!")
      print("")
  