def currancy():
    while True:
      print(" \n 1 - Euros to US Dollars \n 2 - US Dollars to Euros \n 3 - Euros to Pounds \n 4 - Pounds to Euros")
        
      choice = int(input("Enter your choice: "))

      while choice > 4 or choice < 1:
        choice = int(input("Enter a valid choice: "))
        
      if choice == "1":
        exchange_rate = 1.08
        euros = float(input("Enter the amount in Euros: "))
        usd = euros * exchange_rate
        print(f"{euros} Euros is equal to {usd} dollars")

      elif choice == "2":
        exchange_rate = 0.93
        usd = float(input("Enter the amount in US Dollars: "))
        euros = usd * exchange_rate
        print(f"{usd} dollars is equal to {euros} euros")

      elif choice == "3":
        exchange_rate = 0.87
        euros = float(input("Enter the amount in Euros: "))
        pounds = euros * exchange_rate
        print(f"{euros} euros is equal to {pounds} pounds")
        
      else:
        exchange_rate = 1.14
        pounds = float(input("Enter the amount in British Pounds: "))
        euros = pounds * exchange_rate
        print(f"{pounds} pounds is equal to {euros} euros")

      print("Press 'r' to restart or 'e' to end it")
      user_answer = input (" : ")
      if user_answer =="e":
       break
    
      elif user_answer == "r":
       continue


currancy()
