#Cadastro de Alunos
#Programa que recebe um conjuto de operações a ser realizado com alunos e mostra as operaçoes realizadas
#Maicon Gabriel de Oliveira, ra 221329

class EmailInvalido(Exception):
    pass

class SenhaFraca(Exception):
    pass

class RAInvalido(Exception):
    pass

class Repositorio:

    def __init__(self):
        self.alunos = []
        self.busca = []

    #Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        k = self.BuscaExiste(aluno.ra,False)        #chama função que verifica se o aluno ja existe
        self.VerificaSenha(aluno.senha)
        self.VerificaEmail(aluno.email)
        #Falta 2 exceções
        self.alunos.append(aluno)       #Armazena instancia na lista
        self.busca.append(aluno.ra)     #Armazena ra correspondente a instancia em outra lista

    def VerificaSenha(self,senha):
        #print("senha recebida: ",senha)
        import re
        if len(senha) < 8:                      #Compara se tem o tamanho minimo de 8 caracteres
            raise SenhaFraca                    #Chama excessao

        s = re.compile(r'[A-Z]')     #Busca por letras maiusculas
        s = s.findall(senha)
        #print("maiuscula", s)
        if s == []:
            raise SenhaFraca  # Chama excessao

        s = re.compile(r'[a-z]')     #Busca por letras minusculas
        s = s.findall(senha)
        #print("minuscula",s)
        if len(s) < 2:      #Verifica se ha pelo menos duas letras minusculas
            raise SenhaFraca  # Chama excessao

        s = re.compile(r'\d')  # Busca por numeros
        s = s.findall(senha)
        #print("numeros:",s)
        if len(s) < 2:  # Verifica se ha pelo menos dois numeros
            raise SenhaFraca  # Chama excessao

        s = re.compile(r'[!]|[@]|[#]|[$]|[&]|[*]')#Busca por um caractere especial do tipo !@#$& ou *
        s = s.findall(senha)
        #print("especial:",s)
        if s == []:
            raise SenhaFraca  # Chama excessao


    def VerificaEmail(self,email):
        #print(email)
        import re
        e = re.compile(r'.*@\w+\.\w+')     #Verifica se formato do email e valido
        f = e.search(email)
        f = f.group(0)
        #print("formato:",f)
        if f is None:
            raise EmailInvalido

        #Verifica usuário
        e = re.compile(r'.*\@')  #Adiquire o usuario
        f = e.search(email)
        f = f.group(0)
        #print("usuario:",f)
        e = re.compile(r'\W+')  # Procura por caracteres nao alfanumericos
        g = e.findall(f)
        #g = g.group(0)
        #print("caracteres especiais:",g)
        aux = 0
        arroba = True
        for i in g:
            if i == "." or i == "+" or i == "-":        #Testa se nao-alfanumericos estao no formato permitido
                aux += 1
            if arroba and i == "@":
                aux += 1
                arroba = False
        #print("quantidade de caracteres permitidos", aux)
        if len(g) != aux:       #Compara se a quantidade de alfanumericos é igual a quantidade de caracteres permitidos
            raise EmailInvalido

        #Verifica Servidor
        e = re.compile(r'\@\w+')   #Adiquire o servidor
        f = e.search(email)
        f = f.group(0)
        #print("servidor:",f)
        e = re.compile(r'\W+')   #Verifica se servidor é composto apenas por alfanumericos
        g = e.findall(f)
        g = g.remove("@")
        #print("alfanumericos:",g)
        if g is not None:
            raise EmailInvalido

        #Verifica Dominio
        e = re.compile(r'\@\w+\.\w+')  # Adiquire o servidor e o dominio
        f = e.findall(email)
        e = re.compile(r'\.\w+')  # Adiquire so o dominio
        f = e.findall(f[0])
        f = f[0]
        #print("dominio:",f)
        if len(f) > 5 or len(f) < 3:      #Verifica se dominio tem tamanho entre 2 e 4
            raise EmailInvalido
        e = re.compile(r'\W+|\d|\_')  #Verifica se são somente letras
        g = e.findall(f)
        #print("especiais:",g)
        if g is not None:
            if g[0] != ".":
                raise EmailInvalido


    def BuscaExiste(self,aux,reverso):
        '''Busca se aluno ja esta cadastrado, se reverso=False, lança exceção caso ele existir, se reverso=True lança exceção caso ele nao existir'''
        k = self.busca.index(aux) if aux in self.busca else -1  # Busca se aluno ja esta na lista e retorna -1 caso nao esteja
        if k != -1 and not reverso:  # Caso aluno esteja na lista
            raise RAInvalido  # Lança exceção
        if k == -1 and reverso:  # Caso aluno não esteja na lista
            raise RAInvalido  # Lança exceção
        return k

    #Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra
    def alterar(self, aluno):
        k = self.BuscaExiste(aluno.ra, True)  # chama função que verifica se o aluno ja existe
        self.VerificaSenha(aluno.senha)
        self.VerificaEmail(aluno.email)
        self.alunos[k] = aluno
        self.busca[k] = aluno.ra

    #Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
    def achaAluno(self, ra):
        try:
            k = self.busca.index(ra)    #Busca na lista de RAs se o mesmo existe, se sim retorna sua posição, senao -1
        except ValueError:
            raise RAInvalido
        return self.alunos[k]       #Retorna a posição da memoria segundo alunos[ra]

    #Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
    def remover(self, ra):
        k = self.BuscaExiste(ra, True)  # chama função que verifica se o aluno ja existe
        self.alunos.remove(self.alunos[k])
        self.busca.remove(self.busca[k])
        return ra

    #Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
        self.__init__()