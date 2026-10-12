# Trabalho Final de IA — Steel Plates Faults (papel B: Engenheiro de processo)

**Aluno:** NOME SOBRENOME (editar) | **Disciplina:** Inteligência Artificial — PUC Minas | **Ano:** 2026

## O problema
Decisão apoiada: **ajustar ou não o parâmetro de laminação**.
Alvo binário: `1` = defeito ajustável por parâmetro de laminação (Bumps, Z_Scratch, K_Scatch);
`0` = defeito que o ajuste não resolve (Pastry, Stains, Dirtiness, Other_Faults).

## Como executar (corretor)
```bash
pip install -r requirements.txt
python demo.py          # carrega modelo.joblib do disco e faz previsões (não retreina nada)
```
Abrir `interface.html` com duplo clique (offline). Métricas, matriz de confusão, controle deslizante do ponto de corte,
faixa de revisão humana e tabela dos casos de teste.

## Conteúdo
| Item | Descrição |
|---|---|
| `APRESENTACAO.pptx` | relatório: respostas às 5 perguntas de negócio |
| `NOTEBOOK.ipynb` / `.pdf` | código e saídas executadas (todo número dos slides vem daqui) |
| `modelo.joblib` | árvore de decisão podada + metadados (corte, faixa, faixas de treino) |
| `demo.py` | função `prever(registro: dict) -> dict` e demonstração |
| `interface.html` | interface local com dados embutidos |
| `artefatos/` | SKILL, REGRAS_DO_AGENTE, WORKFLOW, ESCADA_DE_DECISAO |
| `evidencias/` | comparações pareadas, modo de falha, diário de construção |
| `data/` | `steel_plates.csv` + `ACESSO.txt` (fonte e data de acesso) |

## Uso de IA generativa (documentado)
Assistente utilizado: **EDITAR** (nome, plano gratuito, datas das sessões).
As regras que governaram a IA estão em `artefatos/`; as evidências do efeito delas estão em `evidencias/`.

## Premissas e limitações (resumo)
- O alvo é premissa de domínio: a base não documenta a causa física de cada defeito.
- `R` (custo do falso negativo / falso positivo) e a largura da faixa de revisão são premissas do autor (ver notebook, seção 9).
- Other_Faults (classe residual) vai para a classe 0 por regra conservadora; Dirtiness e Stains têm poucas placas no teste.
