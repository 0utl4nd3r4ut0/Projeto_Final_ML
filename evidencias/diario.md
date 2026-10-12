# Diário de construção (5 ciclos)

> Regras do enunciado: cada ciclo = **especificar → gerar → executar → testar → criticar → corrigir**.
> Cole o que realmente aconteceu. Ciclos em que tudo funcionou de primeira não atendem ao propósito.
> **Pelo menos um ciclo deve terminar em DESCARTE**, com justificativa técnica.
> Assistente usado: ______ (plano gratuito) | Artefatos colados na sessão: REGRAS_DO_AGENTE.md, WORKFLOW.md (+ SKILL.md quando aplicável)

## Modelo de ciclo (copiar para cada um)

### Ciclo N — título curto
- **Objetivo:**
- **Critério de pronto (teste objetivo):**
- **Prompt usado (literal):**
  ```
  [colar]
  ```
- **O que a IA devolveu (resumo + trecho relevante):**
- **Teste executado e saída (literal):**
  ```
  [colar a saída]
  ```
- **Mensagem de erro colada do terminal (se houve):**
  ```
  [colar]
  ```
- **Crítica (o que estava errado ou arriscado, e por que):**
- **Correção aplicada (prompt de correção ou edição minha):**
- **Decisão:** ACEITAR | REFAZER | DESCARTAR — justificativa técnica:

---

## Ciclos sugeridos (escolha os seus; use os que realmente aconteceram)
1. Divisão treino/teste e exploração (checar: random_state mantido? 7 colunas fora do X? meta alinhado pelo índice?)
2. Árvore e poda por validação cruzada (checar: a busca usou só o treino? ou olhou o teste?)
3. Ponto de corte pelo custo do erro (checar: escolheu pelo teste? usou 0,5 por padrão?)
4. `prever()` e `demo.py` (checar: valida entrada? caminho absoluto? retreina?)
5. `interface.html` (checar: usa fetch? dados embutidos? faixa de revisão?)

## Ciclo 1
## Ciclo 2
## Ciclo 3
## Ciclo 4
## Ciclo 5
