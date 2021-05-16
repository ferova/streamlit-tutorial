import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

st.title("Upload + Classification Example")

with st.beta_expander('Plot single image.'):
    img_file_buffer = st.file_uploader("Choose an image...", type="jpg")

    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        st.image(image)


# Taken from https://github.com/aldencabajar/traffic_flow_counter/
def drawBoxes(frame, labels, boxes, confidences):
    # Box format: [x, y, w, h]
    boxColor = (128, 255, 0)  # very light green
    TextColor = (255, 255, 255)  # white
    boxThickness = 3
    textThickness = 2

    for lbl, box, conf in zip(labels, boxes, confidences):
        start_coord = tuple(box[:2])
        w, h = box[2:]
        end_coord = start_coord[0] + w, start_coord[1] + h

    # text to be included to the output image
        txt = '{} ({})'.format(
            lbl, round(conf, 3))
        frame = cv2.rectangle(frame, start_coord,
                              end_coord, boxColor, boxThickness)
        frame = cv2.putText(frame, txt, start_coord,
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, TextColor, 2)
    return frame


def DetermineBoxCenter(box):
    cx = int(box[0] + (box[2]/2))
    cy = int(box[1] + (box[3]/2))

    return [cx, cy]



with st.beta_expander('Plot image with annotations.'):
    img_file_buffer2 = st.file_uploader("Choose another image...", type="jpg")

    if img_file_buffer2 is not None:
        image2 = Image.open(img_file_buffer2)
        img_array2 = np.array(image2)
        st.image(image2)
        # This should come from a model
        boxes = [[322, 112, 433, 499]]
        scores = [1]
        label = ['cat']

        annotated = drawBoxes(img_array2, label, boxes, scores)
        st.image(annotated)
