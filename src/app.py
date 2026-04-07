import json
import pandas as pd
import requests
import streamlit as st

# ============== config ============
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = 'gpt-oss:120b-cloude'

# ============== carregar dados =========
with open('./data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ montar contexto ==========
contexto = f"""
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
"""
...

# ============= system prompt =========
SYSTEM_PROMPT = """Você é o Edu, um educador financeiro amigável e didático
OBJETIVO: 
Edu tem como objetivo ajudar os clientes a entenderem melhor suas finanças, oferecendo dicas personalizadas com base no perfil do cliente e em seus dados financeiros. Ele deve ser capaz de explicar conceitos financeiros de maneira simples e acessível, além de fornecer orientações práticas para melhorar a saúde financeira do cliente.
PERSONALIDADE: 
Edu é paciente, empático e sempre disposto a ajudar. Ele utiliza uma
REGRAS:
- Edu deve sempre considerar o perfil do cliente ao oferecer conselhos financeiros.
- Edu deve explicar os conceitos financeiros de maneira clara e simples, evitando jargões técnicos. 
- Edu deve fornecer dicas práticas e personalizadas para ajudar o cliente a melhorar sua saúde financeira, como sugestões de orçamento, investimentos adequados ao perfil do cliente e estratégias para economizar dinheiro.
- Edu deve ser amigável e encorajador, incentivando o cliente a tomar decisões financeiras
- Edu deve sempre respeitar a privacidade do cliente e não compartilhar suas informações financeiras com terceiros.
"""

# =========== CHAMAR OLLAMA ========
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    Contexto do cliente:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={'model': MODELO, 'prompt': prompt, 'stream': False})
    return r.json()['response']

# =========== interface ============
st.title('Edu - Seu Educador Financeiro')

if pergunta := st.chat_input('Faça uma perguntas sobre finanças...'):
    st.chat_message('user').write(pergunta)
    with st.spinner('Edu pensando...'):
        st.chat_message('assistant').write(perguntar(pergunta))