from reportlab.pdfgen           import canvas
from reportlab.lib.pagesizes    import A4
from reportlab.lib              import colors
from reportlab.platypus         import Table, TableStyle

students_list = []
student_tuple = ()
subjects = ["Matemática", "Matematica", "Gramática", "Gramatica", "Português", "Portugues",
            "Álgebra", "Algebra", "História", "Historia", "Inglês", "Ingles",  
            "Espanhol", "Artes"]

while True:
    print("SISTEMA DE NOTAS DE ALUNOS")
    menu_options = input("Digite uma das opções:\n1 - Adicionar informações\n2 - Visualizar informações\n3 - Sair\n: ").strip()
    match menu_options:
        case "1":
            while True:
                student_name = input("Nome do aluno: ").capitalize().strip()
                
                while True:
                    student_subject = input("Matéria: ").capitalize().strip()
                    subjetct_repeated = False

                    for each_subject in students_list:
                        if each_subject[1] == student_subject:
                            subjetct_repeated = True
                            break

                    if subjetct_repeated:
                        print("Essa matéria já foi cadastrada. Digite outra.")
                        continue

                    break

                while not student_subject in subjects:
                    student_subject = input("Digite uma matéria válida: ").capitalize().strip()

                student_grade = float(input("Nota: ").strip())
                while student_grade > 10 or student_grade < 0:
                    student_grade = float(input("Digite uma nota válida: "))

                student_tuple = (student_name, student_subject, student_grade)
                students_list.append(student_tuple)

                continue_option = input("Deseja continuar?\n'S' para SAIR\n'N' para continuar ADICIONANDO ALUNO\n: ")
                
                if not continue_option.lower() in ("sair", "cancelar", "s"):
                    break

                print()

        case "2":
            # [print(student_name, subject, grade) for student_name, subject, grade in students_list]
            print(f"{'NOME':^10} | {'MATÉRIA':^10} | {'NOTA':^10} | {'SITUAÇÃO':^10}")
            for student_name, subject, grade in students_list:
                if grade >= 7:
                    result = "Aprovado"
                elif 5 < grade < 6.9:
                    result = "Recuperação"
                else:
                    result = "Reprovado"

                print(f"{student_name:^10} | {subject:^10} | {grade:^10.2f} | {result:^10}")
            
        case "3":
            break
        case _:
            print("Opção não encontrada")