import streamlit as st

st.title("💰 Calculadora de Salário Líquido")
st.write("Digite seu salário bruto abaixo:")

# Entrada de número
salario_bruto = st.number_input("Salário Bruto (R$)", min_value=0.0, step=100.0)

if st.button("Calcular Agora"):
    if salario_bruto > 0:
        imposto = salario_bruto * 0.10  # Simulação de 10%
        salario_liquido = salario_bruto - imposto
        
        st.success(f"Salário Líquido Estimado: R$ {salario_liquido:.2f}")
        st.info(f"Desconto de Impostos (10%): R$ {imposto:.2f}")
    else:
        st.warning("Por favor, digite um valor maior que zero.")