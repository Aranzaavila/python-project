import random 

warm = ["Mexico", "Venezuela"]

cold = ["Canada", "Russia"]

def choose_warm(warm_list):
 return random.choice(warm_list)

def choose_cold(cold_list):
 return random.choice(cold_list)

activities = {
 "Mexico": ["visit cancun", "go to cdmx"],
 "Venezuela": ["vist ....", "go to..."],
 "Canada": ["go to quebec", "ski"],
 "Russia": ["", ]
}


while True:
 print("Choose the type of weather you would like to have in your vacation")
 print("\n 1 - warm \n 2 - cold")
 choice = input("Type warm or cold: ").lower()
 if choice == "warm":
  warm = choose_warm(warm)
  print(f"You should go to: {warm}")
  break

  
 
 
 elif choice == "cold":
  cold = choose_cold(cold)
  print(f"You should go to: {cold}")
  user_answer = input(f"Do you want to know some activities from {cold}?")
  if user_answer == "yes":


  
  

 else:
  print("Type a valid input")


  


   