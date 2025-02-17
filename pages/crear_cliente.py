import streamlit as st
import requests

# Configurar el título de la página y el ícono
st.set_page_config(
    page_title="Crear Cliente",
    page_icon="👥",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': 'THE Selling System v1.0'
    }
)

# Contenido principal
st.title("👥 Crear Cliente")

# Campo para insertar URL de documento de onboarding
document_url = st.text_input("Insertar URL de documento de onboarding")

# Opciones de tipo de cliente
client_type = st.radio("Selecciona el tipo de cliente", ("Básico", "Completo"))

# Botón para crear cliente
if st.button("Crear Cliente"):
    if document_url:
        # URL del webhook
        webhook_url = "HTTPS://marta-pro-n8n.onrender.com:443/webhook/c9ec5b66-1ef3-4c7b-8cd4-147911406ba9"
        
        # Datos a enviar en formato JSON
        data = {
            "document_url": document_url
        }
        
        # Enviar solicitud POST al webhook
        try:
            response = requests.get(webhook_url, json=data)  # Asegúrate de usar 'json=data' para enviar el cuerpo
            response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
            st.success(f"Cliente creado exitosamente con el documento: {document_url} y tipo: {client_type}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error al enviar datos al webhook: {e}")
    else:
        st.error("Por favor, inserta una URL de documento de onboarding.") 