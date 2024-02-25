import pytest
from src.api.movesuggestion.moves_api import compute_effectiveness

def test_all_neutral_no_stab():
    move_num = compute_effectiveness(
        "normal", 80,
        "flying", 75,
        "ghost", 30,
        "psychic", 90,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == 4
    
def test_all_neutral_with_stab():
    move_num = compute_effectiveness(
        "dark", 80,
        "flying", 75,
        "ghost", 30,
        "psychic", 90,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == 1
    
def test_with_not_very_effective():
    move_num = compute_effectiveness(
        "normal", 80,
        "flying", 75,
        "ghost", 30,
        "bug", 90,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == 1

def test_quad_resist():
    move_num = compute_effectiveness(
        "normal", 21,
        "dragon", 21,
        "ghost", 21,
        "grass", 80,
        "Kingambit",
        "Volcarona"
    )
    assert move_num == 1

def test_with_super_effective():
    move_num = compute_effectiveness(
        "water", 80,
        "flying", 75,
        "ghost", 30,
        "bug", 90,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == 1
    
def test_with_four_times_super_effective():
    move_num = compute_effectiveness(
        "water", 80,
        "flying", 75,
        "ice", 45,
        "bug", 90,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == 3
    
def test_immune():
    move_num = compute_effectiveness(
        "ground", 80,
        "electric", 75,
        "normal", 45,
        "ground", 90,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == 3
    
def test_with_resisted_and_stab_less_power():
    move_num = compute_effectiveness(
        "normal", 80,
        "flying", 75,
        "fire", 45,
        "bug", 90,
        "Volcarona",
        "Landorus-Therian"
    )
    assert move_num == 1
    
def test_with_resisted_and_stab_more_power():
    move_num = compute_effectiveness(
        "normal", 70,
        "flying", 60,
        "normal", 45,
        "bug", 100,
        "Volcarona",
        "Landorus-Therian"
    )
    assert move_num == 4
    
def test_tie_all_neutral():
    move_num = compute_effectiveness(
        "normal", 80,
        "flying", 80,
        "ghost", 80,
        "psychic", 80,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == 1
    
def test_tie_diff_base_powers():
    move_num = compute_effectiveness(
        "water", 40,
        "ice", 20,
        "bug", 160,
        "psychic", 80,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == 1
    
def test_bad_move1type_input():
    move_num = compute_effectiveness(
        "not a type", 40,
        "ice", 20,
        "bug", 160,
        "psychic", 80,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == -1
    
def test_bad_move2type_input():
    move_num = compute_effectiveness(
        "ice", 20,
        "not a type", 40,
        "bug", 160,
        "psychic", 80,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == -1
    
def test_bad_move3type_input():
    move_num = compute_effectiveness(
        "ice", 20,
        "bug", 160,
        "not a type", 40,
        "psychic", 80,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == -1
    
def test_bad_move4type_input():
    move_num = compute_effectiveness(
        "ice", 20,
        "bug", 160,
        "psychic", 80,
        "not a type", 40,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == -1
    
def test_invalid_pokemon():
    move_num = compute_effectiveness(
        "ice", 20,
        "bug", 160,
        "psychic", 80,
        "water", 40,
        "not a pokemon",
        "Landorus-Therian"
    )
    assert move_num == -1
    
def test_invalid_enemy_pokemon():
    move_num = compute_effectiveness(
        "ice", 20,
        "bug", 160,
        "psychic", 80,
        "water", 40,
        "Landorus-Therian",
        "not a pokemon"        
    )
    assert move_num == -1
    
def test_negative_power():
    move_num = compute_effectiveness(
        "ice", 29,
        "fire", 49354,
        "water", 34,
        "ground", -1,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num == -1