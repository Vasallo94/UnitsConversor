import streamlit as st
from astropy import units as u
from astropy.units import PhysicalType


# Función para obtener todas las unidades y sus tipos físicos
def obtener_unidades_y_tipos_fisicos():
    unidades_y_tipos = {}
    for unit_name in dir(u):
        unit = getattr(u, unit_name)
        if isinstance(unit, u.UnitBase):
            tipo_fisico = str(unit.physical_type)
            if tipo_fisico not in unidades_y_tipos:
                unidades_y_tipos[tipo_fisico] = []
            unidades_y_tipos[tipo_fisico].append(unit_name)
    return unidades_y_tipos

# Función para convertir unidades
def convertir_unidad_avanzada(valor, unidad_origen, unidad_destino):
    try:
        cantidad = valor * u.Unit(unidad_origen)
        resultado = cantidad.to(u.Unit(unidad_destino))
        tipo_fisico = resultado.unit.physical_type
        return resultado, tipo_fisico
    except Exception as e:
        return f"Error: {str(e)}", None

# Obtener unidades y tipos físicos
unidades_y_tipos = obtener_unidades_y_tipos_fisicos()

# Crear lista de tipos físicos
tipos_fisicos = sorted(unidades_y_tipos.keys())

# Interfaz de usuario de Streamlit
st.title("Conversor Avanzado de Unidades para Física")

tipo_fisico = st.selectbox("Seleccione el tipo físico", tipos_fisicos)

if tipo_fisico:
    unidades_compatibles = unidades_y_tipos[tipo_fisico]

    valor = st.number_input("Ingrese el valor", value=1.0)
    unidad_origen = st.selectbox("Seleccione la unidad de origen", unidades_compatibles)
    unidad_destino = st.selectbox("Seleccione la unidad de destino", unidades_compatibles)

    if st.button("Convertir"):
        resultado, tipo_fisico = convertir_unidad_avanzada(valor, unidad_origen, unidad_destino)
        if tipo_fisico:
            st.write(f"Resultado: {resultado} ({tipo_fisico})")
        else:
            st.write(f"Resultado: {resultado}")

st.sidebar.header("Información")
st.sidebar.write("Este conversor está diseñado para físicos avanzados utilizando astropy.")
st.sidebar.write("- Seleccione el tipo físico de la unidad que desea convertir en el menú desplegable.")
st.sidebar.write("- Ingrese el valor numérico de la cantidad que desea convertir en el campo de entrada.")
st.sidebar.write("- Seleccione la unidad de origen y la unidad de destino en los menús desplegables.")
st.sidebar.write("- Haga clic en el botón 'Convertir' para obtener el resultado de la conversión.")
st.sidebar.write("- El resultado se mostrará en la sección principal de la aplicación.")
