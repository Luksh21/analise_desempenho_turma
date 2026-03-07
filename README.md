# 📊 Análise de Desempenho de Turma

Projeto desenvolvido em Python para análise de notas de alunos a partir de um arquivo CSV.

O sistema realiza validação de dados, cálculo de métricas individuais e métricas gerais da turma, aplicando boas práticas como separação de responsabilidades e tratamento de exceções.

---

## 🚀 Funcionalidades

- 📂 Leitura de arquivo CSV
- ✅ Validação de dados (valores ausentes, tipo inválido, intervalo 0–10)
- ⚠️ Exception personalizada (`DadosInvalidosError`)
- 📈 Cálculo de média individual
- 📊 Média geral da turma
- 📉 Percentual de aprovação e reprovação
- 🧱 Estrutura modular com funções separadas

---

## 🛠 Tecnologias utilizadas

- Python 3
- Biblioteca padrão `csv`
- Git para versionamento
- Matplotlib

---

## 📁 Estrutura do Projeto

Projeto-desempenho-escolar/

├── main.py
├── turma.csv
├── turma_1000.csv
└── README.md

---

## 🎯 Próximos passos

- Implementar tolerância a falhas (processamento parcial com relatório de inconsistências)
- Evoluir para análise com Pandas
- Implementar geração de relatório em arquivo
- Estruturar a saída de dados referente aos alunos em risco acadêmico

---

## 📌 Objetivo do Projeto

Este projeto foi desenvolvido como prática de:

- Estruturação de código
- Tratamento de exceções
- Validação de dados
- Organização lógica de fluxo

---
