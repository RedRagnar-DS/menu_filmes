# 🎬 Menu de Gerenciamento de Filmes

Sistema de gerenciamento de filmes via terminal desenvolvido em Python. Permite cadastrar, visualizar, excluir e persistir filmes em um arquivo JSON.

---

## 📋 Funcionalidades

| Opção | Descrição |
|-------|-----------|
| 1 | Adicionar novo filme |
| 2 | Visualizar filmes cadastrados |
| 3 | Excluir filme da memória |
| 4 | Salvar filmes no arquivo JSON |
| 5 | Excluir filmes do arquivo JSON |
| 6 | Visualizar filmes do arquivo JSON |
| 7 | Sair do programa |

---

## 🚀 Como executar

**Pré-requisitos:** Python 3.6 ou superior instalado.

```bash
# Clone o repositório
git clone https://github.com/RedRagnar-DS/menu_filmes.git

# Acesse a pasta
cd menu_filmes

# Execute o programa
python menu_ronaldinho.py
```

> Nenhuma biblioteca externa é necessária. O projeto usa apenas módulos da biblioteca padrão do Python (`os` e `json`).

---

## 🗂️ Estrutura do projeto

```
📁 menu_filmes/
├── menu_ronaldinho.py   # Script principal
├── filmes.json      # Gerado automaticamente ao salvar filmes
└── README.md
```

---

## 📖 Como usar cada opção

### 1 — Adicionar novo filme
Solicita **nome**, **ano de lançamento** e **gênero(s)** (separados por vírgula). Após cada cadastro, pergunta se deseja adicionar outro filme. O filme é salvo temporariamente na memória do programa.

```
Nome do filme: Interestelar
Ano de lançamento: 2014
Gênero(s): Ficção Científica, Drama
```

### 2 — Visualizar filmes cadastrados
Exibe uma tabela com todos os filmes em memória, mostrando ID, nome, ano de lançamento e gênero(s). Pergunta se deseja visualizar novamente ao final.

```
ID    Nome                           Lançamento   Gênero
----------------------------------------------------------------------
0     Interestelar                   2014         Ficção Científica, Drama
```

### 3 — Excluir filme da memória
Lista os filmes cadastrados e solicita o ID do filme a remover. Digite `sair` a qualquer momento para cancelar e voltar ao menu sem excluir nada.

### 4 — Inserir filmes no JSON
Salva os filmes que estão em memória no arquivo `filmes.json`. Filmes com o mesmo nome que já existem no arquivo são ignorados automaticamente, evitando duplicatas.

Exemplo do arquivo gerado:
```json
[
    {
        "nome": "Interestelar",
        "lancamento": 2014,
        "genero": ["Ficção Científica", "Drama"]
    }
]
```

### 5 — Excluir filmes do JSON
Lê o arquivo `filmes.json`, lista os filmes e permite removê-los pelo número. Digite `sair` para cancelar e voltar ao menu sem excluir nada.

### 6 — Visualizar filmes do JSON
Lê o arquivo `filmes.json` e exibe uma tabela formatada com Nº, Nome, Ano de lançamento e Gênero(s), além do total de filmes salvos no arquivo. Pergunta se deseja visualizar novamente ao final.

### 7 — Sair
Encerra o programa.

---

## 🛡️ Validações implementadas

- Nome do filme não pode ser vazio
- Ano de lançamento aceita apenas números inteiros
- Nas telas de exclusão, é possível digitar `sair` para voltar ao menu sem realizar nenhuma ação
- Ao salvar no JSON, duplicatas são detectadas pelo nome (sem diferenciação de maiúsculas/minúsculas)
- Leitura e escrita do JSON com tratamento de erros (`JSONDecodeError`)

---

## 💡 Conceitos aplicados

- Programação Orientada a Objetos (classe `Filme`)
- Estruturas de repetição com `while`
- Persistência de dados com JSON (`json.load` / `json.dump`)
- Manipulação de dicionários
- Tratamento de exceções com `try/except`
- Compatibilidade multiplataforma para limpeza de tela (`cls` / `clear`)

---

## 👤 Autor

Feito por **seu-nome** — sinta-se à vontade para abrir issues ou contribuir com melhorias!
