import csv
import matplotlib.pyplot as plt

class DadosInvalidosError(Exception):
    pass

def carregar_dados(arquivo):

    try:
        with open(arquivo) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            alunos_validos = {}
            erros = []

            for row in reader:
                nome = row[0]
                notas = row[1:]
                notas_convertidas = []
                aluno_valido = True
                for nota in notas:
                    try:
                        nota_convertida = float(nota)
                    except ValueError:
                        aluno_valido = False
                        break

                    if 0 <= nota_convertida <= 10:
                        notas_convertidas.append(nota_convertida)
                    else:
                        aluno_valido = False
                        break

                if aluno_valido:
                    alunos_validos[nome] = notas_convertidas
                else:
                    erros.append(f'Aluno(a): {nome} possui notas inválidas: {nota}')
            if not erros:
                erros.append('Nenhum erro encontrado.')
    except FileNotFoundError:
        print('Arquivo não encontrado')

    return alunos_validos, erros

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
            risco_academico.append(f'Aluno(a) em risco acadêmico: {aluno}')


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

def grafico_desempenho_turma(dados):
    aprovados = sum(1 for alunos in dados.values() if alunos['Situação'] == 'Aprovado')
    reprovados = len(dados) - aprovados

    status = ['Aprovados', 'Reprovados']
    quantidade = [aprovados, reprovados]

    plt.figure('Análise de Desempenho Escolar')

    barras = plt.bar(status, quantidade, color=['#2ecc71', '#e74c3c'])

    plt.ylim(0, len(dados))

    passo = max(1, len(dados) // 5)
    plt.yticks(range(0, len(dados) + 1, passo))

    plt.bar_label(barras, padding=5)

    plt.title(f"Resultado Semestral (Total: {len(dados)} alunos)")
    plt.ylabel("Número de Alunos")

    plt.show()




def main():
    try:
        alunos, erro = carregar_dados('turma_100.csv')
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
    for aluno in alunos_em_risco:
        print(f'{(aluno)}')
    print("\nRelatório de Erros:")
    print("-" * 30)
    for aluno in erro:
        print(f"- {aluno}")
    grafico_desempenho_turma(relatorio_individual)

if __name__ == '__main__':
    main()