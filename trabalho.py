class Tarefas:
    incrementa_id = 1
    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = "Pendente"
        self.id = Tarefas.incrementa_id
        Tarefas.incrementa_id +=1

    def __srt__(self):
        return f"Tarefa {self.titulo} - {self.descricao} - {self.prioridade}"

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.lista_tarefas = []
    #---------------------
    
    def criar_tarefa(self, titulo, descricao, prioridade):
        nova_tarefa = Tarefas(titulo, descricao, prioridade)
        self.lista_tarefas.append(nova_tarefa)

    #------------------- \trabalho-projeto> py .\trabalho.py
    # PS C:\Users\Karen Cristina\Documents

    def listar_tarefas(self, status=None):
         for tarefa in self.listar_tarefas:
            print(f"lista de tarefas {self.Tarefas}")

    def procura_tarefa(self, id_tarefa):
        for tarefa in self.lista_tarefas:
            if tarefa.id == id_tarefa:
                return tarefa
        return None
    
    def remover_tarefa(self, id_tarefa):
        tarefa_buscada = self.procura_tarefa(id_tarefa)
        if tarefa_buscada:
            self.lista_tarefas.remove(tarefa_buscada)
        else:
            print("tarefa nãoo encontrada")

    def concluir_tarefa(self):
        self.status = "concluída"
        print(f"tarefa: {self.titulo} concluída!")

    def concluir_tarefa(self):
        self.status = "concluída"
        print|(f"tarefa: {self.tiutulo} concluída!")

    def limpar_concluidas(self):
        tarefas_ativas = []
        for tarefa in self.lista_tarefas:
            if tarefa.status != "Concluída":
                tarefas_ativas.append(tarefa)
            self.lista_tarefas = tarefas_ativas
  
class Sistema:
    def __init__(self):
        self.lista_usuarios = []
        self.usuario_logado = None
        
    def cadastrar_usuario(self):
        nome = input("nome de usuário: ")
        email = input("email: ")
        senha = input("senha: ")
        
        if "@" not in email:
            print("email inválido")
            return
        else:
            novo_usuario = Usuario(nome, email, senha)
            self.lista_usuarios.append(novo_usuario)
            print("Usuário cadastrado com sucesso.")
            
    def login(self):
        email = input("digite seu email: ")
        senha = input("digite seu senha: ")
        
        for usuario in self.lista_usuarios:
            if email == usuario.email and  senha == usuario.senha:
                self.usuario_logado = usuario
                print(f"usuario logado: {self.usuario_logado.nome}")
                self.menu_funcionalidades()
                return
            
            print("Usuário não encontrado")
    
    def menu_principal(self):
        opcao_escolhida = ""
        while opcao_escolhida != "0":
            print("------------------------")
            print("escolha uma das opções: ")
            print(" 1 - cadastrar usuário")
            print("2 - fazer login")
            print("0 - sair: \n")
            opcao_escolhida = input("escolha: ")
        
            if opcao_escolhida == "1":
                self.cadastrar_usuario()
            elif opcao_escolhida == "2":
                self.login()
            elif opcao_escolhida == "0":
                print("Saindo")
            else:
                print("opção inválida")
                
    def menu_funcionalidades(self):
        escolha = ""
        while escolha != "0":
            print("\n ----------- Tarefas ------------")
            print(" 1 criar tarefa")
            print(" 2 - listar tarefas")
            print("3 - pendentes")
            print("4 - listar tarefas concluídas")
            print("5 - concluir tarefa")
            print("6 - editar tarefa")
            print("7 - remover tarefa")
            escolha = input("Selecione: ")

            if escolha == "1":
                titulo = input("insira um título: ")
                descricao = input("insira uma descricao: ")
                prioridade = input("insira um prioridade (alta, média ou baixa): ")
                self.usuario_logado.criar_tarefa(titulo, descricao, prioridade)
            #!!!!!!!!!! ------------
            elif escolha == "2":
                self.usuario_logado.listar_tarefas()
            elif escolha == "3":
                self.usuario_logado.lista_tarefas("Pendentes")
            elif escolha == "4":
                self.usuario_logado.lista_tarefas("concluídas")
                #--------------------------
            elif escolha == "5":
                id = input("insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.procura_tarefa(int(id))
                    if tarefa_buscada:
                        tarefa_buscada.concluir_tarefa()
                    else:
                        print("tarefa não encontrada!")

            elif escolha == "6":
                id = input("insira o ID da Tarefa: ")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.procura_tarefa(int(id))
                    if tarefa_buscada:
                                novo_titulo = input("insira o titulo: ")
                                nova_descricao = input("insira nova descrição: ")
                                nova_prioridade = input("insira nova prioridade: ")
                                tarefa_buscada.editar_tarefa(novo_titulo, nova_descricao, nova_prioridade)

                    else:
                        print("tarefa não encontrada!")
            elif escolha == "7":
                id = input("insira o id da tarefa")
                if id.isdigit():
                    tarefa_buscada = self.usuario_logado.remover_tarefa(int(id))
            elif escolha == "8":
                self.usuario_logado.limpar_concluidas()
        
teste = Sistema()
teste.menu_principal()