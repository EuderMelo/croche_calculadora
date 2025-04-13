import streamlit as st
import math

# Função de cálculo do peso do fio para peças redondas
def estimar_peso_fio_redondo(diametro_cm, diametro_referencia=36, peso_referencia_g=150):
    raio = diametro_cm / 2
    raio_ref = diametro_referencia / 2

    area = math.pi * raio ** 2
    area_ref = math.pi * raio_ref ** 2

    peso_estimado = (area / area_ref) * peso_referencia_g
    return round(peso_estimado, 2)

# Função de cálculo do peso do fio para peças retangulares
def estimar_peso_fio_retangular(comprimento_cm, largura_cm, area_referencia=36*36, peso_referencia_g=150):
    area = comprimento_cm * largura_cm
    peso_estimado = (area / area_referencia) * peso_referencia_g
    return round(peso_estimado, 2)

# Função para calcular o custo final
def calcular_valor_final(peso_estimado, valor_rolo, peso_rolo, mao_de_obra_hora, tempo_gasto, quantidade, dificuldade):
    # Custo dos materiais com fator de segurança
    custo_material = (peso_estimado / peso_rolo) * valor_rolo * 1.15

    # Custo da mão de obra
    custo_mao_de_obra = mao_de_obra_hora * tempo_gasto

    # Multiplicador de dificuldade
    multiplicador_dificuldade = {"Baixo": 1.0, "Médio": 1.2, "Alto": 1.4}[dificuldade]

    # Cálculo do valor final
    valor_final = (custo_material + custo_mao_de_obra) * multiplicador_dificuldade * quantidade
    return round(valor_final, 2)

# Interface Streamlit
st.set_page_config(page_title="Calculadora Valor Final para Peças Artesanais", page_icon="🧶")

st.title("🧶 Calculadora Valor Final para Peças Artesanais")

st.markdown("""
Informe os dados abaixo para estimar o peso do fio necessário e o valor final da peça com base nos custos de materiais, mão de obra e dificuldade.
""")

# Seleção do tipo de peça
tipo_peca = st.selectbox("Selecione o tipo de peça", ["Sousplat (Redondo)", "Retangular"])

# Entrada de dados para o tipo de peça
if tipo_peca == "Sousplat (Redondo)":
    diametro = st.number_input("Diâmetro do sousplat (em cm)", min_value=10.0, max_value=100.0, step=0.5)
    peso_estimado = estimar_peso_fio_redondo(diametro)
else:
    comprimento = st.number_input("Comprimento da peça (em cm)", min_value=10.0, max_value=200.0, step=0.5)
    largura = st.number_input("Largura da peça (em cm)", min_value=10.0, max_value=200.0, step=0.5)
    peso_estimado = estimar_peso_fio_retangular(comprimento, largura)

# Entrada de dados gerais
valor_rolo = st.number_input("Valor do rolo de fio (em R$)", min_value=0.0, step=0.1)
peso_rolo = st.number_input("Peso do rolo de fio (em g)", min_value=1.0, step=1.0)
mao_de_obra_hora = st.number_input("Valor da mão de obra por hora (em R$)", min_value=0.0, step=0.1)
tempo_gasto = st.number_input("Tempo gasto para fazer uma peça (em horas)", min_value=0.0, step=0.1)
quantidade = st.number_input("Quantidade de peças", min_value=1, step=1)
dificuldade = st.selectbox("Nível de dificuldade", ["Baixo", "Médio", "Alto"])

# Botão para calcular
if st.button("Calcular"):
    valor_final = calcular_valor_final(peso_estimado, valor_rolo, peso_rolo, mao_de_obra_hora, tempo_gasto, quantidade, dificuldade)
    
    # Cálculo da quantidade de rolos de fio necessários
    rolos_necessarios = math.ceil((peso_estimado * quantidade) / peso_rolo)
    rolos_necessarios = round((peso_estimado * quantidade) / peso_rolo, 1)

    if tipo_peca == "Sousplat (Redondo)":
        st.success(f"""
        📏 **Diâmetro:** {diametro} cm  
        🧵 **Peso estimado do fio:** {peso_estimado} g  
        📦 **Rolos de fio necessários:** {rolos_necessarios}  
        💰 **Valor final estimado:** R$ {valor_final}
        """)
    else:
        st.success(f"""
        📏 **Comprimento:** {comprimento} cm  
        📐 **Largura:** {largura} cm  
        🧵 **Peso estimado do fio:** {peso_estimado} g  
        📦 **Rolos de fio necessários:** {rolos_necessarios}  
        💰 **Valor final estimado:** R$ {valor_final}
        """)

# Rodapé
st.markdown("---")
st.caption("Criado para cálculo de construção de peças de crochê. 💙")