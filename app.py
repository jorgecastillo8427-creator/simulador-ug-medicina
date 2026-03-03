import streamlit as st
import random
import time

st.set_page_config(page_title="Simulador UG Medicina", layout="centered")

st.title("⚕️ Simulador de Admisión UG - Medicina")
st.markdown("120 preguntas en base de datos | 40 seleccionadas por examen")

# ========================================
# BANCO TOTAL DE PREGUNTAS (120)
# ========================================
banco_preguntas = [
    # ---- BIOLOGÍA Y ANATOMÍA ----
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
    {"tema":"Biología","p":"¿Cuál es el órgano más grande del cuerpo humano?","o":["Hígado","Piel","Pulmón","Intestino"],"c":"Piel"},
    {"tema":"Biología","p":"La unidad funcional del riñón es:","o":["Glomérulo","Nefrona","Alvéolo","Neurona"],"c":"Nefrona"},
    {"tema":"Biología","p":"¿Qué tipo de tejido conecta músculos con huesos?","o":["Cartílago","Tendón","Ligamento","Epitelio"],"c":"Tendón"},
    {"tema":"Biología","p":"La hormona producida por la glándula tiroides es:","o":["Insulina","Tiroxina","Adrenalina","Progesterona"],"c":"Tiroxina"},
    {"tema":"Biología","p":"¿Cuál es la función principal de los alvéolos pulmonares?","o":["Filtración","Intercambio gaseoso","Producción de moco","Digestión"],"c":"Intercambio gaseoso"},
    {"tema":"Biología","p":"El sistema que coordina las funciones del cuerpo mediante hormonas es:","o":["Nervioso","Endocrino","Digestivo","Excretor"],"c":"Endocrino"},
    {"tema":"Biología","p":"La médula ósea roja produce principalmente:","o":["Plaquetas","Glóbulos rojos","Hormonas","Enzimas"],"c":"Glóbulos rojos"},
    {"tema":"Biología","p":"El órgano que regula la temperatura corporal es:","o":["Corazón","Hipotálamo","Hígado","Páncreas"],"c":"Hipotálamo"},
    {"tema":"Biología","p":"La vitamina necesaria para la coagulación sanguínea es:","o":["Vitamina A","Vitamina C","Vitamina K","Vitamina D"],"c":"Vitamina K"},
    {"tema":"Biología","p":"La capa externa del corazón se llama:","o":["Endocardio","Miocardio","Pericardio","Epicardio"],"c":"Pericardio"},

    # ---- QUÍMICA Y BIOQUÍMICA ----
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
    {"tema":"Química","p":"El grupo funcional característico de los alcoholes es:","o":["-NH2","-OH","-COOH","-CHO"],"c":"-OH"},
    {"tema":"Química","p":"La molécula de hemoglobina contiene:","o":["Hierro","Cobre","Zinc","Magnesio"],"c":"Hierro"},
    {"tema":"Química","p":"La enzima que cataliza la descomposición del peróxido de hidrógeno es:","o":["Amilasa","Lipasa","Catalasa","Pepsina"],"c":"Catalasa"},
    {"tema":"Química","p":"El colesterol pertenece al grupo de:","o":["Proteínas","Carbohidratos","Lípidos","Vitaminas"],"c":"Lípidos"},
    {"tema":"Química","p":"La molécula de ADN está formada por:","o":["Monosacáridos","Nucleótidos","Aminoácidos","Ácidos grasos"],"c":"Nucleótidos"},
    {"tema":"Química","p":"La glucosa es un tipo de:","o":["Monosacárido","Disacárido","Polisacárido","Proteína"],"c":"Monosacárido"},
    {"tema":"Química","p":"El ATP se considera:","o":["Fuente de energía","Proteína estructural","Hormona","Vitamina"],"c":"Fuente de energía"},
    {"tema":"Química","p":"La reacción química que libera energía se llama:","o":["Endotérmica","Exotérmica","Reversible","Neutra"],"c":"Exotérmica"},
    {"tema":"Química","p":"La fórmula química de la glucosa es:","o":["C6H12O6","C12H22O11","CH3COOH","C2H5OH"],"c":"C6H12O6"},

    # ---- FISIOLOGÍA Y MEDICINA ----
    {"tema":"Medicina","p":"La presión arterial normal en adultos es aproximadamente:","o":["120/80 mmHg","140/90 mmHg","100/60 mmHg","160/100 mmHg"],"c":"120/80 mmHg"},
    {"tema":"Medicina","p":"La hormona que estimula la producción de leche materna es:","o":["Progesterona","Prolactina","Estrógeno","Testosterona"],"c":"Prolactina"},
    {"tema":"Medicina","p":"El órgano encargado de metabolizar fármacos es:","o":["Riñón","Hígado","Pulmón","Estómago"],"c":"Hígado"},
    {"tema":"Medicina","p":"El marcapasos natural del corazón es:","o":["Nodo AV","Nodo SA","Haz de His","Ventrículo"],"c":"Nodo SA"},
    {"tema":"Medicina","p":"La hormona antidiurética (ADH) actúa principalmente en:","o":["Pulmones","Riñones","Hígado","Estómago"],"c":"Riñones"},
    {"tema":"Medicina","p":"La anemia se relaciona con la disminución de:","o":["Glóbulos blancos","Plaquetas","Glóbulos rojos","Plasma"],"c":"Glóbulos rojos"},
    {"tema":"Medicina","p":"La insulina se produce en:","o":["Hígado","Páncreas","Riñón","Estómago"],"c":"Páncreas"},
    {"tema":"Medicina","p":"La hormona que regula el ciclo menstrual es:","o":["Testosterona","Progesterona","Insulina","Tiroxina"],"c":"Progesterona"},
    {"tema":"Medicina","p":"El líquido cefalorraquídeo se encuentra en:","o":["Corazón","Médula espinal y cerebro","Pulmones","Riñones"],"c":"Médula espinal y cerebro"},
    {"tema":"Medicina","p":"La enfermedad causada por deficiencia de vitamina D es:","o":["Raquitismo","Anemia","Beriberi","Escorbuto"],"c":"Raquitismo"},

    # ---- MATEMÁTICAS APLICADAS ----
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
    {"tema":"Matemáticas","p":"Si un medicamento se administra cada 8 horas, ¿cuántas dosis se aplican en 2 días?","o":["4","6","8","12"],"c":"6"},
    {"tema":"Matemáticas","p":"Un paciente pesa 70 kg. Si la dosis es 5 mg/kg, ¿cuál es la dosis total?","o":["250 mg","350 mg","400 mg","500 mg"],"c":"350 mg"},
    {"tema":"Matemáticas","p":"Si la frecuencia cardíaca es de 75 latidos por minuto, ¿cuántos latidos en una hora?","o":["3000","4500","5000","6000"],"c":"4500"},
    {"tema":"Matemáticas","p":"Un suero de 500 ml se administra en 5 horas. ¿Cuál es la velocidad de infusión en ml/h?","o":["50","100","125","200"],"c":"100"},
    {"tema":"Matemáticas","p":"Si un antibiótico se da cada 12 horas, ¿cuántas dosis en una semana?","o":["7","10","12","14"],"c":"14"},
    {"tema":"Matemáticas","p":"Un paciente consume 2 litros de agua al día. ¿Cuántos litros en una semana?","o":["10","12","14","20"],"c":"14"},
    {"tema":"Matemáticas","p":"Si la glucosa en sangre es 90 mg/dl, ¿cuántos mg en 1 litro (10 dl)?","o":["900","1000","1100","1200"],"c":"900"},
    {"tema":"Matemáticas","p":"Un frasco tiene 250 ml de solución. Si se administran 50 ml por día, ¿cuántos días dura?","o":["3","4","5","6"],"c":"5"},
    {"tema":"Matemáticas","p":"Si el área de un círculo es πr², ¿cuál es el área con r=7?","o":["49π","14π","21π","7π"],"c":"49π"},
    {"tema":"Matemáticas","p":"Si un medicamento cuesta 2.5 dólares por tableta y se compran 40, ¿cuánto cuesta?","o":["80","90","100","120"],"c":"100"},
]

# =========================
# GENERAR EXAMEN (Balanceado)
# =========================
def generar_examen():
    # Tomamos 15 de Biología/Medicina combinadas, 15 de Química y 10 de Matemáticas
    bio_med = random.sample([p for p in banco_preguntas if p["tema"] in ["Biología", "Medicina"]], 15)
    qui = random.sample([p for p in banco_preguntas if p["tema"]=="Química"], 15)
    mat = random.sample([p for p in banco_preguntas if p["tema"]=="Matemáticas"], 10)
    
    preguntas = bio_med + qui + mat
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
    st.info("Responde las 40 preguntas y haz clic en 'Finalizar' al final de la página.")
    
    for i, pregunta in enumerate(st.session_state.preguntas):
        st.markdown(f"**Pregunta {i+1}** ({pregunta['tema']})")
        st.session_state.respuestas[i] = st.radio(
            pregunta['p'],
            pregunta['o'],
            key=f"q_{i}",
            index=None # Para que no aparezca ninguna marcada al inicio
        )
        st.write("---")

    if st.button("🚀 Finalizar Examen y Ver Puntaje", use_container_width=True):
        # Verificar que todas estén respondidas
        if None in st.session_state.respuestas.values():
            st.warning("⚠️ Por favor, responde todas las preguntas antes de finalizar.")
        else:
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

    # Mostrar Resultado con globos
    st.balloons()
    st.header(f"📊 Resultado: {puntaje} / 40")
    porcentaje = (puntaje/40)*100
    st.progress(porcentaje/100)
    
    if puntaje >= 30:
        st.success("¡Excelente nivel! Estás muy cerca de entrar a Medicina.")
    else:
        st.warning("Buen intento, pero debes reforzar los temas fallados.")

    if errores:
        with st.expander("Ver corrección de errores"):
            for e in errores:
                st.write(f"**[{e['tema']}]** {e['pregunta']}")
                st.error(f"Tu respuesta: {e['tu']}")
                st.success(f"Correcta: {e['correcta']}")
                st.write("---")

    if st.button("🔄 Intentar de Nuevo (Nuevas Preguntas)", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
