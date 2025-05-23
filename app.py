import streamlit as st
from fpdf import FPDF
import urllib.parse
import os

# Configuración inicial
st.set_page_config(page_title="Inscripción Curso Python", page_icon="🐍", layout="centered")

# Estilos personalizados
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

# Cabecera principal
st.title("🐍 Curso de Python con Certificado Microsoft")
st.markdown("**Inicio:** Miércoles 28 de mayo · **Duración:** 3 meses · **Horario:** Martes y Miércoles 4–5 p.m.")
st.markdown("**Modalidad:** En línea con clases en vivo (se graban) · **Costo:** $600 MXN por mes")
st.markdown("**Certificación oficial por Microsoft Partner** ✅")
st.markdown("---")

# Información bancaria real
st.subheader("💳 Información para transferencia bancaria")
st.markdown("""
- **Nombre:** ALEXANDER EDUARDO ROJAS  
- **CLABE:** 138580000011747469  
- **Banco:** Ualá - ABC Capital  
- **Teléfono asociado:** 7225597963  
- **Concepto:** Curso Python + Tu nombre

📌 **Si deseas pagar con tarjeta de crédito o débito**, comunícate primero por WhatsApp debido al cargo adicional del 5%.
""")

# Botón de WhatsApp directo
st.markdown("### 📲 ¿Tienes dudas o deseas pagar con tarjeta?")
whatsapp_url = "https://wa.me/527225597963?text=" + urllib.parse.quote("Hola, quiero inscribirme al curso de Python.")
st.markdown(f"[Haz clic aquí para escribirme por WhatsApp 🚀]({whatsapp_url})")

st.markdown("---")
st.subheader("✍️ Formulario de Inscripción")

# Formulario interactivo
with st.form("formulario"):
    nombre = st.text_input("Nombre completo")
    correo = st.text_input("Correo electrónico")
    whatsapp = st.text_input("Número de WhatsApp")
    edad = st.number_input("Edad", min_value=10, max_value=100, step=1)
    nivel = st.slider("¿Qué tanto conoces de Python? (1 = Nada, 10 = Experto)", 1, 10, 3)

    submit = st.form_submit_button("📄 Generar constancia PDF")

# Función para crear el PDF personalizado
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

# Generación y descarga del PDF
if submit:
    if not nombre or not correo or not whatsapp:
        st.warning("⚠️ Por favor completa todos los campos obligatorios.")
    else:
        ruta_pdf = generar_pdf(nombre, correo, whatsapp, edad, nivel)
        with open(ruta_pdf, "rb") as f:
            st.success("✅ ¡Constancia generada correctamente!")
            st.download_button("📥 Descargar constancia PDF", f, file_name=os.path.basename(ruta_pdf))
        os.remove(ruta_pdf)
