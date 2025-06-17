from mcpq import Minecraft, Vec3, NBT, Block

mc = Minecraft()

def clear(x, y, z, width, height, depth):
    mc.setBlockCube("air", Vec3(x, y, z), Vec3(x + width, y + height, z + depth))

def choose_player() -> str:
    players = [player.name for player in mc.getPlayerList()]
    print(f"Player List: {players}")

    player_name = input("Choose a player: ")

    while player_name not in players:
        print(f"Player '{player_name}' not found! Try again.")
        player_name = input("Choose a player: ")

    print(f"Player '{player_name}' selected!")
    return player_name

def get_slot(nbt: NBT, number: int) -> tuple[Block | None, int | None]:
    slot = next((slot for slot in nbt["Inventory"] if slot["Slot"] == number), None)
    if slot is not None:
        return Block(slot["id"]), slot["count"]
    return None, None

def sort_pair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2

def block_save(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float, structure):
    x1, x2 = sort_pair(x1, x2)
    y1, y2 = sort_pair(y1, y2)
    z1, z2 = sort_pair(z1, z2)

    width = x2 - x1
    height = y2 - y1
    depth = z2 - z1

    print("Wait a minute...")

    for dz in range(int(depth + 1)):
        layer = []
        for dy in range(int(height + 1)):
            row = []
            for dx in range(int(width + 1)):
                block = Block(mc.getBlockWithData(Vec3(x1 + dx, y1 + dy, z1 + dz)))
                row.append(block)
            layer.append(row)
        structure.append(layer)
    return structure

def block_load(x, y, z, structure):
    print("Building...")
    for dz, layer in enumerate(structure):
        for dy, row in enumerate(layer):
            for dx, block in enumerate(row):
                    mc.setBlock(block, Vec3(x + dx, y + dy, z + dz))
