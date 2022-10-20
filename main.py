import numpy as np
import gradio as gr
from rembg import remove


def remove_background(input_img):
	print(type(input_img))
	output = remove(input_img)
	return output

demo = gr.Interface(remove_background, gr.Image(), "image")
demo.launch(server_name="0.0.0.0")