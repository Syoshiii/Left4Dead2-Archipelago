from BaseClasses import Region, Entrance, MultiWorld, ItemClassification
from .Types import L4D2Location, APSkeletonItem
from .Locations import location_table
from .Items import campaign_names
from .Options import L4D2Options

# Locations whose name does not start with "<Campaign> - "
extra_location_regions = {
    "Moustachio Strength": "Dark Carnival",
    "Moustachio Whack A Mole": "Dark Carnival",
    "Gnome Chompski": "Dark Carnival",
}

def completion_event_name(campaign_name: str) -> str:
    return f"{campaign_name} Completed"

def create_regions(world: MultiWorld, options: L4D2Options, player: int) -> None:
    regions = {"Menu": Region("Menu", player, world)}
    for campaign_name in campaign_names:
        regions[campaign_name] = Region(campaign_name, player, world)

    world.regions += regions.values()

    # Put every location in its campaign region
    for location_name, location_data in location_table.items():
        region = regions[get_region_for_location(location_name)]
        region.locations.append(L4D2Location(player, location_name, location_data.code, region))

    for campaign_name in campaign_names:
        region = regions[campaign_name]

        # Completion event: reached once the campaign region is reachable (chapters are linear)
        event_name = completion_event_name(campaign_name)
        event = L4D2Location(player, event_name, None, region)
        event.place_locked_item(APSkeletonItem(event_name, ItemClassification.progression, None, player))
        region.locations.append(event)

        # Menu -> campaign entrance
        entrance = Entrance(player, f"Menu to {campaign_name}", regions["Menu"])
        regions["Menu"].exits.append(entrance)
        entrance.connect(region)


def get_region_for_location(location_name: str) -> str:
    # Returns the campaign region of a location, from its name.
    if location_name in extra_location_regions:
        return extra_location_regions[location_name]
    campaign_name = location_name.split(" - ")[0]
    if campaign_name in campaign_names:
        return campaign_name
    raise Exception(f"No region found for location \"{location_name}\"")
