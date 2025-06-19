import random
import keyboard
from mcpq import Minecraft
from stuff import choose_player
from scripts.herobrineStructure import herobrine_structure
from scripts.tunnel import tunnel

mc = Minecraft()

print('=' * 10 + "Press a shortcut to do something" + '=' * 10)

def build_herobrine_structure():
    player_name = choose_player()
    player = mc.getPlayer(player_name)
    nbt = player.getNbt()
    selected_item_slot = nbt["SelectedItemSlot"]

    pos = player.pos
    x, y, z = pos.x, pos.y, pos.z
    herobrine_structure(x, y, z, player_name, nbt, selected_item_slot)

def build_tunnel():
    player_name = choose_player()
    player = mc.getPlayer(player_name)

    x, y, z = random.randint(0, 1000000), random.randint(-44, 0), random.randint(0, 1000000)
    tunnel(x, y, z, player, player_name)

keyboard.add_hotkey('ctrl+n', lambda: build_herobrine_structure())
keyboard.add_hotkey('ctrl+r', lambda: build_tunnel())
keyboard.wait('ctrl+home')