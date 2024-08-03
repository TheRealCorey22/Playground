from npc import NPC, bestiary

npc_instances = {name: NPC(name, **attributes) for name, attributes in bestiary.items()}

# Display stats for all NPCs in the bestiary
for npc_name, npc in npc_instances.items():
    print(f"--- {npc_name} ---")
    npc.display_stats()
    print()
