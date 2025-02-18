import streamlit as st
import streamlit.components.v1 as components

# Configurar el título de la página en el navegador
st.set_page_config(
    page_title="THE Selling System",
    page_icon="🏠",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': 'THE Selling System v1.0'
    }
)

# Personalizar la barra lateral
st.sidebar.title("🏠 THE Selling System")
st.sidebar.divider()

# Botón para mostrar la sección de Archivos
show_archivos = st.sidebar.button("Archivos")

# Mostrar solo el contenido HTML si se pulsa el botón "Archivos"
if show_archivos:
    st.sidebar.header("Archivos")
    components.html(
        """
        <style>
            html, body {
                width: 100%;
                height: 100%;
                margin: 0;
                padding: 0;
                overflow: hidden;
            }
            .chat-window-wrapper.n8n-chat, .chat-window {
                --chat--window--width: 100vw;
                --chat--window--height: 100vh;
            }
        </style>
        <link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet" />
        <div id="n8n-chat"></div>
        <script type="module">
            import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';

            createChat({
                webhookUrl: 'https://marta-pro-n8n.onrender.com:443/webhook/f406671e-c954-4691-b39a-66c90aa2f103/chat',
                container: '#n8n-chat'
            });
        </script>
        """,
        height=600  # Ajusta la altura según sea necesario
    )
else:
    # Contenido principal
    st.title("🏠 Bienvenido a THE Selling System")
    st.write("Selecciona una opción del menú lateral para comenzar.")
