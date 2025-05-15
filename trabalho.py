#class Tarefas

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
class Sistema:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_logado = None
        
    def cadastrar_usuario(self):
        nome = input("nome de usuário: ")
        email = input("email: ")
        
        if "@" not in email:
            print("email inválido")
            return
        else:
            novo_usuario = Usuario(nome, email)
            self.lista_usuarios.append(novo_usuario)
            print("Usuário cadastrado com sucesso.")
        
    def login(self):
        email = input("digite seu email")
        
        for usuario in self.lista_usuarios:
            if email == email:
                self.usuario_logado = usuario
                print(f"usuario logado: {self.usuario_logado.nome}")
                return
            
            print("Usuário não encontrado")

    def menu_principal(self):
        opcao_escolhida = ""
        while opcao_escolhida != "0":
            print("escolha uma das opções: ")
            print(" 1 - cadastrar usuário")
            print("2 - fazer login")
            print("0 - sair: \n")
            opcao_escolhida = input("escolha")
        
            if opcao_escolhida == "1":
                self.cadastrar_usuario()
            elif opcao_escolhida == "2":
                self.login()
            elif opcao_escolhida == "0":
                print("Saindo")
            else:
                print("opção inválida")
    
teste = Sistema()

teste.menu_principal()