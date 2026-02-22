import json
import os

WOOD_TYPES = [
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

OUTPUT_DIR = "woodcutter_datapack/data/minecraft/woodcutter/recipes"


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def log_to_planks_name(log_name: str) -> str:
    if log_name.endswith("_log"):
        return log_name.replace("_log", "_planks")
    if log_name.endswith("_stem"):
        return log_name.replace("_stem", "_planks")
    raise ValueError(f"Unsupported wood type: {log_name}")


def generate_plank_to_slabs():
    for log in WOOD_TYPES:
        planks = log_to_planks_name(log)
        wood_type = planks.replace("_planks", "")

        recipe = {
            "type": "minecraft:stonecutting",
            "ingredient": {
                "item": f"minecraft:{planks}"
            },
            "result": f"minecraft:{wood_type}_slab",
            "count": 2
        }

        file_path = os.path.join(
            OUTPUT_DIR,
            f"{wood_type}_planks_to_slab.json"
        )

        with open(file_path, "w") as f:
            json.dump(recipe, f, indent=2)


def generate_plank_to_stairs():
    for log in WOOD_TYPES:
        planks = log_to_planks_name(log)
        wood_type = planks.replace("_planks", "")

        recipe = {
            "type": "minecraft:stonecutting",
            "ingredient": {
                "item": f"minecraft:{planks}"
            },
            "result": f"minecraft:{wood_type}_stairs",
            "count": 1
        }

        file_path = os.path.join(
            OUTPUT_DIR,
            f"{wood_type}_planks_to_stairs.json"
        )

        with open(file_path, "w") as f:
            json.dump(recipe, f, indent=2)


if __name__ == '__main__':
    ensure_output_dir()
    generate_plank_to_slabs()
    generate_plank_to_stairs()
    print("Recipes generated successfully!")