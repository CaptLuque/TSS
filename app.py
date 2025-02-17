import streamlit as st

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
st.sidebar.image("https://via.placeholder.com/150", width=150)
st.sidebar.title("🏠 THE Selling System")
st.sidebar.divider()

# Contenido principal
st.title("🏠 Bienvenido a THE Selling System")
st.write("Selecciona una opción del menú lateral para comenzar.")

# Puedes agregar más contenido informativo aquí
st.markdown("""
### Funcionalidades disponibles:
- 👥 Crear Cliente
- 📊 Más funcionalidades próximamente...
""")
