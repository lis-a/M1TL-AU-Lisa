from Models.Player import Player
from Views.PlayerView import PlayerView
from Controllers.PlayerController import PlayerController
from unittest.mock import patch
import pytest


@pytest.fixture
def player_controller():
    return PlayerController()


@patch.object(PlayerView, 'get_player_info', return_value=('John', 'Doe', '2000-01-01', '12345'))
@patch.object(Player, 'save_player')
def test_add_player(mock_save_player, mock_get_player_info, player_controller):
    player_controller.add_player()
    mock_get_player_info.assert_called_once()
    mock_save_player.assert_called_once()
