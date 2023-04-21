import gradio as gr
from fastai.vision.all import *

# Load learner
learn = load_learner('model_linux.pkl')

categories = ('Tumor Tissue', 'Non-tumor Tissue')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

image = gr.inputs.Image(shape=(96, 96))
label = gr.outputs.Label()

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label)
intf.launch(inline=False)