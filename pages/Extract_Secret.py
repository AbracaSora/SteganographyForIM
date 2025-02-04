#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
streamlit run app.py --server.port 8501
"""
import inspect
import os
import sys

cdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.insert(1, os.path.join(cdir, '../'))
from PIL import Image
from tools.augment_imagenetc import RandomImagenetC
import streamlit as st
from Embed_Secret import load_ecc, load_model, decode_secret

model_names = ['毕业设计', 'RivaGAN']
SECRET_LEN = 160

def app():
    st.title('信息隐写demo')
    # setup model
    model_name = st.selectbox("Choose the model", model_names)
    model, prep, tform = load_model(model_name)
    display_width = 300

    # setup st
    st.subheader("Input")
    image_file = None
    image_file = st.file_uploader("Upload stego image", type=["png","jpg","jpeg"])
    if image_file is not None:
        im = Image.open(image_file).convert('RGB')
        st.image(im, width=display_width)
        
    ecc = load_ecc('BCH')

    # add noise
    st.subheader("Corrupt")
    noise = RandomImagenetC(phase='test')
    corrupt_methods = [noise.method_names[i] for i in noise.corrupt_ids]

    corrupt_method = st.selectbox("Choose the corruption", ['None'] + corrupt_methods)
    if corrupt_method == 'None':
        corrupt_id = 999
    else:
        corrupt_id = noise.corrupt_ids[corrupt_methods.index(corrupt_method)]
    corrupt_strength = st.slider('Select the corrupt strength', 1, 5, value=1, step=1)
    
    # perform augment
    im_aug = None
    if image_file is not None:
        im_aug = im if corrupt_id==999 else noise(im, corrupt_id, corrupt_strength)
        st.image(im_aug, width=display_width)
        # im_aug = tform(im_aug).unsqueeze(0).cuda()

    # prediction
    st.subheader('Extract Secret')
    status = st.empty()
    if im_aug is not None:
        secret_pred = decode_secret(model_name, model, im_aug, tform)
        secret_decoded = ecc.decode_text(secret_pred)[0]
        status.markdown(f'Predicted secret: **{secret_decoded}**', unsafe_allow_html=True)
    
    # bit acc
    st.subheader('Accuracy')
    secret_text = st.text_input('Input groundtruth secret')
    bit_acc_status = st.empty()
    if secret_text:
        secret = ecc.encode_text([secret_text])  # (1, 100)
        bit_acc = (secret_pred == secret).mean()
        # bit_acc_status.markdown('**Bit Accuracy**: {:.2f}%'.format(bit_acc*100), unsafe_allow_html=True)
        word_acc = int(secret_decoded == secret_text)
        bit_acc_status.markdown(f'Bit Accuracy: **{bit_acc*100:.2f}%**<br />Word Accuracy: **{word_acc}**', unsafe_allow_html=True)

if __name__ == '__main__':
    app()
    