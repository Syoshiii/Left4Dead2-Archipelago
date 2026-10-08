from BaseClasses import MultiWorld, Item, Tutorial, ItemClassification, LocationProgressType
from worlds.AutoWorld import World, CollectionState, WebWorld
from typing import Dict
from .Items import unique_item_dict, useful_items, junk_items, progression_items, campaign_names, filler_item_names, melee_weapon_names
from .Locations import get_location_names, get_total_locations
from .Options import L4D2Options, WeaponMode
from .Regions import create_regions
from .Rules import set_rules
from .Types import APSkeletonItem

class L4D2Web(WebWorld):
    theme = "Party"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Left 4 Dead 2 for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Yufii", "Syoshi"]
    )]

class L4D2World(World):
    """
    Left 4 Dead 2 is a cooperative FPS where you fight your way through hordes of zombies,
    and can also play as the Special Infected against the survivors.
    """
    game = "Left 4 Dead 2"
    item_name_to_id = unique_item_dict
    location_name_to_id = get_location_names()
    options_dataclass = L4D2Options
    options: L4D2Options
    web = L4D2Web()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def generate_early(self) -> None:
        # Campaigns the player starts with (removed from the item pool in create_items)
        if self.options.all_campaigns_start:
            self.starting_campaigns = list(campaign_names)
        else:
            # Option keys are the campaign names in snake_case ("dead_center" -> "Dead Center")
            key = self.options.starting_campaign.current_key
            self.starting_campaigns = [c for c in campaign_names if c.lower().replace(" ", "_") == key]
        for campaign_name in self.starting_campaigns:
            self.push_precollected(self.create_item(campaign_name))

        # Melee-only: random starting melee weapon (replaces the vanilla pistol in game)
        self.melee_only = self.options.weapon_mode == WeaponMode.option_melee_only
        self.starting_melee = self.random.choice(melee_weapon_names) if self.melee_only else None

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.options, self.player)

        # Melee-only: Gnome Chompski is won at a shooting gallery, impossible without guns.
        # Excluded = it can only hold filler, so it never blocks a seed.
        if self.melee_only:
            self.get_location("Gnome Chompski").progress_type = LocationProgressType.EXCLUDED

    def set_rules(self) -> None:
        set_rules(self)

    def get_filler_item_name(self) -> str:
        # Called by the core when it needs an extra item (plando, item links, start_inventory_from_pool)
        return self.random.choice(filler_item_names)

    def create_item(self, name: str) -> "APSkeletonItem":
        item_id: int = self.item_name_to_id[name]

        match name:
            case "Pump Shotgun":
                classification = ItemClassification.useful
            case "Chrome Shotgun":
                classification = ItemClassification.useful
            case "Submachine Gun":
                classification = ItemClassification.useful
            case "Silenced Submachine Gun":
                classification = ItemClassification.useful
            case "MP5":
                classification = ItemClassification.useful
            case "Tactical Shotgun":
                classification = ItemClassification.useful
            case "Combat Shotgun":
                classification = ItemClassification.useful
            case "Hunting Rifle":
                classification = ItemClassification.useful
            case "Sniper Rifle":
                classification = ItemClassification.useful
            case "M-16":
                classification = ItemClassification.useful
            case "Scar-H":
                classification = ItemClassification.useful
            case "AK-47":
                classification = ItemClassification.useful
            case "SG 552":
                classification = ItemClassification.useful
            case "Scout":
                classification = ItemClassification.filler
            case "AWP":
                classification = ItemClassification.filler
            case "The Passing":
                classification = ItemClassification.progression
            case "Dark Carnival":
                classification = ItemClassification.progression
            case "Swamp Fever":
                classification = ItemClassification.progression
            case "Hard Rain":
                classification = ItemClassification.progression
            case "The Parish":
                classification = ItemClassification.progression
            case "Cold Stream":
                classification = ItemClassification.progression
            case "No Mercy":
                classification = ItemClassification.progression
            case "Crash Course":
                classification = ItemClassification.progression
            case "Death Toll":
                classification = ItemClassification.progression
            case "Dead Air":
                classification = ItemClassification.progression
            case "Blood Harvest":
                classification = ItemClassification.progression
            case "The Sacrifice":
                classification = ItemClassification.progression
            case "The Last Stand":
                classification = ItemClassification.progression
            case "First Aid Kit":
                classification = ItemClassification.useful
            case "Defib":
                classification = ItemClassification.useful
            case "Pills":
                classification = ItemClassification.useful
            case "Adrenaline":
                classification = ItemClassification.useful
            case "Laser Sight":
                classification = ItemClassification.useful
            case "Incendiary":
                classification = ItemClassification.useful
            case "Explosive Ammo":
                classification = ItemClassification.useful
            case "Grenade Launcher":
                classification = ItemClassification.useful
            case "M60":
                classification = ItemClassification.useful
            case "Molotov":
                classification = ItemClassification.useful
            case "Pipe Bomb":
                classification = ItemClassification.useful
            case "Bile Bomb":
                classification = ItemClassification.useful
            case "Fireaxe":
                classification = ItemClassification.useful
            case "Baseball Bat":
                classification = ItemClassification.useful
            case "Cricket Bat":
                classification = ItemClassification.useful
            case "Crowbar":
                classification = ItemClassification.useful
            case "Frying Pan":
                classification = ItemClassification.useful
            case "Golf Club":
                classification = ItemClassification.useful
            case "Guitar":
                classification = ItemClassification.useful
            case "Katana":
                classification = ItemClassification.useful
            case "Machete":
                classification = ItemClassification.useful
            case "Nightstick":
                classification = ItemClassification.useful
            case "Pitchfork":
                classification = ItemClassification.useful
            case "Shovel":
                classification = ItemClassification.useful
            case "Knife":
                classification = ItemClassification.useful
            case "Chainsaw":
                classification = ItemClassification.useful
            case "Riot Shield":
                classification = ItemClassification.useful
            case "Gas Can":
                classification = ItemClassification.useful
            case "Oxygen Tank":
                classification = ItemClassification.useful
            case "Propane Tank":
                classification = ItemClassification.useful
            case "Fireworks":
                classification = ItemClassification.useful
            case "P220 Pistol":
                classification = ItemClassification.useful
            case "Glock":
                classification = ItemClassification.filler
            case "Gutted Medkit":
                classification = ItemClassification.filler
            case "Empty Gas Can":
                classification = ItemClassification.filler
            case "Expired Pills":
                classification = ItemClassification.filler
            case "Dud Pipe Bomb":
                classification = ItemClassification.filler
            case "Bent Laser Sight":
                classification = ItemClassification.filler
            case "Punctured Oxygen Tank":
                classification = ItemClassification.filler
            case "Magnum":
                classification = ItemClassification.useful
            case "Gnome Chompski":
                classification = ItemClassification.useful
            case "Dead Center":
                classification = ItemClassification.progression
            case _:
                raise Exception("Unexpected case met: classification cannot be set for unknown item \"" + name + "\"")

        return APSkeletonItem(name, classification, item_id, self.player)
    
    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {
            "options": {
                "L4D2DeathLink":            self.options.death_link.value,
                "StartWithCampaign":           self.options.starting_campaign.value,
                "AllCampaignsStart":               self.options.all_campaigns_start.value,
                "L4D2Goal":       self.options.goal.value,
                "WeaponMode":     self.options.weapon_mode.current_key  # "all_weapons" or "melee_only"
            },
            "Seed": self.multiworld.seed_name,
            "Slot": self.multiworld.player_name[self.player],
            "TotalLocations": get_total_locations(self),
            "StartingMelee": self.starting_melee  # melee-only: weapon that replaces the starting pistol (None otherwise)
        }
        slot_data["item_name_to_id"] = self.item_name_to_id
        slot_data["location_name_to_id"] = self.location_name_to_id

        return slot_data
    
    def create_items(self) -> None:
        all_items = []
        for name in progression_items.keys():
            if name not in self.starting_campaigns:
                all_items.append(name)
        if self.melee_only:
            # Melee-only: only healing items, throwables and melee weapons go in the pool.
            high_priority = ["First Aid Kit", "Defib", "Pills", "Adrenaline", "Molotov", "Pipe Bomb", "Bile Bomb"]
            for name in high_priority:
                all_items += [name] * 5
            for name in melee_weapon_names:
                all_items += [name] * 3
            junk_names = filler_item_names  # items that do nothing in game
        else:
            # All weapons: useful items in tiers
            high_priority = ["First Aid Kit", "Defib", "Pills", "Adrenaline", "Laser Sight", "Incendiary", "Explosive Ammo", "Molotov", "Pipe Bomb", "Bile Bomb", "Grenade Launcher", "M60"]
            for name in high_priority:
                all_items += [name] * 5
            medium_priority = ["Pump Shotgun", "Chrome Shotgun", "Submachine Gun", "Silenced Submachine Gun", "MP5", "Tactical Shotgun", "Combat Shotgun", "Hunting Rifle", "Sniper Rifle", "M-16", "Scar-H", "AK-47", "SG 552", "P220 Pistol", "Magnum", "Gnome Chompski"]
            for name in medium_priority:
                all_items += [name] * 4
            low_priority = [name for name in useful_items.keys() if name not in high_priority and name not in medium_priority]
            for name in low_priority:
                all_items += [name] * 3
            junk_names = list(junk_items.keys())
        # Fill the remaining locations with junk
        total_locations = get_total_locations(self)
        while len(all_items) < total_locations:
            all_items.append(self.random.choice(junk_names))
        self.multiworld.itempool += [self.create_item(item_name) for item_name in all_items]
    
    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)
    
    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)
