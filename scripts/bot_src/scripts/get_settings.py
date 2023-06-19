import os
import json

bot_model_files = os.path.join(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir),
    "params",
)


def get_settings(model="illuminati_v1.1") -> dict:
    filename = os.path.join(f"{bot_model_files}/models.json")
    try:
        with open(filename, mode="r") as f:
            return json.loads(f.read())[model]
    except FileNotFoundError:
        return {}
