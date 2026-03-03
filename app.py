import streamlit as st
import random
import time

st.set_page_config(page_title="Simulador UG Medicina", layout="centered")

st.title("⚕️ Simulador de Admisión UG - Medicina")
st.markdown("40 preguntas aleatorias | Resultado detallado")

# ========================================
# BANCO COMPLETO DE 80 PREGUNTAS (FORMATO CORRECTO)
# ========================================
banco_preguntas = [

    # ---- BIOLOGÍA (30) ----
    {"tema":"Biología","p":"¿Cuál es la unidad básica, estructural y funcional de los seres vivos?","o":["Tejido","Órgano","Célula","Sistema"],"c":"Célula"},
    {"tema":"Biología","p":"Organelo encargado de la respiración celular y producción de ATP:","o":["Ribosoma","Mitocondria","Lisosoma","Vacuola"],"c":"Mitocondria"},
    {"tema":"Biología","p":"¿En qué fase del ciclo celular se duplica el ADN?","o":["Fase G1","Fase S","Fase G2","Mitosis"],"c":"Fase S"},
    {"tema":"Biología","p":"Tipo de división celular que produce cuatro células hijas haploides:","o":["Mitosis","Bipartición","Meiosis","Gemación"],"c":"Meiosis"},
    {"tema":"Biología","p":"El azúcar presente en el ADN es:","o":["Ribosa","Desoxirribosa","Glucosa","Fructosa"],"c":"Desoxirribosa"},
    {"tema":"Biología","p":"¿Cuál de estas bases nitrogenadas es exclusiva del ARN?","o":["Timina","Uracilo","Adenina","Citosina"],"c":"Uracilo"},
    {"tema":"Biología","p":"La función principal de los glóbulos rojos es:","o":["Defensa","Coagulación","Transporte de oxígeno","Nutrición"],"c":"Transporte de oxígeno"},
    {"tema":"Biología","p":"El conjunto de genes de un individuo se denomina:","o":["Fenotipo","Genotipo","Cariotipo","Alelo"],"c":"Genotipo"},
    {"tema":"Biología","p":"La digestión intracelular es realizada por:","o":["Mitocondrias","Ribosomas","Lisosomas","Cloroplastos"],"c":"Lisosomas"},
    {"tema":"Biología","p":"Células que carecen de núcleo definido son:","o":["Eucariotas","Procariotas","Animales","Vegetales"],"c":"Procariotas"},
    {"tema":"Biología","p":"La hormona que regula los niveles de glucosa en sangre es:","o":["Adrenalina","Insulina","Tiroxina","Estrógeno"],"c":"Insulina"},
    {"tema":"Biología","p":"Principal carbohidrato de reserva en los animales:","o":["Almidón","Celulosa","Glucógeno","Quitina"],"c":"Glucógeno"},
    {"tema":"Biología","p":"¿Cuál es el 'dogma central' de la biología molecular?","o":["ADN -> ARN -> Proteína","ARN -> ADN -> Proteína","Proteína -> ADN","ADN -> Lípidos"],"c":"ADN -> ARN -> Proteína"},
    {"tema":"Biología","p":"Sistema encargado de filtrar la sangre y eliminar desechos:","o":["Digestivo","Excretor/Urinario","Linfático","Endocrino"],"c":"Excretor/Urinario"},
    {"tema":"Biología","p":"Padre de la genética que experimentó con guisantes:","o":["Darwin","Mendel","Pasteur","Lamarck"],"c":"Mendel"},
    {"tema":"Biología","p":"Órgano principal del sistema circulatorio:","o":["Pulmón","Corazón","Hígado","Riñón"],"c":"Corazón"},
    {"tema":"Biología","p":"Las neuronas transmiten impulsos:","o":["Eléctricos","Digestivos","Respiratorios","Óseos"],"c":"Eléctricos"},
    {"tema":"Biología","p":"La fotosíntesis ocurre en:","o":["Mitocondria","Núcleo","Cloroplasto","Ribosoma"],"c":"Cloroplasto"},
    {"tema":"Biología","p":"Tipo de sangre considerado donador universal:","o":["A+","B-","O-","AB+"],"c":"O-"},
    {"tema":"Biología","p":"Sistema encargado de la defensa del organismo:","o":["Digestivo","Nervioso","Inmunológico","Respiratorio"],"c":"Inmunológico"},
    {"tema":"Biología","p":"El ADN se encuentra principalmente en el:","o":["Citoplasma","Núcleo","Ribosoma","Lisosoma"],"c":"Núcleo"},
    {"tema":"Biología","p":"Proceso por el cual las plantas pierden agua:","o":["Transpiración","Digestión","Fijación","Oxidación"],"c":"Transpiración"},
    {"tema":"Biología","p":"Vitaminas liposolubles son:","o":["B y C","A, D, E, K","C y B12","Todas"],"c":"A, D, E, K"},
    {"tema":"Biología","p":"El pH normal de la sangre es aproximadamente:","o":["5","7.4","9","2"],"c":"7.4"},
    {"tema":"Biología","p":"Órgano encargado del intercambio gaseoso:","o":["Hígado","Pulmón","Corazón","Riñón"],"c":"Pulmón"},
    {"tema":"Biología","p":"Tipo de reproducción asexual en bacterias:","o":["Mitosis","Meiosis","Bipartición","Fecundación"],"c":"Bipartición"},
    {"tema":"Biología","p":"El sistema nervioso central está formado por:","o":["Nervios","Cerebro y médula espinal","Ganglios","Músculos"],"c":"Cerebro y médula espinal"},
    {"tema":"Biología","p":"Células encargadas de la defensa:","o":["Eritrocitos","Plaquetas","Leucocitos","Neuronas"],"c":"Leucocitos"},
    {"tema":"Biología","p":"Órgano que produce la bilis es:","o":["Estómago","Hígado","Páncreas","Intestino"],"c":"Hígado"},

    # ---- QUÍMICA (30) ----
    {"tema":"Química","p":"¿Cuál es el símbolo químico del Sodio?","o":["S","So","Na","Sn"],"c":"Na"},
    {"tema":"Química","p":"El enlace donde se transfieren electrones totalmente se llama:","o":["Covalente","Iónico","Metálico","Coordinado"],"c":"Iónico"},
    {"tema":"Química","p":"Sustancia con pH de 2 se considera:","o":["Neutra","Básica","Ácida","Alcalina"],"c":"Ácida"},
    {"tema":"Química","p":"Partícula subatómica con carga negativa:","o":["Protón","Neutrón","Electrón","Positrón"],"c":"Electrón"},
    {"tema":"Química","p":"¿Cuál es el número atómico del Hidrógeno?","o":["1","2","0","1.008"],"c":"1"},
    {"tema":"Química","p":"Fórmula química del Ácido Sulfúrico:","o":["HCl","H2SO4","HNO3","H2O"],"c":"H2SO4"},
    {"tema":"Química","p":"Los elementos del grupo 18 de la tabla periódica son:","o":["Halógenos","Metales alcalinos","Gases nobles","Actínidos"],"c":"Gases nobles"},
    {"tema":"Química","p":"Estado de la materia con volumen y forma definida:","o":["Líquido","Gaseoso","Sólido","Plasma"],"c":"Sólido"},
    {"tema":"Química","p":"La suma de protones y neutrones nos da:","o":["Número atómico","Masa atómica","Valencia","Isótopos"],"c":"Masa atómica"},
    {"tema":"Química","p":"Un cambio físico de la materia es:","o":["Combustión","Oxidación","Evaporación","Putrefacción"],"c":"Evaporación"},
    {"tema":"Química","p":"¿Cuál es el símbolo del Oro?","o":["Or","Ag","Au","Fe"],"c":"Au"},
    {"tema":"Química","p":"Mezcla donde no se distinguen sus componentes a simple vista:","o":["Heterogénea","Homogénea","Coloide","Suspensión"],"c":"Homogénea"},
    {"tema":"Química","p":"La ley de Lavoisier dice que la materia:","o":["Se destruye","Se crea","No se crea ni se destruye, se transforma","Desaparece"],"c":"No se crea ni se destruye, se transforma"},
    {"tema":"Química","p":"Unidad de medida de la cantidad de sustancia en el SI:","o":["Gramo","Mol","Litro","Kelvin"],"c":"Mol"},
    {"tema":"Química","p":"El principal componente del gas natural es:","o":["Butano","Propano","Metano","Etano"],"c":"Metano"},
    {"tema":"Química","p":"El agua tiene fórmula:","o":["H2O","CO2","O2","NaCl"],"c":"H2O"},
    {"tema":"Química","p":"El pH neutro es:","o":["0","7","14","5"],"c":"7"},
    {"tema":"Química","p":"El oxígeno tiene número atómico:","o":["6","7","8","9"],"c":"8"},
    {"tema":"Química","p":"La tabla periódica fue organizada por:","o":["Newton","Mendeléyev","Einstein","Dalton"],"c":"Mendeléyev"},
    {"tema":"Química","p":"Gas necesario para la respiración:","o":["CO2","O2","N2","H2"],"c":"O2"},
    {"tema":"Química","p":"El enlace covalente comparte:","o":["Protones","Neutrones","Electrones","Núcleos"],"c":"Electrones"},
    {"tema":"Química","p":"Unidad de temperatura en el SI:","o":["Celsius","Fahrenheit","Kelvin","Joule"],"c":"Kelvin"},
    {"tema":"Química","p":"El NaCl es:","o":["Ácido","Base","Sal","Gas"],"c":"Sal"},
    {"tema":"Química","p":"Sustancia que dona protones:","o":["Base","Ácido","Sal","Metal"],"c":"Ácido"},
    {"tema":"Química","p":"La combustión requiere:","o":["Agua","Oxígeno","Nitrógeno","Helio"],"c":"Oxígeno"},

    # ---- MATEMÁTICAS (20) ----
    {"tema":"Matemáticas","p":"Si 3x - 5 = 10, ¿cuánto vale x?","o":["3","5","15","2"],"c":"5"},
    {"tema":"Matemáticas","p":"¿Cuál es el 15% de 200?","o":["15","20","30","45"],"c":"30"},
    {"tema":"Matemáticas","p":"Si un tren recorre 300 km en 3 horas, su velocidad media es:","o":["90 km/h","100 km/h","110 km/h","80 km/h"],"c":"100 km/h"},
    {"tema":"Matemáticas","p":"Resultado de (2 + 3) * 5 - 10:","o":["15","25","10","5"],"c":"15"},
    {"tema":"Matemáticas","p":"¿Cuántos minutos hay en 2 horas y cuarto?","o":["120","135","150","125"],"c":"135"},
    {"tema":"Matemáticas","p":"El área de un cuadrado de lado 5 cm es:","o":["10 cm2","20 cm2","25 cm2","15 cm2"],"c":"25 cm2"},
    {"tema":"Matemáticas","p":"Simplificar: 2/4 + 1/2","o":["3/4","1","1/2","1/4"],"c":"1"},
    {"tema":"Matemáticas","p":"¿Qué número sigue en la serie: 2, 6, 18, ...?","o":["24","36","54","42"],"c":"54"},
    {"tema":"Matemáticas","p":"Un ángulo recto mide:","o":["45°","180°","90°","360°"],"c":"90°"},
    {"tema":"Matemáticas","p":"Si x/2 = 8, x es:","o":["4","8","16","2"],"c":"16"},
    {"tema":"Matemáticas","p":"Perímetro de un cuadrado de lado 6:","o":["12","24","36","18"],"c":"24"},
    {"tema":"Matemáticas","p":"25% de 80 es:","o":["10","15","20","25"],"c":"20"},
    {"tema":"Matemáticas","p":"Raíz cuadrada de 81:","o":["7","8","9","6"],"c":"9"},
    {"tema":"Matemáticas","p":"Si 5x = 45, x es:","o":["9","8","10","7"],"c":"9"},
    {"tema":"Matemáticas","p":"Área de un rectángulo 4x5:","o":["20","9","10","25"],"c":"20"},
    {"tema":"Matemáticas","p":"Serie: 5,10,20,40,...","o":["60","70","80","100"],"c":"80"},
    {"tema":"Matemáticas","p":"Convertir 0.5 a fracción:","o":["1/5","1/2","2/5","5/10"],"c":"1/2"},
    {"tema":"Matemáticas","p":"Un triángulo tiene 3 lados y ___ ángulos:","o":["2","4","3","5"],"c":"3"},
    {"tema":"Matemáticas","p":"Si un producto cuesta 100 y tiene 10% de descuento, pagas:","o":["80","85","90","95"],"c":"90"},
]

# =========================
# GENERAR EXAMEN
# =========================
def generar_examen():
    bio = random.sample([p for p in banco_preguntas if p["tema"]=="Biología"], 15)
    qui = random.sample([p for p in banco_preguntas if p["tema"]=="Química"], 15)
    mat = random.sample([p for p in banco_preguntas if p["tema"]=="Matemáticas"], 10)
    preguntas = bio + qui + mat
    random.shuffle(preguntas)
    return preguntas

if "preguntas" not in st.session_state:
    st.session_state.preguntas = generar_examen()
    st.session_state.respuestas = {}
    st.session_state.enviado = False

# =========================
# MOSTRAR EXAMEN
# =========================
if not st.session_state.enviado:

    for i, pregunta in enumerate(st.session_state.preguntas):
        st.subheader(f"Pregunta {i+1} - {pregunta['tema']}")
        st.session_state.respuestas[i] = st.radio(
            pregunta['p'],
            pregunta['o'],
            key=i
        )

    if st.button("Finalizar Examen"):
        st.session_state.enviado = True
        st.rerun()

else:
    puntaje = 0
    errores = []

    for i, pregunta in enumerate(st.session_state.preguntas):
        if st.session_state.respuestas[i] == pregunta["c"]:
            puntaje += 1
        else:
            errores.append({
                "tema": pregunta["tema"],
                "pregunta": pregunta["p"],
                "correcta": pregunta["c"],
                "tu": st.session_state.respuestas[i]
            })

    porcentaje = (puntaje/40)*100

    st.success(f"📊 Resultado final: {puntaje} / 40")
    st.info(f"📈 Porcentaje: {porcentaje:.2f}%")

    if errores:
        st.subheader("❌ Preguntas falladas")
        for e in errores:
            st.write(f"**Tema:** {e['tema']}")
            st.write(f"Pregunta: {e['pregunta']}")
            st.write(f"Tu respuesta: {e['tu']}")
            st.write(f"Correcta: {e['correcta']}")
            st.markdown("---")

    if st.button("Reiniciar Examen"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
