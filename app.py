import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="StormGuard.ai - Decision Intelligence",
    page_icon="⛈️",
    layout="wide"
)

def main():
    st.title("⛈️ StormGuard.ai")
    st.subheader("Inteligencia operativa y gestión de riesgo climático para logística y construcción.")
    
    st.markdown("---")
    
    # Panel de control interactivo básico
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🚚 Monitoreo de Activos")
        asset_id = st.text_input("ID del Activo / Camión", "camion_01")
        lat = st.number_input("Latitud", value=32.7767, format="%.4f")
        lon = st.number_input("Longitud", value=-96.7970, format="%.4f")
        
    with col2:
        st.markdown("### ⚠️ Estado de Alertas NOAA")
        st.info("Conectado al sistema de evaluación de polígonos meteorológicos.")
        
        # Simulación de verificación de riesgo
        if st.button("Verificar Riesgo Operativo", type="primary"):
            # Lógica de prueba para la interfaz
            if 32.0 <= lat <= 33.0 and -97.0 <= lon <= -96.0:
                st.error(f"🚨 [ALERTA EXTREMA] El activo '{asset_id}' se encuentra en zona de riesgo. Acción: DETENER/DESVIAR.")
            else:
                st.success(f"✅ El activo '{asset_id}' se encuentra en una ruta segura.")

    st.markdown("---")
    st.caption("StormGuard.ai SaaS B2B — Prevención de riesgos financieros por clima severo.")

if __name__ == "__main__":
    main()
