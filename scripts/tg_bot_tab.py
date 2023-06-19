from modules import script_callbacks
import modules.scripts as scripts
import gradio as gr
import os
import subprocess
import sys

bot_main_file = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "bot_src/main.py"
)


process = None  # global variable to store the subprocess reference


def toggle_subprocess():
    global process
    if process is None or process.poll() is not None:
        env = os.environ.copy()
        env["PYTHONPATH"] = os.path.abspath(os.path.join(env["VENV_DIR"], os.pardir))
        process = subprocess.Popen([sys.executable, bot_main_file], env=env)
        return gr.Button.update(
            value="Stop Telegram Bot", variant="stop"
        ), gr.Textbox.update(value="Started Telegram Bot")
    else:
        process.terminate()
        return gr.update(
            value="Start Telegram Bot", variant="primary"
        ), gr.Textbox.update(value="Stopped Telegram Bot")


def on_ui_tabs():
    global logs
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Row():
            toggle_button = gr.Button("Start Telegram Bot", button_type="primary")
            logs = gr.Textbox(label="Logs", max_lines=1, readonly=True)
        toggle_button.click(toggle_subprocess, outputs=[toggle_button, logs])
        return [(ui_component, "Telegram Bot", "tg_bot_tab")]


script_callbacks.on_ui_tabs(on_ui_tabs)
