
class CheesPizza:
    def prepare(self):
        return "Preparing Chees Pizza"
    
class PepperoniPizza:
    def prepare(self):
        return "Preparing Perroni Pizza"
    
class VeggiePizza:
    def prepare(self):
        return "Preparing Veggie Pizza"
    
def main():
    # pizza1 = CheesPizza()
    # pizza2 = PepperoniPizza()
    # pizza3 = VeggiePizza()
    
    # print(pizza1.prepare())
    # print(pizza2.prepare())
    # print(pizza3.prepare())
    
    input = "Perroni"
    
    if input == "Perroni":
        return PepperoniPizza()
    elif input == "Chees":
        return CheesPizza()
    elif input == "Veggie":
        return VeggiePizza()
    else:
        print("No valid Pizza")
    
    
main() 