import random 

warm = ["Mexico", "Venezuela"]

cold = ["Canada", "Russia"]

def choose_warm(warm_list):
 return random.choice(warm_list)

def choose_cold(cold_list):
 return random.choice(cold_list)

def activities_countries(country):
 activities = {
  "Mexico": ["visit cancun", "go to cdmx"],
  "Venezuela": ["vist ....", "go to..."],
  "Canada": ["go to quebec", "ski"],
  "Russia": ["drink", "vodka"]
}
 return activities.get(country)


while True:
 print("Choose the type of weather you would like to have in your vacation")
 print("\n 1 - warm \n 2 - cold")
 choice = input("Type warm or cold: ").lower()

 if choice == "warm":
  warm = choose_warm(warm)
  print(f"You should go to: {warm}")
  
  user_answer = input("Write the country that was choosen to know activities or type exit to end it: ").strip()

  if user_answer.lower() == "exit":
   print("Bye bye!")
   break
  
  else:
   activities = activities_countries(user_answer)
   print(f"\n Popular activities in {user_answer}:")
   for i, activities in enumerate(activities, start=1):
    print(f"{i}. {activities}")

 
 
 elif choice == "cold":
  cold = choose_cold(cold)
  result = print(f"You should go to: {cold}")

  

  
  

 else:
  print("Type a valid input")


  


   