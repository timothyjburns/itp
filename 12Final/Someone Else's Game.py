#------ Import Statements-------#
import sys
 
 
#--------- Game Classes ------- #
class Object():
    """Base Object Class"""
    def __init__(self):
        self.self = self
 
 
class Key(Object):
    def __init__(self, name, room, match):
        self.name = name
        self.room = room
        self.match = match
 
 
class Door(Object):
    def __init__(self, name, number, locked, match):
        self.name = name
        self.number = number
        self.locked = locked
        self.match = match
 
 
class Player():
    def __init__(self, name, playerlocation):
        self.self = self
        self.name = name
        self.playerlocation = playerlocation
    def stats(self, health, armour, attack, level, xp):
        self.health = health
        self.armour = armour
        self.attack = attack
        self.level = level
        self.xp = xp
        self.max_health = self.level * 10 + 15
 
 
class Room():
    def __init__(self, number, name, victory):
        self.self = self
        self.number = number
        self.name = name
        self.victory = victory
 
 
class Hall():
    def __init__(self, name, number=0, victory=None):
        self.self = self
        self.number = number
        self.name = name
        self.victory = victory
 
class Monster():
    def __init__(self):
        self.self = self
 
 
class Wolf(Monster):
    def __init__(self, name, room):
        self.self = self
        self.room = room
        self.name = name
    def stats(self, health, armour, attack, level, xp):
        self.health = health
        self.armour = armour
        self.attack = attack
        self.level = level
        self.xp = xp
 
 
#----- Various static Values ------#
hallway = Hall("Hallway")
 
key2 = Key("Key", "Room 1", 10001)
key3 = Key("Key", "Room 2", 20002)
key4 = Key("Key", "Room 3", 30003)
 
room1 = Room(1, "Room 1", False)
room2 = Room(2, "Room 2", False)
room3 = Room(3, "Room 3", False)
room4 = Room(4, "Room 4", False)
 
door1 = Door("Door 1", 1, False, None)
door2 = Door("Door 2", 2, True, 10001)
door3 = Door("Door 3", 3, True, 20002)
door4 = Door("Door 4", 4, True, 30003)
 
level1stats = [25, 5, 10, 1, 0]
player = Player("NoName", None)
player.stats(*level1stats)
 
level1monsterstats = [10, 0, 5, 1, 10]
wolf = Wolf("wolf", "Room 2")
wolf.stats(*level1monsterstats)
wolf2 = Wolf("wolf", "Room 3")
wolf2.stats(*level1monsterstats)
wolf3 = Wolf("wolf", "Room 4")
wolf3.stats(*level1monsterstats)
 
room_victory = False
exit_room = False
battle_status = True
room_count = 0
 
# Empty dictionaries
list_of_doors = {}
list_of_keys = {}
list_of_room_keys = {}
player_inventory = {}
list_of_rooms = {}
list_of_monsters = {}
list_of_room_monsters = {}
 
# Available actions for the loops
list_of_actions_available_room = ["grab", "leave", "fight", "stats", "location", "keys", "help"]
list_of_actions_available_true_main = ["enter", "exit", "stats", "location", "help"]
 
 
#----- Opening Setup------#
def opening_setup():
    """This opening setup gives us a player name and also provides the opening text"""
    global player
    name = raw_input("Whats your name?")
    player.name = name
    player.playerlocation = "Hallway"
    populate_rooms_list()
    populate_keys_list()
    populate_monsters_list()
    player_location()
    # The opening text to give a little story(will change later once we have some actual story)
    opening_text = "Hello and welcome to your adventure %r!\n" \
                   "You must have had one heck of a night last night" \
                   " because you don't know where you are or how you got here!\n" \
                   "Never fear, I'm sure you can figure it out!" % player.name
    print opening_text
 
 
#------- Room Populating function ----#
def populate_rooms_list():
    global list_of_rooms
    list_of_rooms[room1] = room1.name
    list_of_rooms[room2] = room2.name
    list_of_rooms[room3] = room3.name
    list_of_rooms[room4] = room4.name
 
 
def populate_door_list():
    global list_of_doors, player
    list_of_doors = {}
    if player.playerlocation == "Hallway":
        list_of_doors[door1] = door1.name
        list_of_doors[door2] = door2.name
        list_of_doors[door3] = door4.name
        list_of_doors[door4] = door3.name
    else:
        room = player.playerlocation
        for i in list_of_rooms:
            if i.name == room:
                room_number = i.number
                for x in list_of_doors:
                    if room_number == x.number:
                        door_name = x.name
                        list_of_doors[x] = door_name
                        break
 
 
def populate_monsters_list():
    global list_of_monsters
    list_of_monsters[wolf] = wolf.name
    list_of_monsters[wolf2] = wolf2.name
    list_of_monsters[wolf3] = wolf3.name
 
 
def populate_keys_list():
    global list_of_keys
    list_of_keys[key2] = key2.name
    list_of_keys[key3] = key3.name
    list_of_keys[key4] = key4.name
 
 
def populate_room_keys():
    global list_of_keys, list_of_room_keys, player
    for key in list_of_keys:
        if key.room == player.playerlocation:
            list_of_room_keys[key] = key.name
            key_choice = key
            del list_of_keys[key_choice]
            break
 
 
def populate_room_monster_list():
    global list_of_monsters, list_of_room_monsters
    list_of_room_monsters = {}
    for monster in list_of_monsters:
        if monster.room == player.playerlocation:
            list_of_room_monsters[monster] = monster.name
            break
 
 
# ------- Status Functions ------#
# These functions are there to display the info about the room/player on request
def visible_keys():
    global list_of_room_keys, player
    count = 0
    for key in list_of_room_keys:
        if key.room == player.playerlocation:
            count += 1
    if count == 0:
        print "There are no keys"
    else:
        print "You can see %r keys." % count
 
 
def visible_doors():
    count = 1
    if player.playerlocation == "Hallway":
        for x in list_of_doors:
            count += 1
        print "You can see %r doors numbered accordingly." % count
    else:
        print "You can see the door you came through"
 
 
def visible_monsters():
    global list_of_room_monsters
    for monster in list_of_room_monsters:
        print "You can see a %r!" % monster.name
 
 
def player_status():
    global player
    print "Your stats are:\nHealth: %r, Armour: %r, Attack: %r, Level: %r, Experience: %r" % \
          (player.health, player.armour, player.attack, player.level, player.xp)
 
 
def door_status(door):
        if door.locked == True:
            print "Door number %r is locked!" % door.number
        elif door.locked == False:
            print "Door number %r is unlocked!" % door.number
 
 
def player_location():
    print "You are in %r" % player.playerlocation
 
 
#-------- Player Functions --------#
def xp_check():
    """Checks player xp and necessary xp and calls the level up function if applicable"""
    global player
    xp_needed = player.level * 10 + 15
    if player.xp >= xp_needed:
        level_up()
        player.xp -= xp_needed
        print "You have leveled up!"
    else:
        xp_needed = player.level * 10 + 15
        print "Not enough xp to level up!", "You need %r" % xp_needed, "You have %r" % player.xp
 
 
def level_up():
    """this function performs the leveling up of the player"""
    global player
    player.health += 10
    player.attack += 5
    player.level += 1
 
 
def prompt_levelup():
    check_levelup = raw_input("Would you like to see if you leveled up?")
    if check_levelup == "yes":
        xp_check()
 
 
#------Help function ------#
def help_info():
    """Provides a information about the available prompts should the player need it"""
    while True:
        command = raw_input("What command would you like to know more about? If none, please type 'back'")
        if command == "enter":
            print "This command will move your character into the next room."
        elif command == "exit":
            print "This command exits the game! Careful!"
        elif command == "stats":
            print "This command provides you with info about your character."
        elif command == "grab":
            print "This command lets you grab any object. Simply say which one."
        elif command == "leave":
            print "This command lets you leave through any unlocked door"
        elif command == "doors":
            print "This command shows you what doors are visible."
        elif command == "keys":
            print "This command show you any keys you can see."
        elif command == "back":
            break
        elif command == "fight":
            print "This command lets you fight the monster"
        elif command == "location":
            print "This command tells you your current location."
        else:
            print "That's not a valid command!"
 
 
#------- Actions Functions --------#
def take_action(action):
    """This function takes the input of the engine for
    action and completes that action
    Note: This function is only accessible inside the room loop
    """
    global player, room_victory, exit_room, list_of_room_keys, list_of_keys, room_count
    if action == "grab":
        grab_object = raw_input("Grab what?")
        if grab_object == "keys":  # This lets the player grab all the keys in the room rather than one by one
            for i in list_of_room_keys:
                if i.name.lower() == "key":
                    player_inventory[i] = i.name
            for x in list_of_room_keys.keys():
                if x.name == "Key":
                    del list_of_room_keys[x]
            print "You grabbed the keys!!"
        elif grab_object == "key":
        # This is the alternate so that we can populate the room with other objects and grab those too later on
            for i in list_of_room_keys:
                if grab_object.lower() == i.name.lower():
                    player_inventory[i] = i.name
                    del list_of_room_keys[i]
                    print "You grabbed it!"
                    break
    elif action == "leave":
        for i in list_of_rooms:
            if i.name == player.playerlocation:
                current_room = i
                if current_room.victory == False:
                    room_xp = 25
                    player.xp += room_xp
                    print "Congrats you beat this room!"
                    print "You earned %r xp!" % room_xp
                    print "You exit the room!"
                    prompt_levelup()
                    current_room.victory = True
                    player.playerlocation = "Hallway"
                    exit_room = True
                    room_count += 1
                    if room_count >= 4:
                        print "Congrats! You beat the game!"
                        sys.exit()
                else:
                    print "You exit the room!"
                    player.playerlocation = "Hallway"
                    exit_room = True
    elif action == "fight":
        opponent_engine()
    elif action == "stats":
        player_status()
    elif action == "help":
        help_info()
    elif action == "Keys":
        visible_keys()
    elif action == "doors":
        visible_doors()
    elif action == "location":
        player_location()
    else:
        print "Your available actions while in the room are %s" % list_of_actions_available_room
 
 
def game_engine():
    """Game_engine is should maybe be called room_engine
    as its only function is to act as a go between for the main loop
    """
    global exit_room
    while exit_room == False:
        populate_door_list()
        visible_keys()
        visible_monsters()
        print "Your available actions while in the room are %s" % list_of_actions_available_room
        action = raw_input("What do you want to do?")
        take_action(action)
 
 
def monster_attack(monster):
    player.health -= (monster.attack - player.armour)
    if player.health <= 0:
        print "You have died! Better luck next time!"
        sys.exit()
 
 
def player_attack(monster):
    global battle_status, list_of_monsters, list_of_room_monsters
    monster.health -= (player.attack - monster.armour)
    if monster.health <= 0:
        print "You beat the monster!"
        for roommonster in list_of_monsters:
            if roommonster.room == player.playerlocation:
                del list_of_monsters[roommonster]
                break
        for roommonster in list_of_room_monsters:
            if roommonster.room == player.playerlocation:
                del list_of_room_monsters[roommonster]
                break
        player.xp += monster.xp
        prompt_levelup()
        battle_status = False
 
 
def battle_engine(monster):
    global battle_status
    while battle_status == True:
        monster_attack(monster)
        player_attack(monster)
 
 
def opponent_engine():
    global list_of_room_monsters, battle_status
    for monster in list_of_room_monsters:
        battle_status = True
        battle_engine(monster)
        break
 
#------ Main Loops ---------- #
def hall_room_transition():
    room_choice = raw_input("Which room would you like to enter?(please enter a number)")
    populate_door_list()
    for i in list_of_doors:
        if i.number == int(room_choice):
            door_choice = i
            door_number = i.number
            if door_choice.locked == True:
                print "The door seems to be locked. Maybe you need to use a key!"
                use_key = raw_input("Use a key? (yes or no)")
                if use_key.lower() == "yes":
                    for x in player_inventory:
                        if x.match == door_choice.match:
                            door_choice.locked = False
                            print "You used the key!"
                            door_status(door_choice)
                            enter_through_door = raw_input("Enter the room?")
                            if enter_through_door == "yes":
                                print "You entered the room!"
                                for room in list_of_rooms:
                                    if room.number == door_number:
                                        player.playerlocation = room.name
                                        break
                    else:
                        print "There are no matching keys in your inventory!"
                        break
                elif use_key.lower() == "no":
                    print "OK, but the door is still locked!"
            elif door_choice.locked == False:
                print "You entered the room!"
                for room in list_of_rooms:
                    if room.number == door_number:
                        player.playerlocation = room.name
 
 
def main():
    """This main function is the secondary loop that is operational while the player is in the room
    """
    global exit_room
    exit_room = False
    while player.playerlocation == "Hallway":
        hall_room_transition()
    else:
        populate_room_keys()
        populate_room_monster_list()
        game_engine()
 
 
def true_main():
    """True main is the upper loop
    This loop is my solution to dealing with generating a unique room each time
    """
    opening_setup()
    while True:
        raw_input("Press <Enter> to continue!")
        print "Your available actions while in the hallway are %s" % list_of_actions_available_true_main
        player.playerlocation = "Hallway"
        take_action_main = raw_input("What do you want to do?")
        if take_action_main == "enter":
            main()
        elif take_action_main == "exit":
            sys.exit()
        elif take_action_main == "stats":
            player_status()
        elif take_action_main == "help":
            help_info()
        elif take_action_main == "location":
            print player_location()
        else:
            print "That's not a valid command!"
 
 
#------- Game Operation --------#
true_main()