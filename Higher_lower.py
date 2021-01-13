import random
from os import system
from time import sleep
a={"Elon musk (Tesla)":184,"Jeff Beszos(Amazon)":182,"Bernard Arnault(Luis Vuitton, luxury brand)":151,"Bill Gates(Microsoft)":122,"Mark Juckerberg(Faceebook)":92,"Zong Shanshan(water bottle company,china)":91,"Warren Buffet(Berkshire Hathaway)":88,"Larry Elisson()":87,"Larry Page(Google)":77,"Mukesh Ambani(Reliance and telecom)":75,"Steve Ballmer(Microsoft)":73,"Amanica Ortega(ZARA, fashion company)":72,"Francoise Bettencourt(L'Oreal)":71,"Jim Walton(Walmart)":69,"Jack Ma(Alibaba)":58,"Michael Bloomberg(Bloomberg)":55,"Phil Knight(Nike)":54}
b=["Elon musk (Tesla)","Jeff Beszos(Amazon)","Bernard Arnault(Luis Vuitton, luxury brand)","Bill Gates(Microsoft)","Mark Juckerberg(Faceebook)","Zong Shanshan(water bottle company,china)","Warren Buffet(Berkshire Hathaway)","Larry Elisson()","Larry Page(Google)","Mukesh Ambani(Reliance and telecom)","Steve Ballmer(Microsoft)","Amanica Ortega(ZARA, fashion company)","Francoise Bettencourt(L'Oreal)","Jim Walton(Walmart)","Jack Ma(Alibaba)","Michael Bloomberg(Bloomberg)","Phil Knight(Nike)"]
quit=False
while not quit:
  score=0
  first=b[random.randint(0,16)]
  first_value=a[first]
  c=random.randint(0,16)
  second=b[c]
  second_value=a[second]
  should_continue=False
  while not should_continue:
    if first==second:
      c+=1
      second=b[c]
      second_value=a[second]
      print('''        _       _               
    /\  /(_) __ _| |__   ___ _ __ 
   / /_/ / |/ _` | '_ \ / _ \ '__|
  / __  /| | (_| | | | |  __/ |   
  \/ /_/ |_|\__, |_| |_|\___|_|   
            |___/                 
    __                           
    / /  _____      _____ _ __    
   / /  / _ \ \ /\ / / _ \ '__|   
  / /__| (_) \ V  V /  __/ |      
  \____/\___/ \_/\_/ \___|_|      
                                  ''')
    print(f"Your current score is: {score}.")
    print(f"A: {first}")
    print('''_    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____/  
                ''')
    print(f"B: {second}")
    guess=input("Who have more wealth, 'A' or 'B': ").lower()
    if guess=='a':
      if first_value>second_value:
        score+=1
        first=second
        first_value=a[first]
        second=b[random.randint(0,16)]
        second_value=a[second]
        system('cls')
      else:
        print(f"You are wrong.\nYour score: {score}")
        should_continue=True
    elif guess=='b':
      if second_value>first_value:
        score+=1
        first=second
        first_value=a[first]
        second=b[random.randint(0,16)]
        second_value=a[second]
        system('cls')
      else:
        print(f"You are wrong.\nYour score: {score}")
        should_continue=True
  exit=(input("Want to beat your score this time? Play again 'Y' or 'N': ")).lower()
  if exit=='n':
    quit=True
    sleep(2)
    system('cls')
  else:
    system('cls')