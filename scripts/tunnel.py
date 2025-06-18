import time
from mcpq import Minecraft, Vec3, Block, Player
from mcpq.text import RED, ILLEGIBLE
from stuff import block_load, block_save

mc = Minecraft()
structure = []

def is_place_free(func):
    def wrapper(x, y, z, player, player_name):
        front = mc.getBlock(Vec3(x + 83, y, z))
        side = mc.getBlock(Vec3(x, y, z + 2))

        while front == "air" and side == "air":
            print(f"Error! Blocks detected: side={side}, front={front}. Try again.")

        print("Success!")
        func(x, y, z, player, player_name)
    return wrapper

@is_place_free
def tunnel(x: int, y: int, z: int, player: Player | str, player_name: str) -> None:
    start_x = x
    start_y = y
    start_z = z

    block_save(start_x - 3, start_y + 2, start_z - 1, start_x + 83, -64, start_z + 1, structure)

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
        mc.setBlock(Block("redstone_wall_torch").withData({"facing": "north"}), Vec3(x, y + 1, z))
        x += 7

    mc.runCommand(f"effect give {player_name} darkness infinite")

    player.pos = Vec3(start_x, start_y, start_z)

    time.sleep(1)

    while True:
        pos = player.pos
        x1, y1, z1 = pos.x, pos.y, pos.z

        if x1 > start_x + 72:
            mc.postToChat(RED + ILLEGIBLE + "LET HIM COOK NOW LET HIM COOK I SAID LET HIM COOK!")
            for idk in range(100):
                mc.setBlockCube("air", Vec3(start_x, start_y, start_z), Vec3(start_x + 80, -64, start_z))
                time.sleep(0.1)
            time.sleep(10)
            block_load(start_x, -64, start_z, structure)
            structure.clear()
            break

        for dx, dy, dz in [(0, -1, 0), (0, 2, 0), (0, 0, -1),
                           (0, 1, -1), (0, 0, 1), (0, 1, 1),]:
            block = mc.getBlock(Vec3(x1 + dx, y1 + dy, z1 + dz))

            if block == "air":
                mc.setBlock("deepslate", Vec3(x1 + dx, y1 + dy, z1 + dz))

        time.sleep(0.1)