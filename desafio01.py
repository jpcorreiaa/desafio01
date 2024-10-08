def adicionar_contato(contatos, nome_contato, email_contato, telefone_contato):
    contato = {
        "nome": nome_contato, 
        "telefone": telefone_contato, 
        "email": email_contato, 
        "favorito": False  # Por padrão, o contato não será favorito
    }
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de Contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status_favorito = "⭐" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        
        # Exibe todas as informações do contato
        print(f"{indice}. [{status_favorito}] Nome: {nome_contato}")
        print(f"Telefone: {telefone_contato}")
        print(f"Email: {email_contato}")
    return


def atualizar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1  # Ajuste para o índice começar de 0
    
    if 0 <= indice_contato_ajustado < len(contatos):  # Verifica se o índice é válido
        contato = contatos[indice_contato_ajustado]  # Seleciona o contato a ser atualizado

        # Exibir as opções de edição
        print("O que você gostaria de atualizar?")
        print("1. Nome")
        print("2. Telefone")
        print("3. Email")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            novo_nome = input("Digite o novo nome: ")
            contato["nome"] = novo_nome
            print(f"Nome atualizado para {novo_nome}.")
            
        elif opcao == "2":
            novo_telefone = input("Digite o novo telefone: ")
            contato["telefone"] = novo_telefone
            print(f"Telefone atualizado para {novo_telefone}.")
            
        elif opcao == "3":
            novo_email = input("Digite o novo email: ")
            contato["email"] = novo_email
            print(f"Email atualizado para {novo_email}.")
            
def marcar_desmarcar_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1  # Ajusta para índice baseado em 0
    
    if 0 <= indice_contato_ajustado < len(contatos):  # Verifica se o índice é válido
        contato = contatos[indice_contato_ajustado]  # Seleciona o contato
        
        # Alterna o estado do favorito
        contato["favorito"] = not contato["favorito"]
        
        if contato["favorito"]:
            print(f"{contato['nome']} foi marcado como favorito.")
        else:
            print(f"{contato['nome']} não é mais favorito.")
    else:
        print("Índice de contato inválido.")
    return

def ver_contatos_favoritos(contatos):
    print("\nLista de Contatos Favoritos:")
    # Filtra os contatos que são favoritos
    contatos_favoritos = [contato for contato in contatos if contato["favorito"]]

    # Verifica se há contatos favoritos
    if not contatos_favoritos:
        print("Nenhum contato favorito encontrado.")
        return

    for indice, contato in enumerate(contatos_favoritos, start=1):
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        
        # Exibe todas as informações do contato favorito
        print(f"{indice}. Nome: {nome_contato}")
        print(f"   Telefone: {telefone_contato}")
        print(f"   Email: {email_contato}")


def deletar_contatos(contatos):
    ver_contatos(contatos)  # Exibe a lista de contatos antes da deleção
    indice_contato = input("Digite o número do contato que deseja deletar: ")
    
    try:
        indice_contato_ajustado = int(indice_contato) - 1  # Ajusta para índice baseado em 0
        if 0 <= indice_contato_ajustado < len(contatos):  # Verifica se o índice é válido
            contato_removido = contatos[indice_contato_ajustado]
            contatos.pop(indice_contato_ajustado)  # Remove o contato da lista
            print(f"Contato {contato_removido['nome']} deletado com sucesso.")
        else:
            print("Índice de contato inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")


contatos = []

while True:
    print("\nMenu do gerenciador de Lista de Contatos:")
    print("1. Adicionar Contato")
    print("2. Ver Lista de Contato")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar contato favorito")
    print("5. Ver Lista de Contatos Favoritos")
    print("6. Deletar contatos")
    print("7. Sair")

    
    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input ("Digite o telefone do contato que deseja adicionar: ")
        email_contato = input("Digite o email do contato que deseja adicionar: ")
        adicionar_contato(contatos,nome_contato ,telefone_contato, email_contato)
    
    elif escolha == "2":
        ver_contatos(contatos)
    
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja atualizar: ")
        atualizar_contato(contatos, indice_contato)
    
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja marcar/desmarcar como favorito: ")
        marcar_desmarcar_favorito(contatos, indice_contato)

    elif escolha == "5":
        ver_contatos_favoritos(contatos)
    
    elif escolha == "6":
        deletar_contatos(contatos)
        ver_contatos(contatos)
    
    elif escolha == "7":
        break

print("Programa finalizado")