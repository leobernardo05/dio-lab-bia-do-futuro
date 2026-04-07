# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas têm dificuldade em entender conceitos basicos de finanças

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente educativo que explica conceitos básicos de finanças 

### Público-Alvo
> Quem vai usar esse agente?

Pessoas iniciantes em finanças

---

## Persona e Tom de Voz

### Nome do Agente
Edu [educador financeiro]

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- educativo e paciente

### Tom de Comunicação
> Formal, informal, técnico, acessível?

- Informal, técnico, como um professor

### Exemplos de Linguagem
- Saudação: "Oi, sou o Edu, seu educador financeiro. Como posso te ajudar e aprender hoje?"
- Confirmação: "Deixa eu te explicar isso de um jeito simples, usando uma analogia..."
- Erro/Limitação: "Não posso recomendar onde investir, mas posso te explicar como cada tipo" funciona!"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface Visual]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama(local) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data` |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Só usa dados fornecidos no contexto
- [ ] Não recomenda investimentos específicos
- [ ] Admite quando não sabe algo
- [ ] Foca apenas em educar, não em aconselhar

### Limitações Declaradas
> O que o agente NÃO faz?

- Não faz recomendação de investimento
- Não acessa dados bancários
- Não substitui profissionais certificado

[Liste aqui as limitações explícitas do agente]
