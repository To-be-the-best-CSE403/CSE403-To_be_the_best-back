import pytest
from src.api.infoviewer.view_info_api import retrieve_info


def test_basic_moves():
    result = retrieve_info("Great Tusk", "moves")
    assert result == ("Rapid Spin: 93.599%\n" +
                    "Ice Spinner: 64.629%\n" +
                    "Headlong Rush: 64.402%\n" +
                    "Knock Off: 41.962%\n" +
                    "Close Combat: 36.289%\n" +
                    "Earthquake: 33.091%\n" +
                    "Bulk Up: 25.303%\n" +
                    "Stealth Rock: 21.372%\n" +
                    "Other: 19.354%")
    
def test_basic_items():
    result = retrieve_info("Great Tusk", "items")
    assert result == ("Leftovers: 29.169%\n" +
                    "Booster Energy: 26.196%\n" +
                    "Heavy-Duty Boots: 24.453%\n" +
                    "Assault Vest: 7.145%\n" +
                    "Rocky Helmet: 4.618%\n" +
                    "Eject Pack: 2.54%\n" +
                    "Choice Scarf: 1.782%\n" +
                    "Other: 4.097%")
                        
def test_basic_abilities():
    result = retrieve_info("Great Tusk", "abilities")
    assert result == ("Protosynthesis: 100.0%")
    
def test_basic_spreads():
    result = retrieve_info("Great Tusk", "spreads")
    assert result == ("Jolly:0/252/0/0/4/252: 24.798%\n" +
                    "Jolly:252/4/0/0/0/252: 13.755%\n" +
                    "Jolly:0/252/4/0/0/252: 11.888%\n" +
                    "Impish:252/0/252/0/4/0: 3.715%\n" +
                    "Impish:252/0/220/0/0/36: 3.226%\n" +
                    "Jolly:4/252/0/0/0/252: 2.815%\n" +
                    "Other: 39.803%")
    
def test_basic_teammates():
    result = retrieve_info("Great Tusk", "teammates")
    assert result == ("Kingambit: 26.354%\n" +
                    "Gholdengo: 20.863%\n" +
                    "Raging Bolt: 18.07%\n" +
                    "Slowking-Galar: 14.49%\n" +
                    "Dragapult: 13.965%\n" +
                    "Rillaboom: 12.722%\n" +
                    "Roaring Moon: 12.453%\n" +
                    "Kyurem: 12.271%\n" +
                    "Iron Valiant: 11.837%\n" +
                    "Samurott-Hisui: 11.654%\n" +
                    "Volcarona: 11.144%")
    
def test_malformed_input_casing():
    result = retrieve_info("GrEat tuSk", "teAmmatEs")
    assert result == ("Kingambit: 26.354%\n" +
                    "Gholdengo: 20.863%\n" +
                    "Raging Bolt: 18.07%\n" +
                    "Slowking-Galar: 14.49%\n" +
                    "Dragapult: 13.965%\n" +
                    "Rillaboom: 12.722%\n" +
                    "Roaring Moon: 12.453%\n" +
                    "Kyurem: 12.271%\n" +
                    "Iron Valiant: 11.837%\n" +
                    "Samurott-Hisui: 11.654%\n" +
                    "Volcarona: 11.144%")
    
def test_info_type_wrong():
    result = retrieve_info("GrEat tuSk", "wrong")
    assert result == ("")