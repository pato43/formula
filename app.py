import streamlit as st
from fpdf import FPDF
import urllib.parse
import os

# Configuración visual
st.set_page_config(page_title="Inscripción Curso Python", page_icon="🐍", layout="centered")

# Estilos CSS
st.markdown("""
<style>
    .main { background-color: #f0f4fc; }
    h1, h2, h3 { color: #003366; }
    .stButton>button {
        background-color: #003366;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 16px;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("🐍 Curso de Python con Certificado Microsoft")
st.markdown("**Inicio:** Miércoles 28 de mayo · **Duración:** 3 meses · **Horario:** Martes y Miércoles, 4–5 p.m.")
st.markdown("**Modalidad:** En línea con clases en vivo (se graban) · **Costo:** $600 MXN por mes")
st.markdown("**Certificación oficial por Microsoft Partner** ✅")
st.markdown("---")

# Información bancaria
st.subheader("💳 Información para transferencia bancaria")
st.markdown("""
- **Nombre:** ALEXANDER EDUARDO ROJAS  
- **CLABE:** 138580000011747469  
- **Banco:** Ualá - ABC Capital  
- **Teléfono asociado:** 7225597963  
- **Concepto:** Curso Python + Tu nombre

📌 **Si deseas pagar con tarjeta de crédito o débito**, hay un **cargo adicional del 5%**.  
**Es obligatorio comunicarse por WhatsApp para procesar el pago y enviar el comprobante.**
""")

# Botón de WhatsApp
st.markdown("### 📲 ¿Tienes dudas o deseas pagar con tarjeta?")
whatsapp_url = "https://wa.me/527225597963?text=" + urllib.parse.quote("Hola, quiero inscribirme al curso de Python.")
st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="background-color:#25D366;color:white;border:none;border-radius:5px;padding:10px 20px;font-weight:bold;">💬 Enviar mensaje por WhatsApp</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("✍️ Formulario de Inscripción")

# Formulario
with st.form("formulario"):
    nombre = st.text_input("Nombre completo")
    correo = st.text_input("Correo electrónico")
    whatsapp = st.text_input("Número de WhatsApp")
    edad = st.number_input("Edad", min_value=10, max_value=100, step=1)
    nivel = st.slider("¿Qué tanto conoces de Python? (1 = Nada, 10 = Experto)", 1, 10, 3)
    submit = st.form_submit_button("📄 Generar constancia PDF")

# Función para limpiar texto
def limpiar_texto(texto):
    return texto.replace("–", "-").replace("—", "-")

# Función para generar PDF
def generar_pdf(nombre, correo, whatsapp, edad, nivel):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(200, 10, limpiar_texto("Inscripción - Curso de Python"), ln=True, align="C")

    # Info del curso
    pdf.set_font("Arial", "", 12)
    pdf.ln(5)
    pdf.cell(200, 10, limpiar_texto("Inicio: Miércoles 28 de mayo"), ln=True)
    pdf.cell(200, 10, limpiar_texto("Duración: 3 meses (Martes y Miércoles, 4-5 p.m.)"), ln=True)
    pdf.cell(200, 10, limpiar_texto("Modalidad: En línea, clases en vivo (se graban)"), ln=True)
    pdf.cell(200, 10, limpiar_texto("Costo: $600 MXN/mes"), ln=True)
    pdf.cell(200, 10, limpiar_texto("Certificación: Microsoft Partner"), ln=True)

    # Datos del alumno en tabla
    pdf.ln(10)
    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(60, 10, limpiar_texto("Campo"), 1, 0, 'C', True)
    pdf.cell(130, 10, limpiar_texto("Respuesta"), 1, 1, 'C', True)

    pdf.set_font("Arial", "", 12)
    campos = [
        ("Nombre completo", nombre),
        ("Correo electrónico", correo),
        ("WhatsApp", whatsapp),
        ("Edad", f"{edad} años"),
        ("Nivel de Python", f"{nivel}/10")
    ]
    for campo, valor in campos:
        pdf.cell(60, 10, limpiar_texto(campo), 1)
        pdf.cell(130, 10, limpiar_texto(valor), 1)
        pdf.ln()

    ruta = f"inscripcion_{nombre.replace(' ', '_')}.pdf"
    pdf.output(ruta)
    return ruta

# Descargar el PDF
if submit:
    if not nombre or not correo or not whatsapp:
        st.warning("⚠️ Por favor completa todos los campos obligatorios.")
    else:
        ruta_pdf = generar_pdf(nombre, correo, whatsapp, edad, nivel)
        with open(ruta_pdf, "rb") as f:
            st.success("✅ ¡Constancia generada correctamente!")
            st.download_button("📥 Descargar constancia PDF", f, file_name=os.path.basename(ruta_pdf))
        os.remove(ruta_pdf)
