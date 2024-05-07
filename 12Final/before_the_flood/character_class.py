import random

class Character:
    def __init__(self, 
                 name: str, 
                 health: int,
                 crit_chance: float = 0,
                 gui_output=None
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.crit_chance = crit_chance
        self.gui_output = gui_output

        self.weapon = None
        self.critical_hit = False

    def attack(self, target) -> None:
        damage = random.randint(self.weapon.damage - int(0.25*self.weapon.damage), self.weapon.damage + int(0.25*self.weapon.damage))
        
        if random.random() <= self.crit_chance:
            damage *= 2
            self.critical_hit = True
            if self.gui_output:
                self.gui_output.insert('end', f"{self.name} CRITICALLY hits {target.name} for {damage} damage!\n")
                self.gui_output.see('end')
        else:
            self.critical_hit = False

        target.health -= damage
        target.health = max(0, target.health)
        target.health_bar.update()

    def persuade(self, target, persuasion_technique: float) -> bool:
        success = self.charisma * persuasion_technique > target.openness
        return success


class Weapon:
    def __init__(self, 
                 name: str, 
                 weapon_type: str,
                 damage: int, 
                 value: int
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

class Hero(Character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 crit_chance: float,
                 charisma: int,
                 weapon: Weapon,
                 gui_output=None,
                 ) -> None:
        super().__init__(name, health, crit_chance, gui_output)
        self.weapon = weapon
        self.charisma = charisma
        self.health_bar = HealthBar(self, colour="green", gui_output=gui_output)

class Leviathan(Character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 crit_chance: float,
                 weapon: Weapon,
                 gui_output=None,
                 ) -> None:
        super().__init__(name, health, crit_chance, gui_output)
        self.weapon = weapon
        self.health_bar = HealthBar(self, colour="blue", length=80, gui_output=gui_output)

class Rat(Character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 crit_chance: float,
                 weapon: Weapon,
                 gui_output=None,
                 ) -> None:
        super().__init__(name, health, crit_chance, gui_output)
        self.weapon = weapon
        self.health_bar = HealthBar(self, colour="red", gui_output=gui_output)

class NPC(Character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 openness: int,
                 gui_output=None,
                 ) -> None:
        super().__init__(name, health, gui_output)
        self.openness = openness
        self.health_bar = HealthBar(self, colour="yellow", gui_output=gui_output)

class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"

    def __init__(self,
                 entity,
                 length: int = 20,
                 colour: str = "",
                 gui_output=None
                 ) -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health
        self.colour = colour
        self.gui_output = gui_output
        self.line_number = None
        

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw(self) -> None:

        remaining_bars = int(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars

        if self.gui_output:
            self.gui_output.insert('end', f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.health_max}\n")
            self.gui_output.insert('end', f"{self.barrier}")
            self.gui_output.insert('end', f"{self.symbol_remaining * remaining_bars}"
              f"{self.symbol_lost * lost_bars}", self.colour
            )
            self.gui_output.insert('end', f"{self.barrier}\n"
            )
            self.gui_output.see('end')
        
        

blade_of_chosen = Weapon(name="Blade of the Chosen", weapon_type="sword", damage=20, value=1000)
leviathan_tentacle = Weapon(name="Tentacle", weapon_type="body", damage=30, value=2000)
leviathan_mandible = Weapon(name="Mandible", weapon_type="body", damage=40, value=3000)