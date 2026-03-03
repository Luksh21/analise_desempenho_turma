import csv

class DadosInvalidosError(Exception):
    pass
def carregar_dados(arquivo):
    """Carrega notas de alunos a partir de um arquivo.csv
        Retorna um dicionário no formato {nome_aluno: [notas]}.
    """
    try:
        with open(arquivo) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            try:
                alunos = {row[0]: [float(n) for n in row[1:]] for row in reader}
                return alunos
            except ValueError:
                raise DadosInvalidosError("Arquivo contém valores inválidos.")
    except FileNotFoundError:
            raise FileNotFoundError("Arquivo não encontrado.")

def validacao_notas(dados):

        if not dados:
            raise DadosInvalidosError("Nenhum dado fornecido.")

        for aluno, notas in dados.items():
            if not notas:
                raise DadosInvalidosError(f"{aluno} não possui notas.")

            for nota in notas:
                if nota is None:
                    raise DadosInvalidosError(f"Nota ausente para {aluno}")

                if not isinstance(nota, (int, float)):
                    raise DadosInvalidosError(f"Nota inválida para {aluno}")

                if nota < 0 or nota > 10:
                    raise DadosInvalidosError(f"Nota fora do intervalo para {aluno}")

        return True
def desempenho_individual(dados):
    relatorio = {}

    for aluno , notas in dados.items():
        media = sum(notas) / len(notas)
        maior_nota = max(notas)
        menor_nota = min(notas)
        situacao = 'Aprovado' if media >= 6 else 'Reprovado'
        relatorio[aluno] = {
                'Média' : media,
                'Maior nota' : maior_nota,
                'Menor nota' : menor_nota,
                'Situação' : situacao
        }
    return relatorio

def desempenho_turma(dados):
    if not dados:
        return 0.0, []

    medias_alunos = [dados_alunos["Média"] for dados_alunos in dados.values()]

    media = sum(medias_alunos) / len(medias_alunos)
    risco_academico = []
    for aluno, info in dados.items():
        if info['Situação'] == 'Reprovado':
            risco_academico.append(aluno)


    return media, risco_academico



def porcentagem_aprovacao(dados):
    if not dados:
        return 0.0, 0.0

    aprovados = 0
    reprovados = 0
    for alunos in dados.values():
        if alunos['Situação'] == 'Aprovado':
            aprovados += 1
        else:
            reprovados += 1

    return round(aprovados / len(dados) * 100, 2), round(reprovados / len(dados) * 100, 2)

def main():
    try:
        alunos = carregar_dados('turma_1000.csv')

        validacao_notas(alunos)

        relatorio_individual = desempenho_individual(alunos)

    except (DadosInvalidosError, FileNotFoundError) as erro:
        print("Erro:", erro)
        return

    print('Desempenho Individual')
    print("-" * 24)
    for aluno, dados in relatorio_individual.items():
        print(f"Aluno: {aluno}")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
        print("-" * 24)

    aprovacao_turma, reprovacao_turma = porcentagem_aprovacao(relatorio_individual)
    relatorio_turma, alunos_em_risco = desempenho_turma(relatorio_individual)
    print("\nDesempenho da Turma:")
    print("-" * 24)
    print(f"Média geral da turma: {relatorio_turma:.2f}")
    print(f"Percentual de aprovação: {aprovacao_turma:.2f}%")
    print(f"Percentual de reprovação: {reprovacao_turma:.2f}%")
    print(f'Alunos em risco acadêmico: {','.join(alunos_em_risco)}')
if __name__ == '__main__':
    main()
