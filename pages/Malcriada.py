import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
        page_title="DEMO MALCRIADA",
        page_icon="📂",
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': 'THE Selling System v1.0'
        }
    )
st.title("🏠 DEMO MALCRIADA")
st.write("""
    Hablemos Mar)
""")

# Personalizar la barra lateral
st.sidebar.title("🏠 The Selling System")
st.sidebar.divider()
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
                --chat--window--height: 800px;
            }
            .chat-header {
                height: 0px !important;  /* Ajusta la altura a 0px */
            }
        </style>
        <link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet" />
        <div id="n8n-chat"></div>
        <script type="module">
            import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';

            createChat({
                webhookUrl: 'HTTPS://marta-pro-n8n.onrender.com:443/webhook/125fb5d7-e9ed-477d-a2e5-f09f16be506b/chat',
                container: '#n8n-chat',
                initialMessages: [
                    'Hola! 👋',
                    'Te estaba esperando.'
                ],
                mode: 'fullscreen'
            });
        </script>
        """,
        height=540  # Ajusta la altura según sea necesario
    ) 
