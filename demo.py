"""demo.py - carrega o modelo salvo em disco e faz previsoes. NAO retreina nada.

Uso:
    pip install -r requirements.txt
    python demo.py

Decisao apoiada (papel B, Engenheiro de processo): ajustar ou nao o parametro de laminacao.
Classe 1 = defeito ajustavel por parametro de laminacao; classe 0 = nao ajustavel por parametro.
"""
import math                                   # math.isfinite: detecta NaN e infinito
import numbers                                # numbers.Real: aceita int e float (inclusive tipos do numpy)
from pathlib import Path                      # caminhos relativos ao proprio arquivo (nada de caminho absoluto)

import joblib                                 # carrega o modelo salvo em disco
import pandas as pd                           # monta a linha de entrada e le o CSV
import sklearn                                # so para comparar a versao usada no treino com a instalada
from sklearn.model_selection import train_test_split   # so para reproduzir a MESMA divisao (nao treina nada)

RAIZ = Path(__file__).resolve().parent        # pasta onde este arquivo esta (funciona em qualquer maquina)
CAMINHO_MODELO = RAIZ / "modelo.joblib"       # modelo salvo pelo notebook (caminho relativo, nada a editar)
CAMINHO_DADOS = RAIZ / "data" / "steel_plates.csv"   # base usada so para pegar exemplos de teste


_AVISO_VERSAO = []                                           # guarda se o aviso de versao ja foi mostrado (evita repetir)


def _carregar():
    """Carrega do disco o pacote do modelo (modelo + metadados)."""
    if not CAMINHO_MODELO.exists():                          # se o arquivo nao existe...
        raise FileNotFoundError(f"modelo nao encontrado: {CAMINHO_MODELO}")   # ...avisa de forma clara
    pacote = joblib.load(CAMINHO_MODELO)                     # carrega o dicionario salvo no notebook
    treino = pacote.get("versoes", {}).get("scikit-learn")   # versao do scikit-learn usada no treino
    if treino and treino != sklearn.__version__ and not _AVISO_VERSAO:   # versao instalada diferente da do treino
        print(f"AVISO: modelo salvo com scikit-learn {treino}, mas a versao instalada e {sklearn.__version__}. "
              "Use 'pip install -r requirements.txt' (versoes fixas) para resultados garantidos.")
        _AVISO_VERSAO.append(True)                           # marca que o aviso ja apareceu
    return pacote                                            # devolve o dicionario com modelo e metadados


def _validar(registro, pacote):
    """Valida a entrada. Em qualquer problema, levanta ValueError com mensagem clara."""
    colunas = pacote["colunas"]                              # nomes das 27 variaveis, na ordem do treino
    if not isinstance(registro, dict):                       # a entrada precisa ser um dicionario
        raise ValueError("registro deve ser um dict {variavel: valor}")
    faltando = sorted(set(colunas) - set(registro))          # variaveis que o treino exige e nao vieram
    sobrando = sorted(set(registro) - set(colunas))          # variaveis que o modelo nao conhece
    if faltando:                                             # se falta alguma...
        raise ValueError(f"variaveis faltando: {faltando}")  # ...recusa e diz quais
    if sobrando:                                             # se veio algo desconhecido...
        raise ValueError(f"variaveis desconhecidas: {sobrando}")   # ...recusa e diz quais
    for col in colunas:                                      # confere o valor de cada variavel
        v = registro[col]                                    # valor informado
        ok = isinstance(v, numbers.Real) and not isinstance(v, bool) and math.isfinite(v)  # numero real e finito
        if not ok:                                           # texto, bool, NaN ou infinito
            raise ValueError(f"valor invalido em {col}: {v!r} (esperado numero finito)")
    soma_aco = registro["TypeOfSteel_A300"] + registro["TypeOfSteel_A400"]   # as duas dummies sao complementares
    if soma_aco != 1:                                        # na base de treino a soma foi sempre 1
        raise ValueError("TypeOfSteel_A300 e TypeOfSteel_A400 devem somar 1")


def prever(registro: dict) -> dict:
    """Recebe um registro {variavel: valor} e devolve classe, probabilidade e revisao humana.

    Retorno: {"classe": 0|1, "rotulo": str, "probabilidade": float,
              "revisao_humana": bool, "motivo_revisao": str|None, "avisos": [str]}
    Regras: p >= corte + largura -> classe 1 automatica; p < corte - largura -> classe 0 automatica;
    entre as duas -> faixa de revisao humana (classe provisoria pelo corte).
    Entrada fora da faixa vista no treino tambem vai para revisao humana.
    """
    pacote = _carregar()                                     # carrega o modelo do disco a cada chamada
    _validar(registro, pacote)                               # recusa entrada invalida antes de prever
    colunas = pacote["colunas"]                              # ordem exata das variaveis do treino
    linha = pd.DataFrame([[registro[c] for c in colunas]], columns=colunas)   # tabela de 1 linha, na ordem certa
    p = float(pacote["modelo"].predict_proba(linha)[0, 1])   # probabilidade da classe 1 (ajustavel)
    corte, largura = pacote["corte"], pacote["largura_faixa"]   # parametros de decisao salvos no notebook
    avisos = []                                              # avisos que nao impedem a previsao
    for col in colunas:                                      # compara cada valor com a faixa vista no treino
        minimo, maximo = pacote["faixas"][col]               # menor e maior valor do treino nesta variavel
        if not (minimo <= registro[col] <= maximo):          # fora da faixa conhecida
            avisos.append(f"{col}={registro[col]} fora da faixa de treino [{minimo}, {maximo}]")
    classe = int(p >= corte)                                 # classe pelo corte (provisoria se cair na faixa)
    motivo = None                                            # motivo da revisao, se houver
    if corte - largura <= p < corte + largura:               # probabilidade "indecisa"
        motivo = "probabilidade na faixa de incerteza"
    if avisos:                                               # entrada atipica
        motivo = "entrada fora da faixa de treino" if motivo is None else motivo + "; entrada fora da faixa de treino"
    return {
        "classe": classe,                                    # 1 = ajustavel por parametro; 0 = nao ajustavel
        "rotulo": pacote["rotulos"][classe],                 # texto da classe
        "probabilidade": round(p, 4),                        # probabilidade da classe 1
        "revisao_humana": motivo is not None,                # True: um humano precisa decidir
        "motivo_revisao": motivo,                            # por que foi para revisao
        "avisos": avisos,                                    # lista de avisos
    }


def _exemplos(pacote, n=8):
    """Pega n casos da MESMA particao de teste do notebook (sem treinar nada)."""
    df = pd.read_csv(CAMINHO_DADOS)                          # le a base
    df["alvo"] = df[pacote["processo"]].sum(axis=1).astype(int)   # recria o alvo (1 = Bumps, Z_Scratch, K_Scatch)
    X = df.drop(columns=pacote["defeitos"] + ["alvo"])       # entradas: sem as 7 colunas de defeito (evita vazamento)
    y = df["alvo"]                                           # alvo binario
    _, X_teste, _, y_teste = train_test_split(X, y, test_size=0.20, random_state=42)   # divisao fixa do enunciado
    return X_teste.head(n), y_teste.head(n)                  # primeiros n casos de teste


def main():
    """Mostra previsoes em casos reais de teste e a validacao de entradas invalidas."""
    pacote = _carregar()                                     # confirma que o modelo carrega do disco
    X, y = _exemplos(pacote)                                 # casos de teste
    print("=== Previsoes em casos de teste (modelo carregado do disco, sem retreinar) ===")
    for (_, linha), real in zip(X.iterrows(), y):            # percorre cada caso e o rotulo real
        r = prever(linha.to_dict())                          # chama a funcao do enunciado
        print(f"real={real} | classe={r['classe']} ({r['rotulo']}) | p={r['probabilidade']:.3f} | "
              f"revisao_humana={r['revisao_humana']}")
    base = X.iloc[0].to_dict()                               # um registro valido para fabricar entradas ruins
    print("\n=== Validacao de entradas invalidas ===")
    casos = {
        "variavel faltando": {k: v for k, v in base.items() if k != "Pixels_Areas"},
        "valor NaN": {**base, "Pixels_Areas": float("nan")},
        "valor texto": {**base, "Pixels_Areas": "abc"},
    }
    for nome, entrada in casos.items():                      # tenta prever com cada entrada ruim
        try:
            prever(entrada)                                  # nao deve devolver previsao
            print(f"{nome}: ERRO - deveria ter sido recusada")
        except ValueError as e:                              # esperado: recusa com mensagem clara
            print(f"{nome}: recusada -> {e}")
    absurdo = prever({**base, "Pixels_Areas": 1e12})         # valor numerico absurdo, mas valido
    print(f"valor absurdo: revisao_humana={absurdo['revisao_humana']} | motivo={absurdo['motivo_revisao']}")


if __name__ == "__main__":                                   # so roda main() quando executado direto
    main()
