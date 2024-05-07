from character_class import HealthBar


class Game:
    def __init__(self, hero, enemy, gui_output):
        self.hero = hero
        self.enemy = enemy
        self.gui_output = gui_output
        self.round = 0

    def battle(self):
        self.round += 1
        # Delete previous health bars
        if self.round > 1:
            for entity in [self.hero, self.enemy]:
                # Update the line number where the new health bar will be drawn
                if entity.health_bar.line_number is not None:
                    print(entity.health_bar.line_number)
                    lines_to_delete = 3 if entity.critical_hit else 2
                    self.gui_output.delete(f"{entity.health_bar.line_number - 1}.0", f"{entity.health_bar.line_number + lines_to_delete}.end-1c")

        # The hero attacks the leviathan
        self.hero.attack(self.enemy)
        self.enemy.health_bar.update()
        self.enemy.health_bar.line_number = int(self.gui_output.index("end").split('.')[0]) - 1
        self.enemy.health_bar.draw()
        

        # The leviathan attacks the hero
        self.enemy.attack(self.hero)
        self.hero.health_bar.update()
        self.hero.health_bar.line_number = int(self.gui_output.index("end").split('.')[0]) - 1
        self.hero.health_bar.draw()
        
        


