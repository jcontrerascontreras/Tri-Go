import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.title("Tri-Go!")
col2 = st.empty()
col1, col2 = st.columns(2)

# Función para graficar el triángulo rectángulo
def graficar_triangulo(a, b, alpha):
    # Calcular los otros lados y ángulos
    c = np.sqrt(a**2 + b**2)
    beta = 90 - alpha

    # Coordenadas de los vértices del triángulo
    vertices = np.array([[0, 0], [b, 0], [0, a]])

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Dibujar el triángulo
    ax.plot(vertices[:, 0], vertices[:, 1], 'b-')
    ax.fill(vertices[:, 0], vertices[:, 1], alpha=0.6)

    # Etiquetar los vértices
    for i, txt in enumerate(['C', 'A', 'B']):
        ax.annotate(txt, (vertices[i, 0], vertices[i, 1]), textcoords="offset points", xytext=(5,-6), ha='center')

    # Configurar límites y aspecto
    ax.set_xlim([-1, max(b, 1.2*c)])
    ax.set_ylim([-1, max(a, 1.2*c)])
    ax.set_aspect('equal')
    ax.grid(True)

    # Mostrar los ángulos
    ax.text(b/2, -0.5, f'b= {b}', ha='center')
    ax.text(-0.5, a/2, f'a= {a}', va='center', rotation='vertical')
    ax.text(0.2, 0.2, r'$C$')
    ax.text(b-0.8, 0.2, r'$α$')
    ax.text(0.1, a-0.8, r'$β$')

    # Mostrar la imagen del triángulo
    st.pyplot(fig)

def calculo_opcion_1(cateto_a, cateto_b):
    # Calcular la hipotenusa
    hipotenusa = round(math.sqrt(cateto_a**2 + cateto_b**2), 2)
    
    # Calcular los ángulos en radianes
    angulo_a_rad = math.atan(cateto_a / cateto_b)
    angulo_b_rad = math.atan(cateto_b / cateto_a)
    
    # Convertir los ángulos a grados
    angulo_a_gra = math.degrees(angulo_a_rad)
    angulo_b_gra = math.degrees(angulo_b_rad)
    
    # Mostrar los resultados
    st.write(f"**Cateto a:** {cateto_a}, ", f"**Cateto b:** {cateto_b}")
    st.write(f"**Hipotenusa:** {hipotenusa:.2f}, ", f"**Ángulo A (opuesto a cateto a):** {angulo_a_gra:.2f} grados")
    st.write(f"**Ángulo B (opuesto a cateto b):** {angulo_b_gra:.2f} grados")

    graficar_triangulo(cateto_a, cateto_b, angulo_a_gra)

def calculo_opcion_2(cateto_a:float, hipotenusa:float):
    cateto_b = round(math.sqrt(hipotenusa**2 - cateto_a**2), 2)

    angulo_a_rad = math.asin(cateto_a / hipotenusa)

    angulo_a_gra = math.degrees(angulo_a_rad)
    angulo_b_gra = 90-angulo_a_gra

    # Mostrar los resultados
    st.write(f"**Cateto a:** {cateto_a}, ", f"**Cateto b:** {cateto_b}")
    st.write(f"**Hipotenusa:** {hipotenusa:.2f}, ", f"**Ángulo A (opuesto a cateto a):** {angulo_a_gra:.2f} grados")
    st.write(f"**Ángulo B (opuesto a cateto b):** {angulo_b_gra:.2f} grados")

    graficar_triangulo(cateto_a, cateto_b, angulo_a_gra)

def calculo_opcion_3(cateto_b, hipotenusa):
    cateto_a = round(math.sqrt(hipotenusa**2 - cateto_b**2), 2)

    angulo_a_rad = math.acos(cateto_b / hipotenusa)

    angulo_a_gra = math.degrees(angulo_a_rad)
    angulo_b_gra = 90-angulo_a_gra

    # Mostrar los resultados
    st.write(f"**Cateto a:** {cateto_a}, ", f"**Cateto b:** {cateto_b}")
    st.write(f"**Hipotenusa:** {hipotenusa:.2f}, ", f"**Ángulo A (opuesto a cateto a):** {angulo_a_gra:.2f} grados")
    st.write(f"**Ángulo B (opuesto a cateto b):** {angulo_b_gra:.2f} grados")

    graficar_triangulo(cateto_a, cateto_b, angulo_a_gra)

def calculo_opcion_4(cateto_a, angulo_a):

    angulo_a_rad = math.radians(angulo_a)
    hipotenusa = round(cateto_a / math.sin(angulo_a_rad), 2)
    cateto_b = round(hipotenusa *  math.cos(angulo_a_rad), 2)
    angulo_b_gra = 90-angulo_a

    # Mostrar los resultados
    st.write(f"**Cateto a:** {cateto_a}, ", f"**Cateto b:** {cateto_b}")
    st.write(f"**Hipotenusa:** {hipotenusa:.2f}, ", f"**Ángulo A (opuesto a cateto a):** {angulo_a:.2f} grados")
    st.write(f"**Ángulo B (opuesto a cateto b):** {angulo_b_gra:.2f} grados")

    graficar_triangulo(cateto_a, cateto_b, angulo_a)

def calculo_opcion_5(cateto_b, angulo_a):
    angulo_a_rad = math.radians(angulo_a)
    hipotenusa = round(cateto_b / math.cos(angulo_a_rad), 2)
    cateto_a = round(hipotenusa *  math.sin(angulo_a_rad), 2)
    angulo_b_gra = 90-angulo_a

    # Mostrar los resultados
    st.write(f"**Cateto a:** {cateto_a}, ", f"**Cateto b:** {cateto_b}")
    st.write(f"**Hipotenusa:** {hipotenusa:.2f}, ", f"**Ángulo A (opuesto a cateto a):** {angulo_a:.2f} grados")
    st.write(f"**Ángulo B (opuesto a cateto b):** {angulo_b_gra:.2f} grados")

    graficar_triangulo(cateto_a, cateto_b, angulo_a)

def calculo_opcion_6(cateto_a, angulo_b):
    angulo_b_rad = math.radians(angulo_b)
    hipotenusa = round(cateto_a / math.sin(angulo_b_rad), 2)
    cateto_b = round(hipotenusa *  math.cos(angulo_b_rad), 2)
    angulo_a_gra = 90-angulo_b

    # Mostrar los resultados
    st.write(f"**Cateto a:** {cateto_a}, ", f"**Cateto b:** {cateto_b}")
    st.write(f"**Hipotenusa:** {hipotenusa:.2f}, ", f"**Ángulo A (opuesto a cateto a):** {angulo_a_gra:.2f} grados")
    st.write(f"**Ángulo B (opuesto a cateto b):** {angulo_b:.2f} grados")

    graficar_triangulo(cateto_a, cateto_b, angulo_a_gra)

def calculo_opcion_7(cateto_a, angulo_b):
    angulo_b_rad = math.radians(angulo_b)
    hipotenusa = round(cateto_a / math.sin(angulo_b_rad), 2)
    cateto_b = round(hipotenusa *  math.cos(angulo_b_rad), 2)
    angulo_a_gra = 90-angulo_b

    # Mostrar los resultados
    st.write(f"**Cateto a:** {cateto_a}, ", f"**Cateto b:** {cateto_b}")
    st.write(f"**Hipotenusa:** {hipotenusa:.2f}, ", f"**Ángulo A (opuesto a cateto a):** {angulo_a_gra:.2f} grados")
    st.write(f"**Ángulo B (opuesto a cateto b):** {angulo_b:.2f} grados")

    graficar_triangulo(cateto_a, cateto_b, angulo_a_gra)

def calculo_opcion_8(hipotenusa, angulo_a):
    angulo_a_rad = math.radians(angulo_a)
    cateto_a = round(hipotenusa * math.sin(angulo_a_rad), 2)
    cateto_b = round(hipotenusa * math.cos(angulo_a_rad), 2)
    angulo_b_gra = 90-angulo_a

    # Mostrar los resultados
    st.write(f"**Cateto a:** {cateto_a}, ", f"**Cateto b:** {cateto_b}")
    st.write(f"**Hipotenusa:** {hipotenusa:.2f}, ", f"**Ángulo A (opuesto a cateto a):** {angulo_a:.2f} grados")
    st.write(f"**Ángulo B (opuesto a cateto b):** {angulo_b_gra:.2f} grados")

    graficar_triangulo(cateto_a, cateto_b, angulo_a)

def calculo_opcion_9(hipotenusa, angulo_b):
    angulo_b_rad = math.radians(angulo_b)
    cateto_a = round(hipotenusa * math.cos(angulo_b_rad), 2)
    cateto_b = round(hipotenusa * math.sin(angulo_b_rad), 2)
    angulo_a_gra = 90-angulo_b

    # Mostrar los resultados
    st.write(f"**Cateto a:** {cateto_a}, ", f"**Cateto b:** {cateto_b}")
    st.write(f"**Hipotenusa:** {hipotenusa:.2f}, ", f"**Ángulo A (opuesto a cateto a):** {angulo_a_gra:.2f} grados")
    st.write(f"**Ángulo B (opuesto a cateto b):** {angulo_b:.2f} grados")

    graficar_triangulo(cateto_a, cateto_b, angulo_a_gra)


# Función principal de la aplicación
def main():
    opciones = ["Selecciona una opción", "Cateto a y cateto b", "Cateto a e hipotenusa", "Cateto b e hipotenusa", "Ángulo α y cateto a", "Ángulo α y cateto b", "Ángulo β y cateto a", "Ángulo β y cateto b","Ángulo α e hipotenusa", "Ángulo β e hipotenusa"]
    opcion = st.selectbox("Selecciona la opción que prefieras", opciones)

    if opcion == "Cateto a y cateto b":
        lado_a = st.number_input('Ingresa el valor del lado a (cateto)', min_value=0.0, step=1.0)
        lado_b = st.number_input('Ingresa el valor del lado b (cateto)', min_value=0.0, step=1.0)
        if st.button("Graficar"):
            if lado_a>0 and lado_b>0:
                with col2:
                    calculo_opcion_1(lado_a, lado_b)
            else:
                st.warning("Digita datos apropiados")
    elif opcion == "Cateto a e hipotenusa":
        lado_a = st.number_input('Ingresa el valor del lado a (cateto)', min_value=0.0, step=1.0)
        lado_c = st.number_input('Ingresa el valor de la hipotenusa', min_value=0.0, step=1.0)
        if st.button("Graficar"):
            if lado_a>0 and lado_c>0 and lado_c>lado_a:
                with col2:
                    calculo_opcion_2(lado_a, lado_c)
            else:
                st.warning("Digita datos apropiados")
    elif opcion == "Cateto b e hipotenusa":
        lado_b = st.number_input('Ingresa el valor del lado b (cateto)', min_value=0.0, step=1.0)
        lado_c = st.number_input('Ingresa el valor de la hipotenusa', min_value=0.0, step=1.0)
        if st.button("Graficar"):
            if lado_b>0 and lado_c>0 and lado_c>lado_b:
                with col2:
                    calculo_opcion_3(lado_b, lado_c)
            else:
                st.warning("Digita datos apropiados")
    elif opcion == "Ángulo α y cateto a":
        angulo_alpha = st.number_input('Ingresa el valor del ángulo α (en grados)', min_value=0.0, max_value=90.0, step=1.0)
        lado_a = st.number_input('Ingresa el valor del lado a (cateto)', min_value=0.0, step=1.0)
        if st.button("Graficar"):
            if lado_a>0 and 0<angulo_alpha<90:
                with col2:
                    calculo_opcion_4(lado_a, angulo_alpha)
            else:
                st.warning("Digita datos apropiados")
    elif opcion == "Ángulo α y cateto b":
        angulo_alpha = st.number_input('Ingresa el valor del ángulo α (en grados)', min_value=0.0, max_value=90.0, step=1.0)
        lado_b = st.number_input('Ingresa el valor del lado b (cateto)', min_value=0.0, step=1.0)
        if st.button("Graficar"):
            if lado_b>0 and 0<angulo_alpha<90:
                with col2:
                    calculo_opcion_5(lado_b, angulo_alpha)
            else:
                st.warning("Digita datos apropiados")
    elif opcion == "Ángulo β y cateto a":
        angulo_beta = st.number_input('Ingresa el valor del ángulo β (en grados)', min_value=0.0, max_value=90.0, step=1.0)
        lado_a = st.number_input('Ingresa el valor del lado a (cateto)', min_value=0.0, step=1.0)
        if st.button("Graficar"):
            if lado_a>0 and 0<angulo_beta<90:
                with col2:
                    calculo_opcion_6(lado_a, angulo_beta)
            else:
                st.warning("Digita datos apropiados")
    elif opcion == "Ángulo β y cateto b":
        angulo_beta = st.number_input('Ingresa el valor del ángulo β (en grados)', min_value=0.0, max_value=90.0, step=1.0)
        lado_b = st.number_input('Ingresa el valor del lado b (cateto)', min_value=0.0, step=1.0)
        if st.button("Graficar"):
            if lado_b>0 and 0<angulo_beta<90:
                with col2:
                    calculo_opcion_7(lado_b, angulo_beta)
            else:
                st.warning("Digita datos apropiados")
    elif opcion == "Ángulo α e hipotenusa":
        angulo_alpha = st.number_input('Ingresa el valor del ángulo α (en grados)', min_value=0.0, max_value=90.0, step=1.0)
        lado_c = st.number_input('Ingresa el valor de la hipotenusa', min_value=0.0, step=1.0)
        if st.button("Graficar"):
            if lado_c>0 and 0<angulo_alpha<90:
                with col2:
                    calculo_opcion_8(lado_c, angulo_alpha)
            else:
                st.warning("Digita datos apropiados")
    elif opcion == "Ángulo β e hipotenusa":
        angulo_beta = st.number_input('Ingresa el valor del ángulo β (en grados)', min_value=0.0, max_value=90.0, step=1.0)
        lado_c = st.number_input('Ingresa el valor de la hipotenusa', min_value=0.0, step=1.0)
        if st.button("Graficar"):
            if lado_c>0 and 0<angulo_beta<90:
                with col2:
                    calculo_opcion_9(lado_c, angulo_beta)
            else:
                st.warning("Digita datos apropiados")


footer_html = """<span style="text-align: center; position:fixed; bottom: 0; left:0; background-color: #CCC; width: 100%;">
    <p><strong>Tri-Go! - Powered by:</strong> Jaider Fabian Contreras Contreras</p>
</span>"""

st.markdown(footer_html, unsafe_allow_html=True)

with col1:
    main()