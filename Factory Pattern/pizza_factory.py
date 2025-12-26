class Pizza:
    def prepare(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class CheesPizza:
    def prepare(self):
        return "Preparing Chees Pizza"
    
class PepperoniPizza:
    def prepare(self):
        return "Preparing Perroni Pizza"
    
class VeggiePizza:
    def prepare(self):
        return "Preparing Veggie Pizza"
    
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "Chees":
            return CheesPizza()
        elif pizza_type == "Veggie":
            return VeggiePizza()
        elif pizza_type == "Perroni":
            return PepperoniPizza()
        else:
            raise ValueError(f"Unknown Pizza Type: {pizza_type}")
        
        
def main():
    try:
        user_input = "Perroni"
        pizza = PizzaFactory.create_pizza(user_input)
        print(pizza.prepare())
    
    except ValueError as e :
        print(e)
        
if __name__ == "__main__":
    main