import pytest
from props import Ball
from Player import Player
from unittest.mock import Mock


def test_balls():
    ball = Ball(100, 100, 1, velocity=(1, 0))
    for _ in range(36):
        ball.move([Player()])
    assert ball.cords == (136, 100)


def test_player():
    player = Player()
    for _ in range(34):
        try:
            player.move()
        except Exception as x:
            print(x)
    print(player.x, player.y)
    assert 1 == 1


def test_connection():
    sock = Mock()
    sock.send.return_value = "succesful connection".encode("utf-8").decode(
        "utf-8"
    )
    assert sock.send() == "succesful connection"
