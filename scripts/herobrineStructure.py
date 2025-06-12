import random
import time
from mcpq import Minecraft, Vec3
from stuff import clear

mc = Minecraft()

blocks = ["air", "grass", "tall_grass"]
players = []

for randomPlayer in mc.getPlayerList():
    players.append(randomPlayer.name)

player = random.choice(players)

def isPlaceFree(func):
    def wrapper(x, y, z):
        front = mc.getBlock(Vec3(x + 2, y, z))
        side = mc.getBlock(Vec3(x, y, z + 2))
        if side in blocks and front in blocks:
            print(f"There are {side} in side and {front} in front")
            func(x, y, z)
        else:
            print(f"Error! There are {side} in side and {front} in front")
    return wrapper

@isPlaceFree
def herobrineStructure(x: float, y: float, z: float) -> None:
    mc.setBlockCube("gold_block", Vec3(x, y, z), Vec3(x + 2, y, z + 2))

    mc.setBlock("netherrack", Vec3(x + 1, y + 1, z + 1))

    mc.setBlock("redstone_torch", Vec3(x, y + 1, z))
    mc.setBlock("redstone_torch", Vec3(x + 2, y + 1, z))
    mc.setBlock("redstone_torch", Vec3(x, y + 1, z + 2))
    mc.setBlock("redstone_torch", Vec3(x + 2, y + 1, z + 2))

    mc.getPlayer(player).replaceItem("weapon.mainhand", "flint_and_steel")
    mc.postToChat("<Herobrine> Light my fire!")

    while True:
        if mc.getBlock(Vec3(x + 1, y + 2, z + 1)) == "fire":
            for i in range(100):
                mc.getPlayer(player).runCommand(f'summon minecraft:lightning_bolt {x + 1} {y + 2} {z + 1}')
                mc.getPlayer(player).runCommand(f"playsound minecraft:entity.ender_dragon.growl player @a {x + 1} {y + 2} {z + 1} 10000")
            mc.getPlayer(player).runCommand('title @a title {"text":"YOU WILL DIE!","color":"red"}')
            break
    time.sleep(3)
    clear(x, y, z, 2, 2, 2)


pos = player.pos
x, y, z = pos.x, pos.y, pos.z

herobrineStructure(x, y, z)