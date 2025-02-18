import streamlit as st
import streamlit.components.v1 as components


# Configurar el título de la página en el navegador
st.set_page_config(
    page_title="The Selling System",
    page_icon="🏠",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': 'The Selling System v1.0'
    }
)

# Inicializar el estado de la sesión
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Función para cambiar de página
def switch_page(page_name):
    st.session_state.page = page_name

# Personalizar la barra lateral
st.sidebar.title("🏠 The Selling System")
st.sidebar.divider()



# Mostrar contenido según la página seleccionada
if st.session_state.page == 'archivos':
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
elif st.session_state.page == 'crear_cliente':
    crear_cliente()
elif st.session_state.page == 'Buscador de archivos':
    archivos()
else:
    # Contenido principal
    st.title("🏠 Bienvenido a The Selling System")
    st.write("Selecciona una opción del menú lateral para comenzar.")

# Descripción de la herramienta
st.write("""
### Marta: Tu Asistente de IA
Marta es una herramienta de inteligencia artificial diseñada para optimizar tus procesos de ventas. 
Con Marta, puedes gestionar clientes de manera eficiente y acceder a funcionalidades avanzadas de chat.

#### Funcionalidades de las Páginas:
- **Archivos:** Accede a un chat  que te permite interactuar y gestionar tus documentos de manera dinámica.
- **Crear Cliente:** Facilita la creación de nuevos clientes mediante un sencillo formulario que se conecta a nuestro sistema de backend.
""")
