def currancy():
 while True:
   print(" \n 1 - Euros to US Dollars \n 2 - US Dollars to Euros \n 3 - Euros to Pounds \n 4 - Pounds to Euros \n 5 - Euros to Mexican pesos \n 6 - Mexican pesos to Euros")
        
   choice = int(input("Enter your choice: "))

   while choice > 6 or choice < 1:
      choice = int(input("Enter a valid choice: "))
        
      # From Euros to Dollars
      if choice == "1":
        exchange_rate = 1.20
        amount = float(input("Enter the amount: "))
        usd = amount * exchange_rate
        print(f"{amount} Euros is equal to {usd} dollars")

      # From Dollars to Euros
      elif choice == "2":
        exchange_rate = 0.93
        amount = float(input("Enter the amount: "))
        euros = amount // exchange_rate
        print(f"{amount} dollars is equal to {euros} euros")
       
      # From euros to pounds
      elif choice == "3":
        exchange_rate = 1.15
        amount = float(input("Enter the amount: "))
        pounds = amount // exchange_rate
        print(f"{amount} euros is equal to {pounds} pounds")
        
     # from pounds to euros
      elif choice == "4":
        exchange_rate = 1.15
        amount = float(input("Enter the amount: "))
        euros = amount * exchange_rate
        print(f"{amount} pounds is equal to {euros} euros")
# from euros to pesos
      elif choice == "5":
        exchange_rate = 21.39
        amount = float(input("Enter the amount: "))
        pesos = amount * exchange_rate
        print(f"{amount} Euros is equal to {pesos} Mexican pesos")

      else:
        exchange_rate = 0.04
        amount = float(input("Enter the amount: "))
        euros = amount / exchange_rate
        print(f"{amount} mexican pesos is equal to {euros} euros")


        
        
       
   
 


      print("Press 'r' to restart or 'e' to end it")
      user_answer = input (" : ")
      if user_answer =="e":
       break
    
      elif user_answer == "r":
       continue


currancy()
