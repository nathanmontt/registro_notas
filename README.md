# Registro de Notas de Alunos (CLI)

Um programa de terminal desenvolvido em Python para gerenciar o histórico escolar. O sistema permite cadastrar alunos, atribuir notas por matérias e visualizar automaticamente a situação de aprovação de cada estudante.

## Funcionalidades Atuais

- **Cadastro de Alunos e Notas:** O usuário pode inserir o nome do aluno, a matéria e a nota final.
- **Validação de Dados Rigorosa:** O sistema aceita apenas matérias cadastradas no sistema e limita as notas a um intervalo válido.
- **Estruturação com Tuplas:** Os dados de cada registro são empacotados em uma tupla `(nome, materia, nota)`, garantindo que as informações inseridas não sejam alteradas acidentalmente.
- **Boletim Interativo:** Exibição dos dados em formato de tabela diretamente no terminal, calculando automaticamente se o aluno foi *Aprovado* (>= 7), ficou em *Recuperação* (5 a 6.9) ou foi *Reprovado* (< 5).

## *Feats* Futuras (Em breve)

- [x] **Geração de Boletim em PDF:** Exportar a tabela de notas dos alunos em formato PDF utilizando a biblioteca `reportlab`.
- [ ] **Edição de *input*:** Caso o usuário tenha digitado um nome errado, uma nota errada, que a edição daquele elemento seja feita.

## Pré-requisitos

Para rodar este projeto, você precisa ter o **Python 3.10 ou superior** instalado no seu computador, pois o código utiliza a estrutura moderna de controle de fluxo `match/case`.

## Como clonar e executar para uso próprio

Se você quiser testar este projeto na sua máquina, siga os passos abaixo:

1. Abra o seu terminal (ou Git Bash).
2. Clone este repositório executando o comando:
   ```bash
   git clone https://github.com/nathanmontt/registro_notas.git