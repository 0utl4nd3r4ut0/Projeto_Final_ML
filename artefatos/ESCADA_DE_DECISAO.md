# Escada de decisão: TF IA

Versão 1.0 | Dono: Renan Dias | 2026-10-11
Regra: só subir um degrau quando eu consigo justificar por que o anterior não resolve.
Degraus: (1) prompt direto, (2) documento colado no contexto, (3) Skill.
Saída lateral: automação tradicional sem IA.
Fora de escopo, e por quê: RAG (não há base de conhecimento que muda), MCP (não há
sistema externo), fine-tuning (sem volume que pague), agente autônomo (menor
autonomia que resolve).

| Necessidade | Camada | Por que a anterior não resolvia |
|---|---|---|
| Montar steel_plates.csv a partir dos arquivos brutos | Automação tradicional (montar_csv.py) | Tarefa determinística e única; o assert verifica. IA não agrega e pode errar em silêncio. |
| Escrever EDA e treino (pandas, scikit-learn) | Documento colado (REGRAS_DO_AGENTE + contexto do alvo) | Prompt direto não conhece a divisão fixa, o alvo nem a proibição de vazamento; a IA poderia mudar o split ou usar as 7 colunas em X. |
| Revisar código gerado antes de aceitar | Prompt direto + checklist do WORKFLOW | A revisão é minha e o checklist é curto; Skill seria exagero para pouco volume. |
| Avaliar o modelo e redigir a análise de erro | Skill | Documento colado não garante estrutura nem verificações fixas; o procedimento se repete a cada mudança de corte e precisa sair igual. |
| Escolher o ponto de corte | Automação tradicional (varredura de limiares que minimiza o custo esperado com R definido por mim) | A IA não deve decidir: é cálculo com premissa humana, determinístico e auditável. |
| Gerar interface.html | Prompt direto para o template + script Python para embutir os dados | O template é código genérico; embutir dados é determinístico e os dados reais não passam pela IA. |
| Validar a entrada em prever() | Automação tradicional (validação em Python) | Em tempo de execução não há IA; as regras são fixas e testáveis. |
| Redigir a apresentação | Documento colado (saídas do notebook executado) | Prompt direto inventaria números; colando as saídas, cada número é rastreável ao notebook. |