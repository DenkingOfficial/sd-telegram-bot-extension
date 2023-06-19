import modules.scripts as scripts
import gradio as gr
import os

from modules import shared
from modules import script_callbacks


def on_ui_settings():
    section = ("telegram-bot-settings", "Telegram bot settings")
    shared.opts.add_option(
        "tg_bot_token",
        shared.OptionInfo(
            "",
            "Telegram bot token",
            section=section,
        ),
    )
    shared.opts.add_option(
        "tg_api_id",
        shared.OptionInfo(
            "",
            "Telegram API ID",
            section=section,
        ),
    )
    shared.opts.add_option(
        "tg_api_hash",
        shared.OptionInfo(
            "",
            "Telegram API Hash",
            section=section,
        ),
    )


script_callbacks.on_ui_settings(on_ui_settings)
