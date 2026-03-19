import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Quiz: Our Brand is Crisis", page_icon="🗳️")

# 2. Base de datos de preguntas (Muestra de las generadas)
preguntas = [
    {
        "id": 1,
        "pregunta": "¿Cuál era la principal preocupación de los votantes bolivianos según las encuestas iniciales mencionadas en el video?",
        "opciones": ["La falta de infraestructura", "El desempleo", "La corrupción", "El cambio climático"],
        "correcta": "El desempleo"
    },
    {
        "id": 2,
        "pregunta": "¿Cómo se llama la firma de consultoría estadounidense contratada por Gonzalo Sánchez de Lozada?",
        "opciones": ["Saatchi & Saatchi", "Greenberg Carville Shrum", "McKensey & Co", "Cambridge Analytica"],
        "correcta": "Greenberg Carville Shrum"
    },
    {
        "id": 3,
        "pregunta": "¿Cuál fue el concepto central o 'marca' que los consultores decidieron asignar a la campaña de Goni?",
        "opciones": ["Revolución", "Esperanza", "Juventud", "Crisis"],
        "correcta": "Crisis"
    },
    {
        "id": 4,
        "pregunta": "¿Qué analogía utilizó James Carville para referirse al mensaje político serio que debían dar?",
        "opciones": ["Carne asada", "Espinaca", "Medicina amarga", "Pan y agua"],
        "correcta": "Espinaca"
    },
    {
        "id": 5,
        "pregunta": "¿Quién era el principal rival de Goni que lideraba las encuestas al inicio del documental?",
        "opciones": ["Hugo Banzer", "Evo Morales", "Manfred Reyes", "Carlos Mesa"],
        "correcta": "Manfred Reyes"
    },
    {
        "id": 6,
        "pregunta": "¿Qué herramienta utilizaban los consultores para medir la reacción de la gente ante los anuncios televisivos?",
        "opciones": ["Encuestas telefónicas", "Votaciones en línea", "Análisis de Big Data", "Grupos de enfoque"],
        "correcta": "Grupos de enfoque"
    },
    {
        "id": 7,
        "pregunta": "¿Qué rasgo de la personalidad de Goni era visto como una debilidad constante en los grupos de enfoque?",
        "opciones": ["Timidez", "Falta de inteligencia", "Arrogancia", "Pereza"],
        "correcta": "Arrogancia"
    },
    {
        "id": 8,
        "pregunta": "¿Cuál fue el objetivo de la 'Guerra Sucia' lanzada contra Manfred Reyes Villa?",
        "opciones": ["Convertirlo de un candidato 'limpio' en uno 'sucio' ", "Promocionar sus propuestas económicas", "Obligarlo a retirarse de la política", "Lograr que se una a la campaña de Goni"],
        "correcta": "Convertirlo de un candidato 'limpio' en uno 'sucio' "
    },
    {
        "id": 9,
        "pregunta": "¿Qué evento externo impulsó inesperadamente la candidatura de Evo Morales?",
        "opciones": ["Las declaraciones del embajador de EEUU", "La renuncia de Manfred", "Una donación masiva de dinero extranjero", "Un debate televisivo exitoso"],
        "correcta": "Las declaraciones del embajador de EEUU"
    },
    {
        "id": 10,
        "pregunta": "¿Con qué porcentaje aproximado ganó Goni la elección presidencial de 2002?",
        "opciones": ["51%", "10%", "22%", "35%"],
        "correcta": "22%"
    },
    # Puedes seguir agregando las 20 preguntas aquí siguiendo el mismo formato
]

# 3. Inicialización del Estado de la Sesión (Memoria del App)
if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.finalizado = False

# 4. Función para reiniciar el cuestionario
def reiniciar_quiz():
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.finalizado = False

# 5. Interfaz de Usuario
st.title("📊 Cuestionario: Our Brand is Crisis")
st.write("Analiza las estrategias de comunicación política del documental.")

if not st.session_state.finalizado:
    # Mostrar pregunta actual
    item = preguntas[st.session_state.indice]
    st.subheader(f"Pregunta {st.session_state.indice + 1} de {len(preguntas)}")
    st.info(item["pregunta"])
    
    # Formulario de respuesta
    with st.form(key=f"form_{st.session_state.indice}"):
        respuesta = st.radio("Selecciona una opción:", item["opciones"])
        enviar = st.form_submit_button("Siguiente ➡️")
        
        if enviar:
            if respuesta == item["correcta"]:
                st.session_state.puntaje += 1
            
            # Avanzar o finalizar
            if st.session_state.indice < len(preguntas) - 1:
                st.session_state.indice += 1
                st.rerun()
            else:
                st.session_state.finalizado = True
                st.rerun()
else:
    # Pantalla final de resultados
    st.success("¡Has completado el cuestionario!")
    st.metric("Tu Puntaje Final", f"{st.session_state.puntaje} / {len(preguntas)}")
    
    # Cálculo de porcentaje para feedback
    porcentaje = (st.session_state.puntaje / len(preguntas)) * 100
    if porcentaje >= 70:
        st.balloons()
        st.write("✅ ¡Excelente dominio del contenido!")
    else:
        st.write("⚠️ Te recomendamos revisar los puntos clave del documental.")

    # BOTÓN DE REINICIO
    if st.button("🔄 Reiniciar Cuestionario"):
        reiniciar_quiz()
        st.rerun()

# Barra de progreso visual
progress_percent = (st.session_state.indice) / len(preguntas)
st.progress(progress_percent)