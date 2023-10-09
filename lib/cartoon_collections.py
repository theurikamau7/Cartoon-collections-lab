def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    result = []
    for call in planeteer_calls:
        result.append(call.capitalize() + "!")
    return result

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None