# Importar pacotes

import datetime


# 1. Definição das classes e métodos

# Classe Pessoa
class Pessoa:
    def __init__(self, codigo: int, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str):
        self.__codigo = codigo
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__sexo = sexo
        self.__email = email
        self.__telefone = telefone

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_rg(self):
        return self.__rg

    def set_rg(self, rg):
        self.__rg = rg

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

# Classe Paciente


class Paciente(Pessoa):
    def __init__(self, codigo: int, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, plano: bool, convenio: str):
        super().__init__(codigo, nome, cpf, rg, sexo, email, telefone)
        self.__plano = plano
        self.__convenio = convenio

    def get_plano(self):
        return self.__plano

    def set_plano(self, plano):
        self.__plano = plano

    def get_convenio(self):
        return self.__convenio

    def set_convenio(self, convenio):
        self.__convenio = convenio


# Classe Funcionário


class Funcionario(Pessoa):
    def __init__(self, codigo: int, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, salario: float, horarioEntrada: str, horarioSaida: str):
        super().__init__(codigo, nome, cpf, rg, sexo, email, telefone)
        self.__salario = salario
        self.__horarioEntrada = horarioEntrada
        self.__horarioSaida = horarioSaida

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def get_horarioEntrada(self):
        return self.__horarioEntrada

    def set_horarioEntrada(self, horarioEntrada):
        self.__horarioEntrada = horarioEntrada

    def get_horarioSaida(self):
        return self.__horarioSaida

    def set_horarioSaida(self, horarioSaida):
        self.__horarioSaida = horarioSaida

# Classe Pagamento


class Pagamento(Funcionario):
    def __init__(self, dataPagamento: datetime, valorPagamento: float, codigo: int, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, salario: float, horarioEntrada: str, horarioSaida: str):
        super().__init__(codigo, nome, cpf, rg, sexo, email, telefone, salario, horarioEntrada, horarioSaida)
        self.__dataPagamento = dataPagamento
        self.__valorPagamento = valorPagamento

    def get_dataPagamento(self):
        return self.__dataPagamento

    def set_dataPagamento(self, dataPagamento):
        self.__dataPagamento = dataPagamento

    def get_valorPagamento(self):
        return self.__valorPagamento

    def set_valorPagamento(self, valorPagamento):
        self.__valorPagamento = valorPagamento


# Classe Médico


class Medico(Funcionario):
    def __init__(self, codigo: int, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, salario: float, horarioEntrada: str, horarioSaida: str, crm: str, valorConsulta: float, especialidades: list):
        super().__init__(codigo, nome, cpf, rg, sexo, email, telefone, salario, horarioEntrada, horarioSaida)
        self.__crm = crm
        self.__valorConsulta = valorConsulta
        self.__especialidades = especialidades

    def get_crm(self):
        return self.__crm

    def set_crm(self, crm):
        self.__crm = crm

    def get_valorConsulta(self):
        return self.__valorConsulta

    def set_valorConsulta(self, valorConsulta):
        self.__valorConsulta = valorConsulta

    def get_especialidades(self):
        return self.__especialidades

    def set_especialidades(self, especialidades):
        self.__especialidades = especialidades


# Classe Especialidades Médica

class Especialidades:
    def __init__(self, codEspecialidade: int, nome: str, descricao: str):
        self.codEspecialidade = codEspecialidade
        self.nome = nome
        self.descricao = descricao


# Classe Prescrição


class Prescricao:
    def __init__(self, codPrescricao: int, dataPrescricao: datetime, exames: list, medicamentos: list):
        self.__codPrescricao = codPrescricao
        self.__dataPrescricao = dataPrescricao
        self.__exames = exames
        self.__medicamentos = medicamentos

    def get_codPrescricao(self):
        return self.__codPrescricao

    def set_codPrescricao(self, codPrescricao):
        self.__codPrescricao = codPrescricao

    def get_dataPrescricao(self):
        return self.__dataPrescricao

    def set_dataPrescricao(self, dataPrescricao):
        self.__dataPrescricao = dataPrescricao

    def get_exames(self):
        return self.__exames

    def set_exames(self, exames):
        self.__exames = exames

    def get_medicamentos(self):
        return self.__medicamentos

    def set_medicamentos(self, medicamentos):
        self.__medicamentos = medicamentos


# Classe Consulta

class Consulta(Medico, Paciente, Prescricao):
    def __init__(self, codigo: int, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, salario: float, horarioEntrada: str, horarioSaida: str, crm: str, valorConsulta: float, especialidades: list, plano: bool, convenio: str, dataHorario: datetime, codPrescricao: int, dataPrescricao: datetime, exames: list, medicamentos: list):
        Medico.__init__(self, codigo, nome, cpf, rg, sexo, email, telefone, salario, horarioEntrada, horarioSaida, crm, valorConsulta, especialidades)
        Paciente.__init__(self, codigo, nome, cpf, rg, sexo, email, telefone, plano, convenio)
        Prescricao.__init__(self, codPrescricao, dataPrescricao, exames, medicamentos)
        self.__dataHorario = dataHorario

    def get_dataHorario(self):
        return self.__dataHorario

    def set_dataHorario(self, dataHorario):
        self.__dataHorario = dataHorario

# Classe Cobrança Consulta


class Cobranca(Consulta):
    def __init__(self, dataCobranca: datetime, valorTotal: float, codigo: int, nome: str, cpf: str, rg: str, sexo: str, email: str, telefone: str, salario: float, horarioEntrada: str, horarioSaida: str, crm: str, valorConsulta: float, especialidades: list, plano: bool, convenio: str, dataHorario: datetime, codPrescricao: int, dataPrescricao: datetime, exames: list, medicamentos: list):
        super().__init__(codigo, nome, cpf, rg, sexo, email, telefone, salario, horarioEntrada, horarioSaida, crm, valorConsulta, especialidades, plano, convenio, dataHorario, codPrescricao, dataPrescricao, exames, medicamentos)
        self.__dataCobranca = dataCobranca
        self.__valorTotal = valorTotal

    def get_dataCobranca(self):
        return self.__dataCobranca

    def set_dataCobranca(self, dataCobranca):
        self.__dataCobranca = dataCobranca

    def get_valorTotal(self):
        return self.__valorTotal

    def set_valorTotal(self, valorTotal):
        self.__valorTotal = valorTotal


# 2. Instanciação de objetos


## Pessoa

Pessoa1 = Pessoa(1,'Maria','124.456.789-10', '12.445.678-9','F','maria@gmaillcom','44999999999')
Pessoa2 = Pessoa(2,'João','124.456.789-11', '02.445.678-0','M','joao@gmaillcom','44988888888')
Pessoa3 = Pessoa(4,'Ana','111.456.789-10', '22.445.678-9','F','ana@gmaillcom','449977777777')
Pessoa4 = Pessoa(4,'José','244.456.789-11', '44.445.678-0','M','jose@gmaillcom','4496666666')

## Funcionario

Funcionario1 = Funcionario(Pessoa1.get_codigo(), Pessoa1.get_nome(), Pessoa1.get_cpf(), Pessoa1.get_rg(), Pessoa1.get_sexo(), Pessoa1.get_email(), Pessoa1.get_telefone(), 5500.0, '08:00', '17:00')
Funcionario2 = Funcionario(Pessoa2.get_codigo(), Pessoa2.get_nome(), Pessoa2.get_cpf(), Pessoa2.get_rg(), Pessoa2.get_sexo(), Pessoa2.get_email(), Pessoa2.get_telefone(), 4000.0, '09:00', '18:00')


## Paciente

Paciente1 = Paciente(Pessoa2.get_codigo(), Pessoa2.get_nome(), Pessoa2.get_cpf(), Pessoa2.get_rg(), Pessoa2.get_sexo(), Pessoa2.get_email(), Pessoa2.get_telefone(),True,'Unimed')
Paciente2= Paciente(Pessoa4.get_codigo(), Pessoa4.get_nome(), Pessoa4.get_cpf(), Pessoa4.get_rg(), Pessoa4.get_sexo(), Pessoa4.get_email(), Pessoa4.get_telefone(),True,'FUPS')


## Médico

Medico1 = Medico(Funcionario1.get_codigo(),Funcionario1.get_nome(),Funcionario1.get_cpf(),Funcionario1.get_rg(),Funcionario1.get_sexo(),Funcionario1.get_email(),Funcionario1.get_telefone(),Funcionario1.get_salario(),Funcionario1.get_horarioEntrada(),Funcionario1.get_horarioSaida(),'23.410-3',300,['Cardiologia','Radiologia'])
Medico2 = Medico(Funcionario2.get_codigo(),Funcionario2.get_nome(),Funcionario2.get_cpf(),Funcionario2.get_rg(),Funcionario2.get_sexo(),Funcionario2.get_email(),Funcionario2.get_telefone(),Funcionario2.get_salario(),Funcionario2.get_horarioEntrada(),Funcionario2.get_horarioSaida(),'55.620-1',400,['Dermatologia','Cirurgia'])

## Pagamento

Pagamento1 = Pagamento('05/10/2023',5500, Funcionario1.get_codigo(),Funcionario1.get_nome(),Funcionario1.get_cpf(),Funcionario1.get_rg(),Funcionario1.get_sexo(),Funcionario1.get_email(),Funcionario1.get_telefone(),Funcionario1.get_salario(),Funcionario1.get_horarioEntrada(),Funcionario1.get_horarioSaida())
Pagamento2 = Pagamento('05/11/2023',5500, Funcionario1.get_codigo(),Funcionario1.get_nome(),Funcionario1.get_cpf(),Funcionario1.get_rg(),Funcionario1.get_sexo(),Funcionario1.get_email(),Funcionario1.get_telefone(),Funcionario1.get_salario(),Funcionario1.get_horarioEntrada(),Funcionario1.get_horarioSaida())


## Prescrição

Prescricao1 = Prescricao(1,'10/10/2023',['Hemograma', 'Vitamina D', "Glicemia"], ['Dipirona', 'Ibuprofeno'])
Prescricao2 = Prescricao(2,'15/06/2023',['Hemograma', 'Vitamina B12', "Glicemia"], ['Dorflex', 'Ibuprofeno'])


## Consulta


Consulta1 = (Paciente1, Medico1,datetime.time,Prescricao1)
Consulta2 = (Paciente1, Medico2,datetime.time,Prescricao1)


## Cobranca

Cobranca1 = ('05/11/2023',1700,Consulta1)
Cobranca2 = ('05/11/2023',1200,Consulta2)

## Especialidade

Especialidade1 = Especialidades(1,'Cardiologia', 'Cardiologia é a especialidade médica que se ocupa do diagnóstico e tratamento das doenças que acometem o coração bem como os outros componentes do sistema circulatório. ')
Especialidade2 = Especialidades(2,'Dermatologia','Dermatologia é a especialidade médica que se ocupa do diagnóstico e tratamento clínico-cirúrgico das enfermidades relacionados à pele e aos anexos cutâneos.')





