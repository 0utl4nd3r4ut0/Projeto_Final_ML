# Regras do agente: TF IA (papel B, Engenheiro de processo)

Versão 1.0 | Dono: Renan Dias | 2026-10-11
Vale para qualquer assistente de IA usado neste projeto. Colar no início de cada sessão.

## Contexto fixo (não negociável)
- Base: data/steel_plates.csv (1941 linhas x 34 colunas).
- Alvo `alvo`: 1 se o defeito é Bumps, Z_Scratch ou K_Scatch; 0 nos demais.
- Divisão: train_test_split(X, y, test_size=0.20, random_state=42), exatamente assim.
- Bibliotecas permitidas: pandas, scikit-learn, joblib (numpy vem como dependência).
- Caminhos sempre relativos. Nunca caminho absoluto.

## Classificação das ações
| Categoria | Exemplos neste projeto | Controle aplicado |
|---|---|---|
| Ler | ler o CSV, o notebook, os artefatos, mensagens de erro | Autônomo, só dentro da pasta do projeto. Relatar o que leu. |
| Alterar de forma reversível | criar ou editar .py, .ipynb, .md, .html sob git | Só após eu aprovar o plano. Commit antes; eu reviso o diff antes de aceitar. |
| Alterar de forma irreversível | apagar arquivos; sobrescrever o CSV ou o modelo.joblib aprovado; git reset --hard ou push --force; instalar pacote fora da lista | Aprovação explícita minha, a cada vez. Sem exceção. |

## A IA pode fazer sozinha
- Ler arquivos do projeto e explicar o que encontrou.
- Propor planos, código e análises (sem gravar nada).

## Exige conferência minha
- Todo código novo ou alterado: eu leio e consigo explicar antes de aceitar.
- Toda métrica ou número apresentado: precisa vir de uma saída de execução visível.

## Proibido (sempre)
- Alterar a divisão treino/teste, a base ou a definição do alvo.
- Usar o conjunto de teste para escolher modelo, hiperparâmetro ou ponto de corte.
- Colocar as 7 colunas de defeito nas variáveis de entrada (vazamento de dados).
- Inventar saída, métrica ou resultado de execução.
- Esconder ou resumir um erro: reportar a mensagem completa.
- Afirmar que algo funciona sem mostrar a execução. Se não executou, dizer "não executado".

## Quando parar e perguntar
- Qualquer ação irreversível.
- Ambiguidade sobre alvo, divisão ou regra deste arquivo.
- Falta de dado: listar o que falta em vez de estimar.