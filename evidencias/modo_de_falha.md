# Modo de falha provocado: FALHA SILENCIOSA (Aula 4, slide 20)

**Definição:** o sistema devolve uma resposta de aparência normal mesmo quando algo está errado — ninguém percebe.

## 1. Como foi provocada (notebook, seção 16)
Escrevi de propósito uma `prever_sem_validacao()` que não confere nada e a chamei com (a) um registro válido, (b) `Pixels_Areas = -999999` (área impossível) e (c) `Pixels_Areas = NaN`.

## 2. Evidência (colar a saída REAL da célula)
```
[colar a saída da seção 16 do notebook executado]
```
O que a saída mostra: (a) ______ (b) a área absurda produziu a mesma probabilidade de um caso normal, sem erro nem aviso; (c) ______ (depende da versão do scikit-learn: erro ou previsão silenciosa).

## 3. Por que é perigoso no meu problema
Um engenheiro de processo ajustaria (ou deixaria de ajustar) um parâmetro de laminação com base numa probabilidade que não significa nada. Custo: placas produzidas com defeito (FN) ou intervenção sem causa (FP).

## 4. Mitigação aplicada (`demo.py`, função `prever`)
1. Validação explícita: variável faltando, desconhecida, não numérica, NaN/infinito e `TypeOfSteel` inconsistente → `ValueError` com mensagem clara (nunca resposta vazia).
2. Entrada numérica **fora da faixa vista no treino** → `revisao_humana = True` com o motivo e a lista de avisos.
3. Usei `raise ValueError` e não `assert` (o Python pode desligar asserts com `-O`).

## 5. Evidência da mitigação (colar a saída REAL)
```
[colar as linhas "COM validação" da mesma célula e a saída do python demo.py]
```

## 6. Limite da mitigação
A faixa de treino não detecta um valor plausível porém errado (ex.: unidade trocada dentro da faixa). Isso entra na lista de limitações e no critério de desligamento.
