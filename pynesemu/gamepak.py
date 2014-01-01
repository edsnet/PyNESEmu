class GamePak(object):
    def __init__(self, f):
        assert f.read(4) == "NES\32"

        self.rom16count = ord(f.read(1))
        self.vrom8count = ord(f.read(1))
        self.ctrlbyte = ord(f.read(1))
        self.mappernum = ord(f.read(1)) | (self.ctrlbyte >> 4)

        f.read(8)

        self.rom = f.read(self.rom16count * 0x4000)
        self.vram = f.read(self.vrom8count * 0x2000)
