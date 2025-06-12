from mcpq import Minecraft, Vec3, NBT, Block

mc = Minecraft()

def clear(x, y, z, width, height, depth):
    mc.setBlockCube("air", Vec3(x, y, z), Vec3(x + width, y + height, z + depth))

def choose_player():
    players = [player.name for player in mc.getPlayerList()]
    print(f"Player List: {players}")
    player_name = input("Choose a player: ")
    if player_name in players:
        print(f"Player {player_name} selected!")
        return player_name
    else:
        print(f"Player {player_name} not found!")
        return None

def get_slot(nbt: NBT, number: int) -> tuple[Block | None, int | None]:
    slot = next((slot for slot in nbt["Inventory"] if slot["Slot"] == number), None)
    if slot is not None:
        return Block(slot["id"]), slot["count"]
    return None, None