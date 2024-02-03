# from [py file that will be tested] import [thing being imported]

# Tests that the application can properly return the top 10 Pokemon and
# their usage rates for a given format
def test_gen9vgc2024_tier_pkmn_usage_rates():
    # using info from https://www.smogon.com/stats/2024-01/gen9vgc2024regfbo3-1760.txt
    expected = [['Flutter Mane', 71.86], ['Ogerpon-Wellspring', 45.96],
                ['Incineroar', 40.35], ['Amoonguss', 31.88],
                ['Urshifu', 30.36], ['Tornadus', 26.83],
                ['Raging Bolt', 25.72], ['Urshifu-Rapid-Strike', 25.34],
                ['Chien-Pao', 23.46], ['Rillaboom', 18.80]]
    pkmn_usage_rates = get_pkmn_usage_rate('gen9vgc2024')
    assert expected == pkmn_usage_rates
    #pass

# Tests that the application returns a given Pokemon's most used teammates in a given format
def test_gen9vgc2024_tier_flutter_mane_teammates():
    # using info from https://www.smogon.com/stats/2024-01/moveset/gen9vgc2024regfbo3-1760.txt
    expected = ['Ogerpon-Wellspring', 'Incineroar', 'Urshifu', 'Amoonguss', 'Raging Bolt',
                'Tornadus', 'Chien-Pao', 'Urshifu-Rapid-Strike', 'Rillaboom', 'Iron Hands',
                'Landorus']
    flutter_mane_teammates = get_pkm_teammates("gen9vgc2024", 'Flutter Mane')
    assert expected == flutter_mane_teammates
    #pass

# Tests that the application returns a given Pokemon's most used moves in a given format
def test_gen9vgc2024_tier_flutter_mane_moves():
    # using info from https://www.smogon.com/stats/2024-01/moveset/gen9vgc2024regfbo3-1760.txt
    expected = [['Moonblast', 95.57], ['Shadow Ball', 89.38],
                ['Dazzling Gem', 79.43], ['Icy Wind', 46.06],
                ['Protect', 41.66], ['Perish Song', 18.51],
                ['Power Gem', 5.95], ['Thunderbolt', 5.30],
                ['Other', 18.14]]
    flutter_mane_moves = get_pkm_moves("gen9vgc2024", 'Flutter Mane')
    assert expected = flutter_mane_moves
    #pass