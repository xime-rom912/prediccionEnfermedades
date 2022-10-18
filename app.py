import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st
from keras.models import load_model


# Path del modelo preentrenado
MODEL_PATH = 'models/model.h5'


# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds


def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        model = load_model('models/model.h5')
    
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">Sistema de prediccion de la enfermedad Cronica del riñon</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    # Lecctura de datos
    #Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    bp = st.text_input("Presión arterial:")
    sg = st.text_input("Ph:")
    al = st.text_input("Albúmina:")
    bu = st.text_input("Urea de sangre:")
    sc = st.text_input("Suero de creatinina:")
    sod = st.text_input("Sodio:")
    pot = st.text_input("Potasio:")
    hemo = st.text_input("Hemoglobina:")
    wbcc = st.text_input("Recuento de glóbulos blancos:")
    rbcc = st.text_input("Recuento de glóbulos rojos:")
    htn = st.text_input("Hipertensión:")
    
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.float_(bp.title()),
                    np.float_(sg.title()),
                    np.float_(al.title()),
                    np.float_(bu.title()),
                    np.float_(sc.title()),
                    np.float_(sod.title()),
                    np.float_(pot.title()),
                    np.float_(hemo.title()),
                    np.float_(wbcc.title()),
                    np.float_(rbcc.title()),
                    np.float_(htn.title())]
        predictS = model_prediction(x_in, model) 
        respuesta = ''
        if (predictS[0]>2000):
            respuesta='Si'
        else:
            respuesta='No'

        st.success('El paciente tiene una enfermedad cronica renal?: {}'.format(respuesta))

if __name__ == '__main__':
    main()
