# 🤖 Edu — Agente Financeiro Inteligente com IA Generativa

## 📌 Visão Geral

O **Edu** é um agente financeiro inteligente desenvolvido com IA Generativa e executado localmente via Ollama + LLM (Llama 3).

O objetivo do projeto é evoluir o conceito de chatbot tradicional para um agente consultivo, personalizado e proativo, capaz de:

- 📊 Analisar dados financeiros do cliente
- 🧠 Adaptar respostas ao perfil de investidor
- 💡 Sugerir melhorias práticas para a saúde financeira
- 🔐 Reduzir riscos de alucinação utilizando dados estruturados

Este projeto simula um cenário real de aplicação de IA no setor financeiro, utilizando dados mockados e arquitetura modular.

---

# 🎯 Problema Resolvido

Muitos assistentes financeiros:

- Apenas respondem perguntas genéricas
- Não consideram o perfil individual do cliente
- Não utilizam contexto histórico
- Podem gerar respostas imprecisas

O Edu resolve isso ao:

✔ Utilizar dados estruturados  
✔ Considerar perfil de investidor  
✔ Manter um tom didático e acessível  
✔ Garantir coerência e segurança nas respostas  

---

# 🧠 Como o Agente Funciona

## 1️⃣ Entrada de Dados

O agente consome dados estruturados da pasta `data/`:

| Arquivo | Descrição |
|----------|------------|
| `transacoes.csv` | Histórico de movimentações financeiras |
| `historico_atendimento.csv` | Histórico de interações anteriores |
| `perfil_investidor.json` | Perfil e preferências do cliente |
| `produtos_financeiros.json` | Catálogo de produtos disponíveis |

---

## 2️⃣ Construção de Contexto

O sistema:

- Carrega os dados
- Constrói um contexto textual estruturado
- Injeta esse contexto no System Prompt
- Envia para o modelo LLM via API do Ollama

---

## 3️⃣ Geração de Resposta

Fluxo simplificado:

Usuário → Streamlit → Prompt estruturado → Ollama API → LLM → Resposta personalizada

---

# 🏗️ Arquitetura

📦 Aplicação Streamlit  
│  
├── 📂 Base de Dados (CSV / JSON)  
├── 🧠 Construção de Prompt  
├── 🔌 API Ollama (localhost:11434)  
└── 🤖 Modelo LLM (llama3)  

---

# 🔐 Segurança e Anti-Alucinação

O projeto adota estratégias para aumentar confiabilidade:

- Uso de dados mockados controlados
- Prompt restritivo com regras claras
- Contexto financeiro explícito
- Evita respostas fora do escopo
- Modelo executando localmente (sem envio de dados externos)

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python | Backend |
| Streamlit | Interface interativa |
| Ollama | Execução local do LLM |
| Llama 3 | Modelo de linguagem |
| Pandas | Manipulação de dados |
| Requests | Comunicação com API |

---

# 🚀 Como Executar o Projeto

## 1️⃣ Instalar o Ollama

Baixe e instale:
https://ollama.com

---

## 2️⃣ Baixar o Modelo

```bash
ollama pull llama3
