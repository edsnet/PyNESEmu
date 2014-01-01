import os.path
from pynesemu.gamepak import GamePak

ROM = os.path.join(os.path.dirname(__file__), "Mega Man 2.nes")

def test_load():
    with open(ROM, "rb") as f:
        gp = GamePak(f)
        assert gp.rom16count == 16
        assert gp.vrom8count == 0
        assert gp.ctrlbyte == 0x11
        assert gp.mappernum == 1
