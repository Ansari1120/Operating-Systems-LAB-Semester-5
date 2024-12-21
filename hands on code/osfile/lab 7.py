cleanest_cities=['Turkey','Morocco','Bangladesh','Malayshia']
keep_looping = True #Flag
while keep_looping == True:
 user_input = input("Enter a country ")
 for a_clean_city in cleanest_cities:
     if user_input == a_clean_city:
        print("It's one of the cleanest country")
        break
     else:
        print("Not a clean country")
        break  
else:
  keep_looping = False
