import json
import os

VANILLA_PREFIX = 'minecraft'
BIOMES_PREFIX = 'biomeswevegone'

VANILLA_WOOD_TYPES = [
    'oak_log',
    'spruce_log',
    'birch_log',
    'jungle_log',
    'acacia_log',
    'dark_oak_log',
    'mangrove_log',
    'cherry_log',
    'pale_oak_log',
    'crimson_stem',
    'warped_stem'
]

BIOMES_WOOD_TYPES = [
    "aspen_log",
    "baobab_log",
    "blue_enchanted_log",
    "cika_log",
    "cypress_log",
    "ebony_log",
    "fir_log",
    "florus_log",
    "green_enchanted_log",
    "holly_log",
    "ironwood_log",
    "jacaranda_log",
    "mahogany_log",
    "maple_log",
    "palm_log",
    "pine_log",
    "rainbow_eucalyptus_log",
    "redwood_log",
    "sakura_log",
    "skyris_log",
    "white_mangrove_log",
    "willow_log",
    "witch_hazel_log",
    "zelkova_log"
]

OUTPUT_DIR = "woodcutter_datapack/data/woodcutter/recipe"


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def log_to_planks_name(log_name: str) -> str:
    """
    Utility function for renaming where needed.
    """
    if log_name.endswith("_log"):
        return log_name.replace("_log", "_planks")
    if log_name.endswith("_stem"):
        return log_name.replace("_stem", "_planks")
    raise ValueError(f"Unsupported wood type: {log_name}")


def generate_plank_to_slabs(prefix, wood_types):
    for log in wood_types:
        planks = log_to_planks_name(log)
        wood_type = planks.replace("_planks", "")

        recipe = {
            "type": "minecraft:stonecutting",
            "ingredient": {
                "item": f"{prefix}:{planks}"
            },
            "result": {
                "id": f"{prefix}:{wood_type}_slab",
                "count": 2
            } 
        }

        file_path = os.path.join(
            OUTPUT_DIR,
            f"{wood_type}_planks_to_slab.json"
        )

        with open(file_path, "w") as f:
            json.dump(recipe, f, indent=2)


def generate_plank_to_stairs(prefix, wood_types):
    for log in wood_types:
        planks = log_to_planks_name(log)
        wood_type = planks.replace("_planks", "")

        recipe = {
            "type": "minecraft:stonecutting",
            "ingredient": {
                "item": f"{prefix}:{planks}"
            },
            "result": {
                "id": f"{prefix}:{wood_type}_stairs",
                "count": 1
            } 
        }

        file_path = os.path.join(
            OUTPUT_DIR,
            f"{wood_type}_planks_to_stairs.json"
        )

        with open(file_path, "w") as f:
            json.dump(recipe, f, indent=2)

def generate_log_to_fence(prefix, wood_types):
    # 1:2
    for log in wood_types:
        planks = log_to_planks_name(log)
        wood_type = planks.replace("_planks", "")

        recipe = {
            "type": "minecraft:stonecutting",
            "ingredient": {
                "item": f"{prefix}:{log}"
            },
            "result": {
                "id": f"{prefix}:{wood_type}_fence",
                "count": 2
            } 
        }

        file_path = os.path.join(
            OUTPUT_DIR,
            f"{log}s_to_fence.json"
        )

        with open(file_path, "w") as f:
            json.dump(recipe, f, indent=2)

def generate_log_to_fence_gate(prefix, wood_types):
    for log in wood_types:
        planks = log_to_planks_name(log)
        wood_type = planks.replace("_planks", "")

        recipe = {
            "type": "minecraft:stonecutting",
            "ingredient": {
                "item": f"{prefix}:{log}"
            },
            "result": {
                "id": f"{prefix}:{wood_type}_fence_gate",
                "count": 1
            } 
        }

        file_path = os.path.join(
            OUTPUT_DIR,
            f"{log}s_to_fence_gate.json"
        )

        with open(file_path, "w") as f:
            json.dump(recipe, f, indent=2)

if __name__ == '__main__':
    ensure_output_dir()

    prefix_and_wood_types = [
        (VANILLA_PREFIX, VANILLA_WOOD_TYPES), 
        (BIOMES_PREFIX, BIOMES_WOOD_TYPES)
    ]

    generators = [
        generate_plank_to_slabs, 
        generate_plank_to_stairs, 
        generate_log_to_fence,
        generate_log_to_fence_gate
    ]

    for prefix, wood_type in prefix_and_wood_types:
        for generator in generators:
            generator(prefix, wood_type)
    
    print("Recipes generated successfully!")