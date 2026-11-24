while True:
    userscore=input("Enter your score or type NONE:")
    if userscore.lower()=="none":
       print("Cool!")
       break
    try:
      stuscore = float(userscore)
            
      if stuscore < 0 or stuscore > 20:
         print("warning!! The score might be incorrect.")

      elif stuscore <= 11:
         print("Terrible")
         
      elif stuscore <= 15:
         print("NOT bad")
         
      else:
         print("Prefect")
         
    except ValueError:
      print("Pleas just enter a number")
      
