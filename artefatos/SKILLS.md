---
name: avaliar-modelo-e-analise-de-erro
description: >
  Avalia o classificador de defeitos (alvo: ajustável por parâmetro de laminação) e
  redige a análise de erro por defeito original. Usar quando houver predições do
  conjunto de teste e um ponto de corte definido, ou quando o corte mudar.
---

# Avaliar o modelo e redigir a análise de erro

Versão 1.0 | Dono: Renan Dias | 2026-10-11

## Objetivo
Produzir sempre a mesma análise, com números vindos da execução, incluindo o
desempenho separado para cada um dos 7 defeitos originais.

## Quando usar
- Modelo treinado, probabilidades no teste e ponto de corte definidos.
- O ponto de corte ou o modelo mudou e a análise precisa ser refeita.

## Quando não usar
- Para escolher o ponto de corte (é cálculo de custo, não análise de texto).
- Para treinar ou ajustar o modelo.
- Sem saída de execução disponível.

## Entradas necessárias
1. y_test e as probabilidades previstas no teste, na mesma ordem.
2. Ponto de corte e razão de custos R usados.
3. Métricas de treino e de teste.
4. Tabela com o defeito original (um dos 7) de cada caso de teste.
Se faltar qualquer entrada, listar o que falta e parar. Não estimar.

## Procedimento
1. Conferir as entradas (tamanhos iguais, alvo binário, os 7 defeitos presentes).
2. Matriz de confusão no corte: verdadeiros e falsos positivos e negativos.
3. Acurácia, precisão e recall no treino e no teste.
4. Diagnóstico de sobreajuste: comparar treino e teste e dizer se a diferença é
   relevante (padrão: 5 pontos percentuais, premissa do dono).
5. Por defeito original: nº de casos, quantos previstos como 1, % previsto como 1 e se
   isso contraria a classe esperada. Destacar Other_Faults.
6. Redigir a análise no formato abaixo.

## Formato da resposta
1. Resumo (3 linhas)
2. Métricas treino x teste (tabela)
3. Matriz de confusão
4. Desempenho por defeito original (tabela, Other_Faults em destaque)
5. Diagnóstico de sobreajuste
6. Riscos e limitações
7. O que não foi verificado

## Regras
- Todo número vem da saída de execução fornecida. Nunca inventar.
- Separar fato (saída) de hipótese (interpretação), rotulando cada um.
- Falso negativo = ajustável classificado como não ajustável. Falso positivo = o oposto.
- O ponto de corte não é escolhido nem alterado aqui.
- Se faltar dado, listar o que falta em vez de estimar.

## Limitações
- O alvo é premissa de domínio, não causa física comprovada.
- Alguns defeitos têm poucos casos no teste (Dirtiness, Stains): leituras por defeito
  são frágeis.