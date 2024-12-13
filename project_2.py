def Haunted_Forest_Game():
    print('''hardik, the brave explorer, ventured deep into the haunted forest to find a hidden treasure. 
        She got lost after traveling 100 kilometers. Now, she needs your help to navigate through the forest and find her way out, or perhaps discover the treasure.
        hardik has two paths ahead of her: left and right. You must guide her through the haunted forest and make sure she makes it out alive... or finds the treasure.''')
    print("RULES","\n","for left=1","\n","right=2")
    print("Let the adventure begin...")

    n = int(input("(1) for LEFT OR (2) for RIGHT --> "))
    
    if n == 1:
        print("After walking for a while, two paths appear.")
        n1 = int(input("left (1) or right (2): "))
        
        if n1 == 1:
            print("There is a spooky, dark cave ahead.")
            print("Suddenly, you hear growling from within... a huge bear appears!")
            print("GAME OVER")
        elif n1 == 2:
            print("A thick mist surrounds you. You can't see anything.")
            print("Suddenly, you feel something cold grab your ankle... a ghost!")
            print("GAME OVER")
            
    elif n == 2:
        print("After walking for a while, two paths appear.")
        m = int(input("left (1) or right (2): "))
        
        if m == 1:
            print("Oh no, you stumble into an ancient trap! The ground opens beneath you.")
            print("GAME OVER")
        elif m == 2:
            print("You find yourself at the entrance of an eerie abandoned mansion.")
            print("The door creaks open, and a mysterious figure approaches you.")
            print("The figure asks if you wish to enter the mansion.")
            m2 = int(input("1 for enter or 2 for stay outside: "))
            
            if m2 == 1:
                print("You enter the mansion cautiously. After exploring the dark halls, you find the hidden treasure!")
                print("Congratulations! Sarah found the treasure and escaped the haunted forest.")
                print("YOU WON THE GAME!")
            elif m2 == 2:
                print("You decide not to risk it and stay outside.")
                print("Suddenly, the forest seems to close in around you, and you're lost forever.")
                print("GAME OVER")
    


Haunted_Forest_Game()

