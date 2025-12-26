from typing import List

class Stock:
    def __init__(self,name , price):
        self.name = name
        self.price = price
        self.observers: List = []
        
    def add_observer(self,observer):
        self.observers.append(observer)
        
    def remove_observer(self,obsever):
        self.observers.remove(obsever)
        
    def notify_observer(self):
        for observer in self.observers:
            observer.update(self)
        
    def set_price(self , new_price):
        self.price = new_price
        self.notify_observer()
        
class Observer:
    def update(self, stock):
        raise NotImplementedError("this method should be overriden by subclasses")
        
class Dashbaord(Observer):
    def update(self,stock):
        print(f"Dashbaord updated: {stock.name} is now ${stock.price}")
        
class EmailAlert(Observer):
    def update(self,stock):
        print(f"Email Alert: {stock.name} price updated to ${stock.price}")
        
class SMSAlert(Observer):
    def update(self,stock):
        print(f"SMS Alert: {stock.name} price updated to ${stock.price}")
        
        
apple_stock = Stock("AAPL",150)
tesla_stock = Stock("TSLA", 400)

#observer
dashbord = Dashbaord()
email_alerts = EmailAlert()
sms_alerts = SMSAlert()

apple_stock.add_observer(dashbord)
apple_stock.add_observer(email_alerts)
apple_stock.add_observer(sms_alerts)

tesla_stock.add_observer(dashbord)

apple_stock.set_price(160)
apple_stock.set_price(500)