usuarios = {}

def cadastrar_usuario():
    print("Cadastro de Novo Usuário:")
    nome = input("Nome: ")
    email = input("E-mail: ")

    # Verifica se o e-mail já está cadastrado
    while email in usuarios:
        print("Este e-mail já está cadastrado. Por favor, escolha outro.")
        email = input("E-mail: ")

    senha = input("Senha: ")
    telefone = input("Telefone: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    informacoes_adicionais = input("Informações Adicionais: ")
    documentos = input("Documentos: ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    cep = input("CEP: ")
    cpf = input("CPF: ")

    usuarios[email] = {
        'nome': nome,
        'senha': senha,
        'telefone': telefone,
        'data_nascimento': data_nascimento,
        'informacoes_adicionais': informacoes_adicionais,
        'documentos': documentos,
        'endereco': endereco,
        'cidade': cidade,
        'cep': cep,
        'cpf': cpf
    }

    print("Usuário cadastrado com sucesso!")

def excluir_usuario():
    print("Excluir Usuário:")
    email = input("E-mail do usuário a ser excluído: ")

    # Verifica se o e-mail existe antes de excluir
    if email in usuarios:
        del usuarios[email]
        print("Usuário excluído com sucesso!")
    else:
        print("E-mail não encontrado. Nenhum usuário foi excluído.")

def verificar_usuario():
    print("Verificar Usuário:")
    email = input("E-mail: ")
    senha = input("Senha: ")

    # Verifica se o e-mail e a senha correspondem a um usuário registrado
    if email in usuarios and usuarios[email]['senha'] == senha:
        print(f"\nInformações do Usuário:")
        print(f"Nome: {usuarios[email]['nome']}")
        print(f"E-mail: {email}")
        print(f"Telefone: {usuarios[email]['telefone']}")
        print(f"Data de Nascimento: {usuarios[email]['data_nascimento']}")
        print(f"Informações Adicionais: {usuarios[email]['informacoes_adicionais']}")
        print(f"Documentos: {usuarios[email]['documentos']}")
        print(f"Endereço: {usuarios[email]['endereco']}")
        print(f"Cidade: {usuarios[email]['cidade']}")
        print(f"CEP: {usuarios[email]['cep']}")
        print(f"CPF: {usuarios[email]['cpf']}")
    else:
        print("E-mail ou senha incorretos. Verifique suas credenciais.")

def verificar_existencia_usuario(email):
    return email in usuarios

def menu():
    while True:
        print("\nCadastro de Usuários")
        print("1 - Cadastrar Novo Usuário")
        print("2 - Excluir Usuário")
        print("3 - Verificar Usuário")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            excluir_usuario()
        elif opcao == '3':
            verificar_usuario()
        elif opcao == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
