base_id = 69420000

progression_items = {
    "Dead Center": base_id + 1,
    "The Passing": base_id + 2,
    "Dark Carnival": base_id + 3,
    "Swamp Fever": base_id + 4,
    "Hard Rain": base_id + 5,
    "The Parish": base_id + 6,
    "Cold Stream": base_id + 7,
    "No Mercy": base_id + 8,
    "Crash Course": base_id + 9,
    "Death Toll": base_id + 10,
    "Dead Air": base_id + 11,
    "Blood Harvest": base_id + 12,
    "The Sacrifice": base_id + 13,
    "The Last Stand": base_id + 14,
}

# The 14 campaigns. Each campaign item unlocks the campaign of the same name.
campaign_names = list(progression_items.keys())

junk_items = {
    "Glock": base_id + 15,
    "AWP": base_id + 16,
    "Scout": base_id + 17,
    "Gutted Medkit": base_id + 658,
    "Empty Gas Can": base_id + 659,
    "Expired Pills": base_id + 660,
    "Dud Pipe Bomb": base_id + 661,
    "Bent Laser Sight": base_id + 662,
    "Punctured Oxygen Tank": base_id + 663,
}

# Junk items that do nothing in game. Used as filler when the core needs an extra item.
filler_item_names = [
    "Gutted Medkit",
    "Empty Gas Can",
    "Expired Pills",
    "Dud Pipe Bomb",
    "Bent Laser Sight",
    "Punctured Oxygen Tank",
]

# Melee weapons. In melee-only, one of them is the starting weapon (random per seed).
melee_weapon_names = [
    "Fireaxe",
    "Baseball Bat",
    "Cricket Bat",
    "Crowbar",
    "Frying Pan",
    "Golf Club",
    "Guitar",
    "Katana",
    "Machete",
    "Nightstick",
    "Pitchfork",
    "Shovel",
    "Knife",
    "Riot Shield",
]

useful_items = {
    "First Aid Kit": base_id + 18,
    "Defib": base_id + 19,
    "Pills": base_id + 20,
    "Adrenaline": base_id + 21,
    "Laser Sight": base_id + 22,
    "Incendiary": base_id + 23,
    "Explosive Ammo": base_id + 24,
    "Pump Shotgun": base_id + 25,
    "Chrome Shotgun": base_id + 26,
    "Submachine Gun": base_id + 27,
    "Silenced Submachine Gun": base_id + 28,
    "MP5": base_id + 29,
    "Tactical Shotgun": base_id + 30,
    "Combat Shotgun": base_id + 31,
    "Hunting Rifle": base_id + 32,
    "Sniper Rifle": base_id + 33,
    "M-16": base_id + 34,
    "Scar-H": base_id + 35,
    "AK-47": base_id + 36,
    "SG 552": base_id + 37,
    "Grenade Launcher": base_id + 38,
    "M60": base_id + 39,
    "Molotov": base_id + 40,
    "Pipe Bomb": base_id + 41,
    "Bile Bomb": base_id + 42,
    "Fireaxe": base_id + 43,
    "Baseball Bat": base_id + 44,
    "Cricket Bat": base_id + 45,
    "Crowbar": base_id + 46,
    "Frying Pan": base_id + 47,
    "Golf Club": base_id + 48,
    "Guitar": base_id + 49,
    "Katana": base_id + 50,
    "Machete": base_id + 51,
    "Nightstick": base_id + 52,
    "Pitchfork": base_id + 53,
    "Shovel": base_id + 54,
    "Knife": base_id + 55,
    "Chainsaw": base_id + 56,
    "Riot Shield": base_id + 57,
    "Gas Can": base_id + 58,
    "Oxygen Tank": base_id + 59,
    "Propane Tank": base_id + 60,
    "Fireworks": base_id + 61,
    "P220 Pistol": base_id + 62,
    "Magnum": base_id + 63,
    "Gnome Chompski": base_id + 64,
}

# All items, by name
unique_item_dict = {**useful_items, **junk_items, **progression_items}

