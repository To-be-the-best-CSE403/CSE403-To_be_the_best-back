# from [py file that will be tested] import [thing being imported]

# Constants
no_effect_zero = 0
not_very_effective_halved = 0.5
not_very_effective_quarter = 0.25
normal_one = 1
super_effective_doubled = 2
super_effective_quadrupled = 4

# No effect
def test_no_effect_against_single_type():
    effectiveness_scalar = check_effectiveness('Shadow Ball', 'Eevee')
    assert effectiveness_scalar == no_effect_zero
    #pass

def test_no_effect_against_dual_type():
    effectiveness_scalar = check_effectiveness('Quick Attack', 'Gengar')
    assert effectiveness_scalar == no_effect_zero
    #pass

# Not very effective
def test_not_very_effective_against_single_type():
    effectiveness_scalar = check_effectiveness('Earthquake', 'Meganium')
    assert effectiveness_scalar == not_very_effective_halved
    #pass

def test_not_very_effective_against_dual_type_halved():
    effectiveness_scalar = check_effectiveness('Razor Leaf', 'Gengar')
    assert effectiveness_scalar == not_very_effective_halved
    #pass

def test_not_very_effective_against_dual_type_quarter():
    effectiveness_scalar = check_effectiveness('U-Turn', 'Gengar')
    assert effectiveness_scalar == not_very_effective_quarter
    #pass

# Normal damage
def test_normal_damage_against_single_type():
    effectiveness_scalar = check_effectiveness('Quick Attack', 'Eevee')
    assert effectiveness_scalar == normal_one
    #pass

def test_normal_damage_against_dual_type():
    effectiveness_scalar = check_effectiveness('Ice Beam', 'Gengar')
    assert effectiveness_scalar == normal_one
    #pass

# Super effective
def test_super_effective_against_single_type():
    effectiveness_scalar = check_effectiveness('Close Combat', 'Eevee')
    assert effectiveness_scalar == super_effective_doubled
    #pass

def test_super_effective_against_dual_type_doubled():
    effectiveness_scalar = check_effectiveness('Earthquake', 'Gengar')
    assert effectiveness_scalar == super_effective_doubled
    #pass

def test_super_effective_against_dual_type_quadrupled():
    effectiveness_scalar = check_effectiveness('Solar Beam', 'Gastrodon')
    assert effectiveness_scalar == super_effective_quadrupled
    #pass