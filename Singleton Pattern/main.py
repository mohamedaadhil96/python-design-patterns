#Singleton Pattern

# class ControlTower:
#      def __init__(self):
#           print("Initialize Control Tower")
          
    
# tower_1 = ControlTower()
# tower_2 = ControlTower()

# print(tower_1 is tower_2)
# Output 
    #Initialize Control Tower
    #Initialize Control Tower
    #False 

# The Singleton Pattern is a creational design pattern that ensures only one instance of a class exists throughout the application and provides a global access point to that instance.


class ControlTower:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print('Initialize Control Tower')
        return cls._instance
    
    def manageFlight(self, flight):
        print(f"Managing flight : {flight}")
    
tower_1 = ControlTower()
tower_2 = ControlTower()

tower_1.manageFlight("A380")
tower_1.manageFlight("A370")
print(tower_1 is tower_2)
