import random
class Blackboard:

    def __init__(self, battery_level, spot_cleaning, general_cleaning, dusty_spot, home_path): 
        #initialize battery level, spot_cleaning, general_cleaning, dusty_spot
        self.battery_level = battery_level
        self.spot_cleaning = spot_cleaning
        self.general_cleaning = general_cleaning 
        self.dusty_spot = dusty_spot
        #Randomize dusty spot also serves as envirnment 
        #in this scenario the environment is comprised of two tiles
        #1 represent a dirty tile and 0 represents a clean tile      
        self.dusty_spot = { 'A': '1', 'B': '1'}
        self.dusty_spot['A']=random.choice([0,1])
        self.dusty_spot['B']=random.choice([0,1])
        self.home_path = "home_path"
        
    def show(self):
        print("Contents of Blackboard, Battery Level:", self.battery_level, ",",
              "Spot Cleaning:", self.spot_cleaning, ",",
              "General Cleaning:", self.general_cleaning, ",",
              "Dusty Spot:", self.dusty_spot, ",",
              "Path Home:", self.home_path)



class simplereflexagent(Blackboard):
    def __init__(self, Blackboard): 
        #place vacuum somewhere at random
        self.vacuumlocation= random.randint(0,1)
        self.dusty_spot = Blackboard.dusty_spot
        self.battery_level = Blackboard.battery_level
        self.spot_cleaning = Blackboard.spot_cleaning
        self.general_cleaning = Blackboard.general_cleaning
    def show2(self): 
        print(self.vacuumlocation, self.dusty_spot)



#Basic Node
import time 


#condition:
class Less_than_30(simplereflexagent):
    def __init__(self, simplereflexagent):
        self.battery_level = simplereflexagent.battery_level
        
    def lt3(self):
        if self.battery_level<=30:
            print("Less than 30%: Success")
            return True
        else:
            print("Less than 30%: Failure")
            return False

#tasks
class Find_home(Less_than_30):
    def __init__(self, Less_than_30):
        self.battery_level = Less_than_30.battery_level
        
    def fh(self):
        if self.battery_level <=30:
            print("Find Home: Success")
            return True
        else:
            print("Find Home: Failure") 
            return False

class Go_home(Find_home):
    def __init__(self, Find_home):
        self.battery_level = Find_home.battery_level
    def gh(self): 
        if self.battery_level <=30:
            print("Go Home: Success")
            return True
        else:
            print("Go Home: Failure") 
            return False
        
class Dock(Go_home): 
    def __init__(self, Go_home): 
        self.battery_level = Go_home.battery_level
    def d(self): 
        if self.battery_level <=30:
            print("Dock: Success")
            return True
        else:
            print("Dock: Failure") 
            return False 
#sequencer
class sequence_one:
    def seq(vacuum):
#Less than 30 takes in 1 positional arguement, vacuum
        sequencer = Less_than_30(vacuum)
        print(sequencer.lt3())
#Find home takes one positional arguement less than 30 
        sequencer = Find_home(sequencer)
        print(sequencer.fh())
#go home takes one positional arguement find home 
        sequencer = Go_home(sequencer)
        print(sequencer.gh())
#dock takes one positional arguement go home
        sequencer = Dock(sequencer)
        return sequencer.d()

        


#Blackboard takes in 5 positional arguements 
#blackboard = Blackboard(20, 1, False, 'nullnull', 'null')
#vacuum takes in 1 positional arg, blackboard 
#vacuum=simplereflexagent(blackboard)

#sequence_one.seq(vacuum)

#condition:

class Spot(simplereflexagent): 
    def __init__(self, simplereflexagent):
        self.battery_level = simplereflexagent.battery_level
        self.spot_cleaning = simplereflexagent.spot_cleaning
        self.general_cleaning = simplereflexagent.general_cleaning
        self.dusty_spot = simplereflexagent.dusty_spot
        self.vacuumlocation = simplereflexagent.vacuumlocation
        
    def sp(self):
        if self.battery_level>30 and self.spot_cleaning==True: 
            print("Spot: Success") 
            return True
        else: 
            print("Spot: Failure")
            return False 

class Clean_spot(Spot): 
    def __init__(self, Spot): 
        self.battery_level = Spot.battery_level
        self.spot_cleaning = Spot.spot_cleaning
        self.general_cleaning = Spot.general_cleaning
        self.dusty_spot = Spot.dusty_spot
        self.vacuumlocation = Spot.vacuumlocation
        
    def cs(self): 
        if self.battery_level>30 and self.spot_cleaning==True: 
            x = 20
            while x > 0:
                print('Running')
                x-=1
                time.sleep(1)
            print("Clean Spot: Success")
            return True
        else: 
            print("Clean Spot: Failure")
            return False
    
class Done_spot(Clean_spot): 
    def __init__(self, Clean_spot):
        self.battery_level = Clean_spot.battery_level
        self.spot_cleaning = Clean_spot.spot_cleaning
        self.general_cleaning = Clean_spot.general_cleaning
        self.dusty_spot = Clean_spot.dusty_spot
        self.vacuumlocation = Clean_spot.vacuumlocation
    
    def ds(self):
        if self.battery_level>30 and self.spot_cleaning==True: 
            print("Done Spot: Success")
            return True 
        else: 
            print("Done Spot: Failure")
            return False 

class Done_general1(Done_spot):
    def __init__(self, Done_spot):
        self.battery_level = Done_spot.battery_level
        self.general_cleaning = Done_spot.general_cleaning
        self.dusty_spot = Done_spot.dusty_spot
        self.spot_cleaning = Done_spot.spot_cleaning
        self.vacuumlocation = Done_spot.vacuumlocation
        
    def dg1(self):
        print("Done General: Success")
        return None

class sequence_two:
    def seq2(vacuum):
        sequencer = Spot(vacuum)
        print(sequencer.sp())
        sequencer = Clean_spot(sequencer)
        print(sequencer.cs())
        sequencer = Done_spot(sequencer)
        print(sequencer.ds())
        sequencer = Done_general1(sequencer)
        return sequencer.dg1()
        

#blackboard = Blackboard(100, False, False, 'nullnull', 'null')
#vacuum=simplereflexagent(blackboard)
#sequence_two.seq2(vacuum)

import time 

class General_cleaning(simplereflexagent): 
    def __init__(self, simplereflexagent): 
        self.battery_level = simplereflexagent.battery_level
        self.general_cleaning = simplereflexagent.general_cleaning
        self.dusty_spot = simplereflexagent.dusty_spot
        self.vacuumlocation = simplereflexagent.vacuumlocation
        self.spot_cleaning = simplereflexagent.spot_cleaning
        
    def gc(self): 
        if self.battery_level>30 and self.general_cleaning == True:
            print("General Cleaning: Success")
            return True
        else:
            print("General Cleaning: Failure")
            return False 
        
class Dust_spot(General_cleaning):
    def __init__(self, General_cleaning):
        
        self.dusty_spot = General_cleaning.dusty_spot
        self.vacuumlocation = General_cleaning.vacuumlocation
        self.battery_level = General_cleaning.battery_level
        self.general_cleaning = General_cleaning.general_cleaning
        self.spot_cleaning = General_cleaning.spot_cleaning
        
    def ds(self): 
        if self.dusty_spot['A']==1 and self.vacuumlocation == 0 and self.battery_level>30 and self.general_cleaning == True:
            print("Dust Spot: Success")
            return True
        elif self.dusty_spot['B']==1 and self.vacuumlocation == 1 and self.battery_level>30 and self.general_cleaning == True:
            print("Dust Spot: Success")
            return True
        else: 
            print("Dust Spot: Failure")
            return False

class Clean_spot(Dust_spot): 
    def __init__(self, Dust_spot): 
        self.battery_level = Dust_spot.battery_level
        self.general_cleaning = Dust_spot.general_cleaning
        self.dusty_spot = Dust_spot.dusty_spot
        self.vacuumlocation = Dust_spot.vacuumlocation
        self.spot_cleaning = Dust_spot.spot_cleaning
    
    def cs(self):
        if self.dusty_spot['A']==1 and self.vacuumlocation == 0 and self.battery_level>30 and self.general_cleaning == True:
            x = 35
            while x > 0:
                print('Running')
                x-=1
                time.sleep(1)
            print("Clean Spot: Success")
            return True
        elif self.dusty_spot['B']==1 and self.vacuumlocation == 1 and self.battery_level>30 and self.general_cleaning == True:
            x = 35
            while x > 0:
                print('Running')
                x-=1
                time.sleep(1)
            print("Clean Spot: Success")
            return True  
        else: 
            print("Clean Spot: Failure")
            return False 

class Clean_floor(Clean_spot):
    def __init__(self, Clean_spot): 
        self.battery_level = Clean_spot.battery_level
        self.general_cleaning = Clean_spot.general_cleaning
        self.dusty_spot = Clean_spot.dusty_spot
        self.vacuumlocation = Clean_spot.vacuumlocation
        self.spot_cleaning = Clean_spot.spot_cleaning
    
    def cf(self): 
        if self.dusty_spot['A']==1 and self.vacuumlocation == 0 and self.battery_level>30 and self.general_cleaning == True:
            print("Clean Floor: Success")
            return True 
        elif self.dusty_spot['B']==1 and self.vacuumlocation == 1 and self.battery_level>30 and self.general_cleaning == True:
            print("Clean Floor: Success")
            return True 
        else: 
            print("Clean Floor: Failure")
            return False 

class Done_general(Clean_floor):
    def __init__(self, Clean_floor):
        self.battery_level = Clean_floor.battery_level
        self.general_cleaning = Clean_floor.general_cleaning
        self.dusty_spot = Clean_floor.dusty_spot
        self.vacuumlocation = Clean_floor.vacuumlocation
        self.spot_cleaning = Clean_floor.spot_cleaning
        
    def dg(self):
        if self.dusty_spot['A']==1 and self.vacuumlocation == 0 and self.battery_level>30 and self.general_cleaning == True:
            print("Done General: Success")
            return True 
        elif self.dusty_spot['B']==1 and self.vacuumlocation == 1 and self.battery_level>30 and self.general_cleaning == True:
            print("Done General: Success")
            return True 
        else: 
            print('Clean Floor: Failed')
            x = 25
            while x > 0:
                print('Running')
                x-=1
                time.sleep(1)  
            print("Clean Floor: Success")
            print("Done General: Success")
            return True 

class sequence_three:
    def seq3(vacuum):
        sequencer = General_cleaning(vacuum)
        print(sequencer.gc())
        sequencer = Dust_spot(sequencer)
        print(sequencer.ds())
        sequencer = Clean_spot(sequencer)
        print(sequencer.cs())
        sequencer = Clean_floor(vacuum)
        print(sequencer.cf())
        sequencer = Done_general(sequencer)
        return sequencer.dg()



#blackboard = Blackboard(100, True, True, 'nullnull', 'null')
#vacuum=simplereflexagent(blackboard)
#sequence_three.seq3(vacuum)

class Do_nothing(simplereflexagent):
    def __init__(self, simplereflexagent):
        self.battery_level = simplereflexagent.battery_level
        self.general_cleaning = simplereflexagent.general_cleaning
        self.spot_cleaning = simplereflexagent.spot_cleaning
    
    def dn(self):
        if self.battery_level>30 and self.general_cleaning == False and self.spot_cleaning == False: 
            return True 
        else: 
            return False 



class Priority(Blackboard):
    def __init__(self, Blackboard):
        self.spot_cleaning = Blackboard.spot_cleaning
        self.battery_level = Blackboard.battery_level
        
    def donothing(self):
        if Do_nothing.dn(vacuum) == True:
            return print("Do Nothing: Success")
        elif self.spot_cleaning == True and self.battery_level<30: 
            return sequence_one.seq(vacuum)
        elif self.spot_cleaning == True and self.battery_level>30:    
            return sequence_two.seq2(vacuum)
        else:
            return sequence_three.seq3(vacuum)
 


        


blackboard = Blackboard(40, True, True, None, None)
blackboard.show()
vacuum=simplereflexagent(blackboard)
Final = Priority(blackboard)
Final.donothing()

