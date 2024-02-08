# Imports

# Tuples = (Attacking move type, defending Pokemon type)

# normal, fire, water, grass, electric, ice
# fighting, poison, ground, flying, psychic, bug
# rock, ghost, dragon, dark, steel, fairy
normal_effectiveness_against = {
    ("normal", "normal"): , ("normal", "fire"): , ("normal", "water"): , ("normal", "grass"): , ("normal", "electric"): , ("normal", "ice"): ,
    ("normal", "fighting"): , ("normal", "poison"): , ("normal", "ground"): , ("normal", "flying"): , ("normal", "psychic"): , ("normal", "bug"): ,
    ("normal", "rock"): , ("normal", "ghost"): , ("normal", "dragon"): , ("normal", "dark"): , ("normal", "steel"): , ("normal", "fairy"): ,
}

def check_effectiveness(move, defending_pokemon):
    # Query the type of the move
    ## attacking_move_type =

    # Query type1 of the defending pokemon
    ##type1_scalar =

    # Query type2 of the defending pokemon
    ## type2_scalar =

    # Calculate effectiveness scalar
    total_scalar = type1_scalar * type2_scalar

    pass