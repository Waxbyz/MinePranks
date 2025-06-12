import keyboard
from mcpq import Minecraft
from stuff import choose_player
from scripts.herobrineStructure import herobrine_structure

mc = Minecraft()
player_name = choose_player()
player = mc.getPlayer(player_name)
nbt = player.getNbt()
selected_item_slot = nbt["SelectedItemSlot"]

def build_herobrine_structure():
    pos = player.pos
    x, y, z = pos.x, pos.y, pos.z
    herobrine_structure(x, y, z, player_name, nbt, selected_item_slot)

keyboard.add_hotkey('ctrl+n', lambda: build_herobrine_structure())
keyboard.wait('ctrl+home')
