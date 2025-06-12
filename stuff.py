from mcpq import Minecraft, Vec3

mc = Minecraft()

def clear(x, y, z, width, height, depth):
    mc.setBlockCube("air", Vec3(x, y, z), Vec3(x + width, y + height, z + depth))