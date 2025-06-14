import time
from mcpq import Minecraft, Vec3, Block, Player
from stuff import block_save

mc = Minecraft()
structure = []

def is_air_free(func):
    def wrapper(x, y, z, player, player_name):
        front = mc.getBlock(Vec3(x + 82, y, z))
        side = mc.getBlock(Vec3(x, y, z + 2))
        while front == "air" and side == "air":
            print(f"Error! Blocks detected: side={side}, front={front}. Try again.")

        print("Success!")
        func(x, y, z, player, player_name)
    return wrapper

@is_air_free
def tunnel(x: int, y: int, z: int, player: Player | str, player_name: str) -> None:
    mc.setBlockCube("air", Vec3(x, y, z), Vec3(x + 80, y + 1, z))

    mc.setBlockCube("deepslate", Vec3(x, y, z - 1), Vec3(x + 80, y + 1, z - 1))
    mc.setBlockCube("deepslate", Vec3(x, y, z + 1), Vec3(x + 80, y + 1, z + 1))
    mc.setBlockCube("deepslate", Vec3(x, y + 2, z), Vec3(x + 80, y + 2, z))
    mc.setBlockCube("deepslate", Vec3(x, y - 1, z), Vec3(x + 80, y - 1, z))
    mc.setBlock("deepslate", Vec3(x + 81, y, z))
    mc.setBlock("deepslate", Vec3(x + 81, y + 1, z))
    mc.setBlock("deepslate", Vec3(x - 1, y, z))
    mc.setBlock("deepslate", Vec3(x - 1, y + 1, z))

    mc.setBlock("bedrock", Vec3(x + 82, y, z))
    mc.setBlock("bedrock", Vec3(x + 82, y + 1, z))
    mc.setBlock("bedrock", Vec3(x - 2, y, z))
    mc.setBlock("bedrock", Vec3(x - 2, y + 1, z))

    for number in range(11):
        mc.setBlock(Block("redstone_wall_torch").withData({"facing": "south"}), Vec3(x, y + 1, z))
        x += 7

    mc.runCommand(f"effect give {player_name} darkness infinite")

    player.pos = Vec3(x + 1, y, z)

    while True:
        pos = player.pos
        x1, y1, z1 = pos.x, pos.y, pos.z

        for dx, dy, dz in [(0, -1, 0), (0, 2, 0), (0, 0, -1),
                           (0, 1, -1), (0, 0, 1), (0, 1, 1),]:
            block = mc.getBlock(Vec3(x1 + dx, y1 + dy, z1 + dz))\

            if block == "air":
                mc.setBlock("deepslate", Vec3(x1 + dx, y1 + dy, z1 + dz))

        time.sleep(0.1)