from Models.Match import Match


def test_serialize():
    # Create a Match instance
    player1 = {'first_name': 'John', 'last_name': 'Doe'}
    player2 = {'first_name': 'Jane', 'last_name': 'Doe'}
    match = Match(player1, player2)

    # Test the serialize method
    serialized_match = match.serialize()
    assert serialized_match == {'player1': player1, 'player2': player2, 'winner': None}


def test_str():
    # Create a Match instance
    player1 = {'first_name': 'John', 'last_name': 'Doe'}
    player2 = {'first_name': 'Jane', 'last_name': 'Doe'}
    match = Match(player1, player2)

    # Test the __str__ method
    match_string = str(match)
    assert match_string == "John Doe VS Jane Doe"
