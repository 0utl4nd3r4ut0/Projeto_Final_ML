# Workflow de trabalho: observar, decidir, agir, verificar

Versão 1.0 | Dono: Renan Dias | 2026-10-11
Uma tarefa = um objetivo com teste objetivo de "pronto".

## Antes de cada tarefa
- Objetivo: uma frase.
- Critério de pronto: um teste que eu consigo rodar e ver.
- Limite: 3 tentativas.

## O ciclo
1. Observar: ler o estado atual (arquivos, saída, erro). Não agir antes de observar.
2. Decidir: propor um plano de até 5 linhas e classificar cada ação (ler, reversível,
   irreversível, conforme REGRAS_DO_AGENTE.md). Esperar minha aprovação se houver escrita.
3. Agir: executar só o plano aprovado, um passo por vez.
4. Verificar: rodar o teste do critério de pronto e mostrar a saída completa.
   Comparar com o esperado. Não declarar sucesso sem isso.

## Critério de parada
- Sucesso: critério de pronto atendido com saída visível. Parar, resumir, eu faço o commit.
- Limite: 3 tentativas sem sucesso. Parar e entregar relatório (o que tentou, erro completo,
  hipótese) para mim.
- Escalonamento: precisar de ação irreversível, mudar alvo/divisão/base ou usar biblioteca
  fora da lista. Parar e pedir.
- Contexto: se a conversa ficar longa ou confusa, resumir o estado em 10 linhas; eu abro
  sessão nova e recolo os artefatos.

## Registro
Cada tarefa vira um ciclo em evidencias/diario.md: objetivo, prompt, resposta, teste,
erro, correção, decisão (aceitar, refazer ou descartar).