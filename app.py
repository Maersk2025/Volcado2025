import streamlit as st
import pandas as pd
import os
from datetime import datetime

EXCEL_FILE = "plan_vuelco.xlsx"

if not os.path.exists(EXCEL_FILE):
    df_init = pd.DataFrame(columns=[
        "USUARIO", "SEMANA", "FECHA", "TURNO", "PRODUCTO", "PRODUCTOR", "LOTE",
        "N° BINS", "KILOS", "H.INICIO", "H.FINAL", "COMENTARIOS", "TIMESTAMP"])
    df_init.to_excel(EXCEL_FILE, index=False)

st.title("Registro de Plan de Volcado de Producción")

with st.form("volcado_form"):
    usuario = st.text_input("Nombre del usuario")
    semana = st.text_input("Semana")
    fecha = st.date_input("Fecha")
    turno = st.selectbox("Turno", ["Mañana", "Tarde", "Noche"])
    producto = st.text_input("Producto")
    productor = st.text_input("Productor")
    lote = st.text_input("Lote")
    n_bins = st.number_input("N° Bins", min_value=0, step=1)
    kilos = st.number_input("Kilos", min_value=0.0, step=0.1)
    h_inicio = st.time_input("Hora de Inicio")
    h_final = st.time_input("Hora Final")
    comentarios = st.text_area("Comentarios")
    submitted = st.form_submit_button("Guardar")

    if submitted:
        df = pd.read_excel(EXCEL_FILE)
        new_row = {
            "USUARIO": usuario,
            "SEMANA": semana,
            "FECHA": fecha,
            "TURNO": turno,
            "PRODUCTO": producto,
            "PRODUCTOR": productor,
            "LOTE": lote,
            "N° BINS": n_bins,
            "KILOS": kilos,
            "H.INICIO": h_inicio.strftime("%H:%M"),
            "H.FINAL": h_final.strftime("%H:%M"),
            "COMENTARIOS": comentarios,
            "TIMESTAMP": datetime.now()
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        st.success("Datos guardados exitosamente")

st.subheader("Datos registrados")
try:
    df_display = pd.read_excel(EXCEL_FILE)
    st.dataframe(df_display)
except:
    st.warning("Aún no hay datos registrados.")
