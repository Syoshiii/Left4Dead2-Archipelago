from typing import TYPE_CHECKING
from worlds.generic.Rules import set_rule
from .Items import campaign_names
from .Regions import completion_event_name

if TYPE_CHECKING:
    from . import L4D2World


def set_rules(world: "L4D2World") -> None:
    player = world.player

    # A campaign is playable once its campaign item is received
    for campaign_name in campaign_names:
        set_rule(world.get_entrance(f"Menu to {campaign_name}"),
                 lambda state, c=campaign_name: state.has(c, player))

    # Victory: finish `goal` campaigns
    completion_events = [completion_event_name(c) for c in campaign_names]
    required_campaigns = world.options.goal.value
    world.multiworld.completion_condition[player] = \
        lambda state: state.has_from_list(completion_events, player, required_campaigns)
