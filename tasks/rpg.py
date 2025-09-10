import random

class User():
    def __init__(self,attack,defence,hp):
        self.name=None
        self.attack=attack
        self.defence=defence
        self.HP=hp
        self.inventory=[]

class Enemy():
    def __init__(self,name,attack,defence,hp):
        self.name=name
        self.attack=attack
        self.defence=defence
        self.HP=hp

class RPG(User,Enemy):
    def __init__(self,user,enemy):
        self.user=user
        self.enemy=enemy
        self.user_alive=True
        self.enemy_alive=True
        self.items=["Sword",None,"Shield","Axe",None,"Helmet","Armor suit",None]
        
    def start_game(self):
        print("welcome to Python RPG")
        user_name=input("enter your Hero name : ")
        self.user.name=user_name
        print(f"A wild {self.enemy.name} Appears!")
        print(f"Your Hp : {self.user.HP} | {self.enemy.name} HP : {self.enemy.HP}")
        

    def is_user_alive(self):
        if user.HP <=0:
            self.user_alive=False
            return {f" user lose !  {self.user.name}'s HP : {self.user.HP} ,{self.enemy.name}'s HP : {self.enemy.HP}"}
        return None
    def is_enemy_alive(self):
        if self.enemy.HP <=0:
            self.enemy_alive=False
            self.user.name
            self.item=random.choice(self.items)
            print(self.item)
            if self.item is None:
                return {f"user win !  {self.user.name}'s HP : {self.user.HP} ,{self.enemy.name}'s HP : {self.enemy.HP}"}
            else:
                self.user.inventory.append(self.item)
                return {f"user win !  {self.user.name}'s HP : {self.user.HP} ,{self.enemy.name}'s HP : {self.enemy.HP}.\nyou won {self.item} "}
        return None
    def war_start(self,user_action,enemy_action):
        

        if user_action=="attack" and enemy_action=="defence":
            self.enemy.HP -= abs(self.user.attack - self.enemy.defence)
            
            result=self.is_enemy_alive()
            if result:
                return result
            return {f"you attack {self.enemy.name} losses {abs(self.user.attack - self.enemy.defence)} HP"}

        elif user_action=="defence" and enemy_action=="attack":
            if (self.user.defence - self.enemy.attack)==0 :
                self.user.HP -= 5
                result=self.is_user_alive()
                if result:
                    return result
                return {f"{enemy.name} attack .you losses 5 HP"}
            else:
                self.user.HP -=  abs(self.user.defence - self.enemy.attack)
                result=self.is_user_alive()
                if result:
                    return result
                return {f"{self.enemy.name} attack .you losses {abs(self.user.defence - self.enemy.attack)} HP"}

        elif user_action=="attack" and enemy_action=="attack":
            self.enemy.HP -=abs(self.user.defence - self.enemy.attack)
            self.damage = 5 if  (abs(self.user.attack - self.enemy.defence))==0 else (abs(self.user.attack - self.enemy.defence))
            self.user.HP-=self.damage
            result=self.is_user_alive()
            if result:
                return result
            result1=self.is_enemy_alive()
            if result1:
                return result1
            
            return {f"You and {self.enemy.name}  both attacked.you losses {self.damage} HP and {self.enemy.name} losses {abs(self.user.attack - enemy.defence)} HP "}
        
        elif user_action=="run" or enemy_action=="run":
            if user_action=="run":
                self.user_alive=False
                return {f" user lose !  {self.user.name}'s HP : {self.user.HP} ,{self.enemy.name}'s HP : {self.enemy.HP}"}
            elif enemy_action=="run":
                self.enemy_alive=False
                return {f"user win !  {self.user.name}'s HP : {self.user.HP} ,{self.enemy.name}'s HP : {self.enemy.HP}"}


user=User(40,30,100)
enemy=Enemy("Goblin",30,20,50)

rpg=RPG(user,enemy)
rpg.start_game()
while (rpg.enemy_alive and rpg.user_alive):
        enemy_choice=random.choice(["attack","defence"])
        print(enemy_choice)
        print(rpg.war_start(input("Choose action: (1) Attack (2) Defend (3) Run : " ),enemy_choice))
      
        


        

        



    
        
        