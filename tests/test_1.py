from mcpq import Minecraft
from stuff import get_slot

mc = Minecraft()
player = mc.getPlayer()
nbt = player.getNbt()

selected_item_slot = nbt["SelectedItemSlot"]

item_name, item_number = "air", 0
mc.getPlayer().replaceItem("weapon.mainhand", item_name)