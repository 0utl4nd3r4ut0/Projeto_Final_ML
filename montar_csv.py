from pathlib import Path  # Importa a classe Path para manipulação moderna de caminhos de arquivos de forma independente do SO
import datetime           # Importa o módulo datetime para trabalhar com datas
import pandas as pd       # Importa a biblioteca Pandas e a apelida de 'pd' para manipulação de tabelas de dados

RAIZ = Path(__file__).parent             # Define a variável RAIZ com o diretório onde este script Python está salvo
BRUTO = RAIZ / "data" / "bruto"          # Define o caminho para a pasta de dados brutos dentro da estrutura do projeto

# Lê o arquivo de dados brutos (.NNA), usando espaços em branco (regex) como separador e indicando que o arquivo não tem cabeçalho
dados = pd.read_csv(BRUTO / "Faults.NNA", sep=r"\s+", header=None)

# Lê o arquivo de variáveis, limpa os espaços em branco de cada linha e ignora linhas vazias para criar a lista com os nomes das colunas
nomes = [l.strip() for l in (BRUTO / "Faults27x7_var").read_text().splitlines() if l.strip()]

print("dados:", dados.shape, "| nomes:", len(nomes))   # Imprime as dimensões do dataset (linhas, colunas) e a quantidade de nomes lidos

# Faz uma validação rigorosa: garante que o número de colunas e o total de nomes sejam exatamente 34, gerando um erro se não baterem
assert dados.shape[1] == len(nomes) == 34, "colunas e nomes não batem"

dados.columns = nomes                          # Atribui oficialmente a lista de nomes carregada como o cabeçalho (colunas) do DataFrame
dados.to_csv(RAIZ / "data" / "steel_plates.csv", index=False)  # Salva o DataFrame tratado e limpo em um novo arquivo CSV, sem incluir o índice

# Cria e escreve um arquivo de texto 'ACESSO.txt' documentando a origem e metadados do dataset
(RAIZ / "data" / "ACESSO.txt").write_text(
    "Steel Plates Faults (UCI, ID 198), DOI 10.24432/C5J88N\n"        # Linha 1: Nome do dataset, ID na UCI e DOI
    f"Acesso em: {datetime.date.today()}\n"                          # Linha 2: Insere dinamicamente a data atual do acesso
    "Fonte: https://archive.ics.uci.edu/dataset/198/steel+plates+faults\n"  # Linha 3: Link direto para a página do dataset
)

# --- checagens do Passo 1 ---
df = pd.read_csv(RAIZ / "data" / "steel_plates.csv")  # Lê novamente o arquivo CSV limpo gerado anteriormente para iniciar as validações

# Cria uma lista contendo os nomes exatos das colunas que representam os diferentes tipos de defeitos nas placas de aço
defeitos = ["Pastry", "Z_Scratch", "K_Scatch", "Stains", "Dirtiness", "Bumps", "Other_Faults"]

print("shape:", df.shape)                                      # Exibe as dimensões finais (linhas e colunas) do DataFrame carregado
print("ausentes:", int(df.isna().sum().sum()))                 # Conta e exibe o número total de valores nulos/ausentes em toda a tabela
print("duplicadas:", int(df.duplicated().sum()))               # Conta e exibe a quantidade de linhas totalmente duplicadas no dataset
print(df[defeitos].sum().sort_values(ascending=False))         # Soma a ocorrência de cada tipo de defeito e os ordena do mais frequente para o menos frequente
print("soma por linha:\n", df[defeitos].sum(axis=1).value_counts())  # Soma os defeitos linha por linha e conta quantas amostras possuem 0, 1, 2, etc. defeitos simultâneos