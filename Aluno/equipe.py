#coding: utf-8

from Aluno import aluno


class equipe:

    def __init__(self, projeto):

        self.projeto = projeto
        self.listaAluno = []

    def addAluno(self, nome, cpf):

        novoAluno = aluno(nome,cpf)
        self.listaAluno.append(novoAluno)

    def delAluno(self, cpf):

        alunoRemovido = self.pesquisarAluno(cpf)

        if aluno == None:
            print "Aluno não existe"

        else:
            self.listaAluno.remove(alunoRemovido)


    def pesquisarAluno(self, cpf):

        for i in range(len(self.listaAluno)):

            if self.listaAluno[i].getCpf() == cpf:
                return self.listaAluno[i]

        return None

projeto = raw_input("Digite o nome do projeto")
nome= raw_input("Digite o nome do aluno")
cpf= raw_input("Digite o numero do cpf")
eq = equipe(projeto)
print eq.addAluno(nome,cpf)
