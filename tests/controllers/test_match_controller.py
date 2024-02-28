from Controllers.MatchController import MatchController


def test_create_match_pairs():
    controller = MatchController()
    players = ['Player1', 'Player2', 'Player3', 'Player4']
    pairs = controller.create_match_pairs(players)
    assert len(pairs) == 2
    assert pairs[0] == ('Player1', 'Player2')
    assert pairs[1] == ('Player3', 'Player4')


def test_create_matches():
    controller = MatchController()
    pairs = [('Player1', 'Player2'), ('Player3', 'Player4')]
    matches = controller.create_matches(pairs)
    assert len(matches) == 2


def test_has_not_played_together():
    # Test case when players have not played together
    controller = MatchController()
    player1 = {'first_name': 'John', 'last_name': 'Doe'}
    player2 = {'first_name': 'Jane', 'last_name': 'Doe'}
    played_matches = [[('Player1', 'Player2')]]
    assert not controller.has_played_together(player1, player2, played_matches)
