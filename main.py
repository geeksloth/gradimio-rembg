import numpy as np
import gradio as gr
from time import sleep
from rembg import remove


def remove_background(input_img):
	output = remove(input_img)
	return output

demo = gr.Interface(remove_background, gr.Image(shape=(200, 200)), "image")
demo.launch(server_name="0.0.0.0")