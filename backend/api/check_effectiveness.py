# Imports

# Tuples = (Attacking move type, defending Pokemon type)

# normal, fire, water, grass, electric, ice
# fighting, poison, ground, flying, psychic, bug
# rock, ghost, dragon, dark, steel, fairy
normal_effectiveness_against = {
    ("normal", "normal"): 1, ("normal", "fire"): 1, ("normal", "water"): 1, ("normal", "grass"): 1, ("normal", "electric"): 1, ("normal", "ice"): 1,
    ("normal", "fighting"): 1, ("normal", "poison"): 1, ("normal", "ground"): 1, ("normal", "flying"): 1, ("normal", "psychic"): 1, ("normal", "bug"): 1,
    ("normal", "rock"): 0.5, ("normal", "ghost"): 0, ("normal", "dragon"): 1, ("normal", "dark"): 1, ("normal", "steel"): 0.5, ("normal", "fairy"): 1,
}

def check_effectiveness(move, defending_pokemon):
    # Query the type of the move
    move_type = move['type']

    # Query type1 of the defending pokemon
    type1 = defending_pokemon['type1']

    # Query type2 of the defending pokemon
    type2 = defending_pokemon.get('type2')

    effectiveness1 = normal_effectiveness_against.get((move_type, type1))
    effectiveness2 = normal_effectiveness_against.get((move_type, type1))

    total_effectiveness = effectiveness1 * effectiveness2

    return total_effectiveness

    pass