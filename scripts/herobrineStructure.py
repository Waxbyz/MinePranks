from time import sleep
from mcpq import Minecraft, Vec3, NBT
from stuff import clear, get_slot

mc = Minecraft()

blocks = ["air", "grass_block", "short_grass"]

def is_place_free(func):
    def wrapper(x, y, z, player, nbt: NBT, number: int):
        front = mc.getBlock(Vec3(x + 2, y, z))
        side = mc.getBlock(Vec3(x, y, z + 2))

        if side in blocks and front in blocks:
            print(f"Place is free at {x}, {y}, {z}")
            func(x, y, z, player, nbt, number)
        else:
            print(f"Error! Blocks detected: side={side}, front={front}")

    return wrapper

@is_place_free
def herobrine_structure(x: float, y: float, z: float, player, nbt: NBT, number: int) -> None:
    mc.setBlockCube("gold_block", Vec3(x, y, z), Vec3(x + 2, y, z + 2))

    mc.setBlock("netherrack", Vec3(x + 1, y + 1, z + 1))

    for dx, dy, dz in [(0, 1, 0), (2, 1, 0), (0, 1, 2), (2, 1, 2)]:
        mc.setBlock("redstone_torch", Vec3(x + dx, y + dy, z + dz))

    item_name, item_number = get_slot(nbt, number)
    print(item_name, item_number)

    if item_name is None:
        item_name = "air"
        mc.getPlayer(player).replaceItem("weapon.mainhand", "flint_and_steel")
    else:
        mc.getPlayer(player).replaceItem("weapon.mainhand", "flint_and_steel")

    mc.postToChat("<Herobrine> Light my fire!")

    while True:
        if mc.getBlock(Vec3(x + 1, y + 2, z + 1)) == "fire":
            if item_name == "air":
                mc.getPlayer(player).replaceItem("weapon.mainhand", item_name)
            else:
                mc.getPlayer(player).replaceItem("weapon.mainhand", item_name, item_number)

            for i in range(100):
                mc.getPlayer(player).runCommand(f'summon minecraft:lightning_bolt {x + 1} {y + 2} {z + 1}')
                mc.getPlayer(player).runCommand(f"playsound minecraft:entity.ender_dragon.growl player @a {x + 1} {y + 2} {z + 1} 10000")

            mc.getPlayer(player).runCommand('title @a title {"text":"YOU WILL DIE!","color":"red"}')
            break

    sleep(3)
    mc.runCommand("gamerule doTileDrops false")
    clear(x, y, z, 2, 2, 2)
    mc.runCommand("gamerule doTileDrops true")