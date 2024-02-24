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
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
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
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
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
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
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
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
def test_with_resisted_and_stab_less_power():
    move_num = compute_effectiveness(
        "normal", 80,
        "flying", 75,
        "ice", 45,
        "bug", 90,
        "Volcarona",
        "Landorus-Therian"
    )
    assert move_num == 1
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
def test_with_resisted_and_stab_more_power():
    move_num = compute_effectiveness(
        "normal", 70,
        "flying", 60,
        "ice", 45,
        "bug", 100,
        "Volcarona",
        "Landorus-Therian"
    )
    assert move_num == 4
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
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
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
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
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
def test_bad_move1type_input():
    move_num = compute_effectiveness(
        "not a type", 40,
        "ice", 20,
        "bug", 160,
        "psychic", 80,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num["error"] == "move1type is invalid"
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
def test_bad_move2type_input():
    move_num = compute_effectiveness(
        "ice", 20,
        "not a type", 40,
        "bug", 160,
        "psychic", 80,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num["error"] == "move2type is invalid"
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
def test_bad_move3type_input():
    move_num = compute_effectiveness(
        "ice", 20,
        "bug", 160,
        "not a type", 40,
        "psychic", 80,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num["error"] == "move3type is invalid"
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
def test_bad_move4type_input():
    move_num = compute_effectiveness(
        "ice", 20,
        "bug", 160,
        "psychic", 80,
        "not a type", 40,
        "Kingambit",
        "Landorus-Therian"
    )
    assert move_num["error"] == "move4type is invalid"
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
def test_invalid_pokemon():
    move_num = compute_effectiveness(
        "ice", 20,
        "bug", 160,
        "psychic", 80,
        "water", 40,
        "not a pokemon",
        "Landorus-Therian"
    )
    assert move_num["error"] == "Query error for pokemon types"
    
@pytest.mark.skip(reason="need to finish up queries in moves_api")
def test_invalid_enemy_pokemon():
    move_num = compute_effectiveness(
        "ice", 20,
        "bug", 160,
        "psychic", 80,
        "water", 40,
        "Landorus-Therian",
        "not a pokemon"        
    )
    assert move_num["error"] == "Query error for pokemon types"
    