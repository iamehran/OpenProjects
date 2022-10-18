#This is a Coffee Machine program which lets 
#user choose their desired coffee and pay accordingly.

MENU = {                                        #Coffee Menu
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

coffee_emoji='☕'

resources = {                                   #Total Resources 
    "water": 300,
    "milk": 200,
    "coffee": 100,

}

def check_resources(coffee_ingredients) :       #Check available resources
    
    for ingredient in coffee_ingredients :
    
        if coffee_ingredients[ingredient] > resources[ingredient] :
           
            print(f"Sorry! Not enough {ingredient} .")
            return False
    
    return True
    
def transaction(coffee_cost) :                 #Money Transaction
    
    print("Please insert coins !")
    quarter=int(input("How many quarters? "))
    dime=int(input("How many dimes? "))
    nickle=int(input("How many nickles? "))
    penny=int(input("How many pennies? " ))
    
    total_money=(quarter*0.25)+(dime*0.10)+(nickle*0.05)+(penny*0.01)
    
    if total_money >= coffee_cost :
        change=round(total_money-coffee_cost,2)
        if change>0 :
            print(f"Here is your ${change} in change!")
        return True
        
    else:
        print("Sorry that's not enough money. Money refunded !")
        return False
    
def make_coffee(coffee_choice,coffee_ingredients) :        #Makes coffee if resources available and transaction is successful
    for ingredient in coffee_ingredients :
        resources[ingredient]-=coffee_ingredients[ingredient]
        
    print(f"Here is your {coffee_choice} ☕. Enjoy!")

def coffee_machine() :                       #Lets user interact with the machine
    
    money=0
    machine_is_on=True
    while machine_is_on :
    
        choice=input("\nWhat would you like to have ?\n☕Espresso\n☕Latte\n☕Cappuccino\nEnter : ").lower()
        
        #Type 'off' to switch off the machine or 'report' to show resources left
        
        if choice=='report' :
            # for k,v in resources.items() :
            #     print(f"{k} : {v}")
            print(f"\nWater : {resources['water']} ml   ")
            print(f"Milk : {resources['milk']} ml")
            print(f"Coffee : {resources['coffee']} g ")
            print(f"Money : ${money}")
            
        elif choice=='off' :
            machine_is_on=False
            
        else :
            coffee=MENU[choice]
            
            resources_left=check_resources(coffee['ingredients'])
            if resources_left :
                 
                if transaction(coffee['cost']) :
                     money+=coffee["cost"]
                     make_coffee(choice,coffee["ingredients"])
                
                
coffee_machine()                          #Starts machine
    
