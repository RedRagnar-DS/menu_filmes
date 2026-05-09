import os
import json

ARQUIVO_JSON = "filmes.json"

dicionario_filmes = {}
contador = 0


class Filme:
    def adicionar(self, nome, lancamento, genero):
        return {
            "nome": nome,
            "lancamento": lancamento,
            "genero": genero
        }


gerenciador = Filme()


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione Enter para voltar ao menu...")


def exibir_menu():
    limpar_tela()
    print("=" * 50)
    print("         === Menu de Gerenciamento de Filmes ===")
    print("=" * 50)
    print("1 - Adicionar novo filme")
    print("2 - Visualizar filmes adicionados")
    print("3 - Excluir filme")
    print("4 - Inserir filmes no JSON")
    print("5 - Excluir filmes do JSON")
    print("6 - Visualizar filmes do JSON")
    print("7 - Sair")
    print("=" * 50)


# ─── Opção 1: Adicionar ───────────────────────────────────────────────────────
def adicionar_filme():
    global contador
    while True:
        limpar_tela()
        print("=" * 50)
        print("           === Adicionar Filme ===")
        print("=" * 50)

        nome = input("Nome do filme: ").strip()
        if not nome:
            print("Nome não pode ser vazio.")
            pausar()
            continue

        try:
            lancamento = int(input("Ano de lançamento: "))
        except ValueError:
            print("Ano inválido. Digite apenas números.")
            pausar()
            continue

        genero_raw = input("Gênero(s) (separe por vírgula): ").strip()
        genero = [g.strip() for g in genero_raw.split(",") if g.strip()]

        filme = gerenciador.adicionar(nome, lancamento, genero)
        dicionario_filmes[contador] = filme
        contador += 1

        print(f"\n✔  Filme '{nome}' adicionado com sucesso! (ID: {contador - 1})")

        continuar = input("\nDeseja adicionar outro filme? (s/n): ").strip().lower()
        if continuar != "s":
            break


# ─── Opção 2: Visualizar ──────────────────────────────────────────────────────
def visualizar_filmes():
    while True:
        limpar_tela()
        print("=" * 50)
        print("         === Filmes Cadastrados ===")
        print("=" * 50)

        if not dicionario_filmes:
            print("\nNenhum filme cadastrado ainda.")
        else:
            print(f"{'ID':<5} {'Nome':<30} {'Lançamento':<12} {'Gênero'}")
            print("-" * 70)
            for id_filme, dados in dicionario_filmes.items():
                generos = ", ".join(dados["genero"]) if isinstance(dados["genero"], list) else dados["genero"]
                print(f"{id_filme:<5} {dados['nome']:<30} {dados['lancamento']:<12} {generos}")

        continuar = input("\nDeseja visualizar novamente? (s/n): ").strip().lower()
        if continuar != "s":
            break


# ─── Opção 3: Excluir da memória ──────────────────────────────────────────────
def excluir_filme():
    while True:
        limpar_tela()
        print("=" * 50)
        print("            === Excluir Filme ===")
        print("=" * 50)

        if not dicionario_filmes:
            print("\nNenhum filme cadastrado para excluir.")
            pausar()
            break

        print(f"{'ID':<5} {'Nome':<30} {'Lançamento'}")
        print("-" * 50)
        for id_filme, dados in dicionario_filmes.items():
            print(f"{id_filme:<5} {dados['nome']:<30} {dados['lancamento']}")

        entrada = input("\nDigite o ID do filme a excluir (ou 'sair' para voltar): ").strip().lower()
        if entrada == "sair":
            break

        try:
            id_excluir = int(entrada)
        except ValueError:
            print("ID inválido.")
            pausar()
            continue

        if id_excluir in dicionario_filmes:
            nome_excluido = dicionario_filmes[id_excluir]["nome"]
            del dicionario_filmes[id_excluir]
            print(f"\n✔  Filme '{nome_excluido}' removido com sucesso!")
        else:
            print("\n✘  ID não encontrado.")

        continuar = input("\nDeseja excluir outro filme? (s/n): ").strip().lower()
        if continuar != "s":
            break


# ─── Opção 4: Salvar no JSON ──────────────────────────────────────────────────
def inserir_json():
    limpar_tela()
    print("=" * 50)
    print("          === Inserir Filmes no JSON ===")
    print("=" * 50)

    if not dicionario_filmes:
        print("\nNenhum filme em memória para salvar.")
        pausar()
        return

    # Carrega dados existentes no arquivo para não sobrescrever
    dados_existentes = []
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            try:
                dados_existentes = json.load(f)
            except json.JSONDecodeError:
                dados_existentes = []

    # Adiciona filmes em memória que ainda não estão no arquivo (pelo nome)
    nomes_existentes = {filme["nome"].lower() for filme in dados_existentes}
    novos = []
    for dados in dicionario_filmes.values():
        if dados["nome"].lower() not in nomes_existentes:
            novos.append(dados)

    dados_existentes.extend(novos)

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados_existentes, f, ensure_ascii=False, indent=4)

    print(f"\n✔  {len(novos)} filme(s) novo(s) salvo(s) em '{ARQUIVO_JSON}'.")
    if len(novos) < len(dicionario_filmes):
        print(f"   ({len(dicionario_filmes) - len(novos)} já existia(m) no arquivo e foram ignorados.)")
    pausar()


# ─── Opção 5: Excluir do JSON ─────────────────────────────────────────────────
def excluir_json():
    limpar_tela()
    print("=" * 50)
    print("         === Excluir Filmes do JSON ===")
    print("=" * 50)

    if not os.path.exists(ARQUIVO_JSON):
        print(f"\nArquivo '{ARQUIVO_JSON}' não encontrado.")
        pausar()
        return

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        try:
            filmes_json = json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            pausar()
            return

    if not filmes_json:
        print("\nO arquivo JSON está vazio.")
        pausar()
        return

    while True:
        limpar_tela()
        print("=" * 50)
        print("         === Excluir Filmes do JSON ===")
        print("=" * 50)
        print(f"{'Nº':<5} {'Nome':<30} {'Lançamento'}")
        print("-" * 50)
        for idx, filme in enumerate(filmes_json):
            print(f"{idx:<5} {filme['nome']:<30} {filme['lancamento']}")

        entrada = input("\nDigite o Nº do filme a excluir (ou 'sair' para voltar): ").strip().lower()
        if entrada == "sair":
            break

        try:
            idx_excluir = int(entrada)
        except ValueError:
            print("Entrada inválida.")
            pausar()
            continue

        if 0 <= idx_excluir < len(filmes_json):
            nome_excluido = filmes_json[idx_excluir]["nome"]
            filmes_json.pop(idx_excluir)

            with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
                json.dump(filmes_json, f, ensure_ascii=False, indent=4)

            print(f"\n✔  Filme '{nome_excluido}' removido do JSON com sucesso!")
        else:
            print("\n✘  Número fora do intervalo.")

        if not filmes_json:
            print("\nNão há mais filmes no JSON.")
            pausar()
            break

        continuar = input("\nDeseja excluir outro filme do JSON? (s/n): ").strip().lower()
        if continuar != "s":
            break


# ─── Opção 6: Visualizar do JSON ─────────────────────────────────────────────
def visualizar_json():
    while True:
        limpar_tela()
        print("=" * 50)
        print("        === Visualizar Filmes do JSON ===")
        print("=" * 50)

        if not os.path.exists(ARQUIVO_JSON):
            print(f"\nArquivo '{ARQUIVO_JSON}' não encontrado.")
            pausar()
            break

        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            try:
                filmes_json = json.load(f)
            except json.JSONDecodeError:
                print("Erro ao ler o arquivo JSON.")
                pausar()
                break

        if not filmes_json:
            print("\nO arquivo JSON está vazio.")
            pausar()
            break

        print(f"{'Nº':<5} {'Nome':<30} {'Lançamento':<12} {'Gênero'}")
        print("-" * 70)
        for idx, filme in enumerate(filmes_json):
            generos = ", ".join(filme["genero"]) if isinstance(filme["genero"], list) else filme["genero"]
            print(f"{idx:<5} {filme['nome']:<30} {filme['lancamento']:<12} {generos}")

        print(f"\nTotal: {len(filmes_json)} filme(s) no arquivo.")

        continuar = input("\nDeseja visualizar novamente? (s/n): ").strip().lower()
        if continuar != "s":
            break


# ─── Loop principal ───────────────────────────────────────────────────────────
while True:
    exibir_menu()
    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        adicionar_filme()
    elif opcao == "2":
        visualizar_filmes()
    elif opcao == "3":
        excluir_filme()
    elif opcao == "4":
        inserir_json()
    elif opcao == "5":
        excluir_json()
    elif opcao == "6":
        visualizar_json()
    elif opcao == "7":
        limpar_tela()
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
        pausar()