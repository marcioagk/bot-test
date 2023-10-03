import os
import sys


def main():
    # Verificar se foi fornecido um argumento
    if len(sys.argv) > 1:
        pasta = sys.argv[1]
    else:
        pasta = ""
    print(pasta)

    # Construir o caminho para o script dentro da pasta
    script_nome = "botcr.py"  # Nome do script a ser executado
    script_path = os.path.join(pasta, script_nome)
    print(script_path)

    # Verificar se o script existe
    if not os.path.exists(script_path):
        print(f"O script '{script_nome}' não existe na pasta '{pasta}'.")
        sys.exit(1)

    print('PASSOU AQUI!')

    # Executar o script
    try:
        exec(open(script_path).read())
    except Exception as e:
        print(f"Erro ao executar o script '{script_nome}': {str(e)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
