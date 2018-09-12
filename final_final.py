class Pessoa:

    def __init__(self, nome, cpf, dataNascimento):

        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento


class Aluno(Pessoa):
    def __init__(self, nome, cpf, dataNascimento, endereco, telefone, cadastrado = True):
        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        self.telefone = telefone
        self.cadastrado = True

    def cadastrarAluno(self):
        c = 0
        d = 0
        f = open('alunos.txt', '+a')
        print("Cadastre um aluno!")

        n = input("Digite o nome do(a) aluno(a): ")
        m = input("Digite o  RA  do(a) aluno(a): ")

        c = "Aluno(a): " + n + "\n"
        d = "RA......: " + m + "\n"
        f.write("--------------------------------------------\n")
        f.write(c)
        f.write(d)
        f.write("--------------------------------------------\n")

    def editarAluno(self):
        g = open('dados_alunos.txt', '+a')
        edi = str(input("Caso deseje alterar  os dados do aluno, digite SIM: "))

        if edi in ['sim', 's', 'S', 'SIM']:
            self.nome = str(input("Nome: "))
            self.cpf = str(input("CPF: "))
            self.dataNascimento = str(input("Data de Nascimento: "))
            self.endereco = str(input("Endereço: "))            
            self.telefone = str(input("Telefone: "))

            g.write("--------------------------------------------\n")
            g.write("Nome..............: {}\n" .format(self.nome))
            g.write("CPF...............: {}\n" .format(self.cpf))
            g.write("Data de Nascimento: {}\n" .format(self.dataNascimento))
            g.write("Endereço..........: {}\n" .format(self.endereco))
            g.write("Telefone..........: {}\n" .format(self.telefone))
            g.write("--------------------------------------------\n")

            
            print("Dados atualizados!")

        else:
            print("Dados não foram alterados!")    


    def desabilita(self):
        self.cadastrado = False
        #print(self.cadastrado)

    def habilitar(self):
        self.cadastrado = True
        #print(self.cadastrado)


y = Aluno("Renato", 37804343850, "09/12/1989", "rua Augusto Baer", 976334348)
y.cadastrarAluno()
y.editarAluno()
y.desabilita()
y.habilitar()

class professor:
    listaProfessores = []
    def __init__(self, nome, cpf, dataNascimento, endereco, telefone, status = 'Ativo'):
        self.nome = nome
        self. cpf = cpf
        self.dataNascimento = dataNascimento
        self.endereco = endereco
        self. telefone = telefone
        self.status = 'Ativo'
    
    def Cadastrar (self):
        
        self.nome = input("Digite o nome do professor: ").upper()
        self.cpf = input("Digite o CPF do professor: ")
        self.dataNascimento = input("Digite a data de nascimento do professor: ")
        self.endereco = input("Digite o endereço: ").upper()
        self.telefone = input("Digite o telefone: ")

    
    def listas(self):
        self.listaProfessores = []
        self.listaProfessores.append([self.nome, self.cpf, self.dataNascimento, self.endereco, self.telefone])
        
        with open ('professores.txt', 'a+') as Prof:
            Prof.write("--------------------------------------------\n")
            Prof.write("Nome do professor: {}\n" .format(self.nome))
            Prof.write("CPF: {}\n" .format(self.cpf))
            Prof.write("Data de nascimento: {}\n" .format(self.dataNascimento))
            Prof.write("Endereço: {}\n" .format(self.endereco))
            Prof.write("Telefone: {}\n" .format(self.telefone))
            Prof.write("--------------------------------------------\n")


    def editar(self):
         
        continua = True
        doc = input("Digite o CPF para consulta: ")

        while continua:
            if doc in self.cpf:
                print("+-----------------------------------------+")
                print("|   Digite os novos dados de contato      |")
                print("+-----------------------------------------+") 
                self.endereco = input("Digite o endereço: ").upper()
                self.telefone = input("Digite o telefone: ")
                print("+-----------------------------------+")
                print("|   Cadastro alterado com sucesso!  |")
                print("+-----------------------------------+")

                continua = False
            else:
                print("CPF não cadastrado")
                return doc
            
            with open ('professores.txt', 'a+') as Prof:
                Prof.write("--------------------------------------------\n")
                Prof.write("Nome do professor: {}\n" .format(self.nome))
                Prof.write("CPF: {}\n" .format(self.cpf))
                Prof.write("Data de nascimento: {}\n" .format(self.dataNascimento))
                Prof.write("Endereço: {}\n" .format(self.endereco))
                Prof.write("Telefone: {}\n" .format(self.telefone))
                Prof.write("--------------------------------------------\n")
        
    def cancela_cad(self):
        loc_cpf1 = input("Buscar CPF para cancelar o cadastro: ")
        if loc_cpf1 in self.cpf:
            self.status = 'Cancelado'
            print('Status do cadastro: ', self.status)
        else:
            print("CPF não cadastrado!")
        

    def ativa_cad(self):
        loc_cpf2 = input("Buscar CPF para ativar o cadastro: ")
        if loc_cpf2 in self.cpf:
            self.status = 'Ativo'
            print('Status do cadastro: ', self.status)
        else:
            print("CPF não cadastrado!")

     

p = professor('Irineu',"045.548.658-98","05/04/1994","SP","994568475")

p.Cadastrar()
print('\n')
print("+-----------------------------------+")
p.listas()
print('\n')
p.editar()
print("+-----------------------------------+")
p.cancela_cad()
print("+-----------------------------------+")
p.ativa_cad()

class disciplina:
    def __init__(self, nome, cargaHoraria, percentualPratico, percentualTeorico, professor):
        self.nome = nome
        self.cargaHoraria = cargaHoraria
        self.percentualPratico = percentualPratico
        self.percentualTeorico = percentualTeorico
        self.professor = professor

        auxDisciplinas = []
        nomeDB = {}
        cargaHorariaDB = {}
        percPraticoDB = {}
        percTeoricoDB = {}
        professorDB = {}

        with open("disciplinas.txt") as f:
            aux = f.read().splitlines()
            f.close()

        for item in aux:
            auxDisciplinas = item.split(";")
            nomeDB[auxDisciplinas[0]] = auxDisciplinas[0]
            cargaHorariaDB[auxDisciplinas[0]] = auxDisciplinas[1]
            percPraticoDB[auxDisciplinas[0]] = auxDisciplinas[2]
            percTeoricoDB[auxDisciplinas[0]] = auxDisciplinas[3]
            professorDB[auxDisciplinas[0]] = auxDisciplinas[4]

        if self.nome in nomeDB:
            print("Disciplina já cadastrada!\n")
        else:        
            DB = open("disciplinas.txt", "a+")

            nomeDB[self.nome] = self.nome
            cargaHorariaDB[self.nome] = self.cargaHoraria
            percPraticoDB[self.nome] = self.percentualPratico
            percTeoricoDB[self.nome] = self.percentualTeorico
            professorDB[self.nome] = self.professor

            for j in nomeDB:
                DB.write(nomeDB[j] + ';' + cargaHorariaDB[j] + ';' + percPraticoDB[j] + ';' + percTeoricoDB[j] + ';' + professorDB[j] + '\n')

            DB.close()

            print("Disciplina cadastrada com sucesso!\n")

z = disciplina("DevOps", "100%", "50%", "50%", "Eurico")

class curso:
    listaCurso = {}
    cursosCadastrados = []

    def __init__(self, nome, periodo, disciplinas = [], status = "Desativado"):

        self.nome = nome + "*"

        self.periodo = periodo

        self.disciplinas = disciplinas

        self.status = "Desativado"

        self.listaCurso[self.nome] = {"Nome":self.nome, "Periodo":self.periodo, "Disciplina":self.disciplinas, "Status":self.status}

    def cadastraCurso(self):

        if self.listaCurso[self.nome]["Nome"] == "Desativado":
            self.listaCurso[self.nome]["Status"] = "Ativado"
        
        self.cursosCadastrados.append(self.nome)
        self.listaCurso[self.nome]["Status"] = "Ativado"
        
        with open('cursos.txt', 'a+') as Cursos:

            Cursos.write(self.nome + ";" + self.periodo + ";")

            Cursos.close()

        

    def Cursos(self):

        with open('cursos.txt', 'r') as Cursos:

            for item in Cursos:
                item = item.splitlines()
                for item in item:
                    item2 = item.split(";")
                    if '*' in item2:
                        self.cursosCadastrados.append(item2)
        Cursos.close()

        return self.cursosCadastrados

    def exibeCursos(self):

        for curso in self.cursosCadastrados:
            print("*"*20)
            print("Nome: {}" .format(self.listaCurso[curso]["Nome"]))
            print("Periodo: {}" .format(self.listaCurso[curso]["Periodo"]))
            print("Disciplinas {}" .format(self.listaCurso[curso]["Disciplina"]))
            print("Status {}" .format(self.listaCurso[curso]["Status"]))
            print("*"*20)


    def alteraStatus(self):
        if self.listaCurso[self.nome]["Status"] == "Ativado":
            self.listaCurso[self.nome]["Status"] = "Desativado"

        elif self.listaCurso[self.nome]["Status"] == "Desativado":
            self.listaCurso[self.nome]["Status"] = "Ativado"


ADS = curso("ADS", "Manha",["Lógica", "Programação"])
ADS.cadastraCurso()
Banco = curso("Banco", "Noite", ["Banco de dados", "Linguagem SQL"])
Banco.cadastraCurso()
SI = curso("SI", "Tarde", ["Modelagem", "Gestão"])
SI.cadastraCurso()
Banco.alteraStatus()
SI.exibeCursos()