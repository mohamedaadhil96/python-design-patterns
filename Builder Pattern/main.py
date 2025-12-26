class House:
    def __init__(self , bedrooms,bathrooms,kitchen,garden,garage,pool,solar_panals,smart_home):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.kitchen = kitchen
        self.garden = garden
        self.garage = garage
        self.pool = pool
        self.solar_panals = solar_panals
        self.smart_home = smart_home
    
    def __str__(self):
        features = [
            f"Bedrooms : {self.bedrooms}",
            f"Bathrooms : {self.bathrooms}",
            f"Kitchen : {'Yes' if self.kitchen else 'No'}",
            f"Garden : {'Yes' if self.garden else 'No'}",
            f"Garage : {'Yes' if self.garage else 'No'}",
            f"Pool : {'Yes' if self.pool else 'No'}",
            f"Solar_panals : {'Yes' if self.solar_panals else 'No'}",
            f"Smart_home : {'Yes' if self.smart_home else 'No'}",
        ]

        return " | ".join(features)
    
class HouseBuilder:
    def __init__(self):
        self.bedrooms = 1
        self.bathrooms = 1
        self.kitchen = False
        self.garden = False
        self.garage = False
        self.pool = False
        self.solar_panals = False
        self.smart_home = False
        
    def set_bedrooms(self,count):
        self.bedrooms = count
        return self
    
    def set_bathrooms(self,count):
        self.bathrooms = count
        return self
    
    def add_kitchen(self):
        self.kitchen = True
        return self
    
    def add_garden(self):
        self.garden = True
        return self
    
    def add_garage(self):
        self.garage = True
        return self
    
    def add_pool(self):
        self.pool = True
        return self
    
    def add_solar_panals(self):
        self.solar_panals = True
        return self
    
    def add_smart_home(self):
        self.smart_home = True
        return self
    
    def build(self):
        return House(
            self.bedrooms,
            self.bathrooms,
            self.kitchen,
            self.garden,
            self.garage,
            self.pool,
            self.solar_panals,
            self.smart_home
        )
        
        
house_builder = HouseBuilder()

custom_house = (
    house_builder.set_bedrooms(4)
    .set_bathrooms(3)
    .add_garden()
    .add_garage()
    .add_pool()
    .add_smart_home()
    .build()
)

print("Custom House :", custom_house)