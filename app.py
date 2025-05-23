import streamlit as st
from fpdf import FPDF
import os

st.set_page_config(page_title="Inscripción Curso Python", page_icon="🐍", layout="centered")

# Estilos
st.markdown("""
<style>
    .main { background-color: #f0f4fc; }
    h1, h2, h3 { color: #003366; }
    .stButton>button {
        background-color: #003366;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("📘 Inscripción al Curso de Python")
st.markdown("Por favor completa el formulario para generar tu constancia.")

# Formulario
with st.form("formulario"):
    nombre = st.text_input("Nombre completo")
    correo = st.text_input("Correo electrónico")
    whatsapp = st.text_input("Número de WhatsApp")
    edad = st.number_input("Edad", min_value=10, max_value=100, step=1)
    nivel = st.slider("¿Qué tanto conoces de Python? (1 = Nada, 10 = Experto)", 1, 10, 3)

    submit = st.form_submit_button("Generar PDF")

# Función para crear PDF
def generar_pdf(nombre, correo, whatsapp, edad, nivel):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(200, 10, "Inscripción - Curso de Python", ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Nombre completo: {nombre}", ln=True)
    pdf.cell(200, 10, f"Correo electrónico: {correo}", ln=True)
    pdf.cell(200, 10, f"Número de WhatsApp: {whatsapp}", ln=True)
    pdf.cell(200, 10, f"Edad: {edad} años", ln=True)
    pdf.cell(200, 10, f"Nivel de conocimiento en Python: {nivel}/10", ln=True)

    ruta = f"inscripcion_{nombre.replace(' ', '_')}.pdf"
    pdf.output(ruta)
    return ruta

# Generación y descarga
if submit:
    if not nombre or not correo or not whatsapp:
        st.warning("Por favor completa todos los campos.")
    else:
        ruta_pdf = generar_pdf(nombre, correo, whatsapp, edad, nivel)
        with open(ruta_pdf, "rb") as f:
            st.success("✅ ¡PDF generado con éxito!")
            st.download_button("📄 Descargar PDF", f, file_name=os.path.basename(ruta_pdf))
        os.remove(ruta_pdf)
