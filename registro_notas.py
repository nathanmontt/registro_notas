from reportlab.pdfgen           import canvas
from reportlab.lib.pagesizes    import A4
from reportlab.lib              import colors
from reportlab.platypus         import Table, TableStyle

students_list = []
student_tuple = ()

while True:
    print("SISTEMA DE NOTAS DE ALUNOS")
    menu_options = input("Digite uma das opções:\n1 - Adicionar informações\n2 - Visualizar informações\n3 - Sair\n: ").strip()
    match menu_options:
        case "1":
            while True:
                student_name = input("Nome do aluno: ")
                student_subject = input("Matéria: ")
                student_grade = float(input("Nota: "))

                student_tuple = (student_name, student_subject, student_grade)
                students_list.append(student_tuple)

                continue_option = input("deseja continuar - s para sim, n para não: ")
                if not continue_option.lower() in ("sair", "cancelar", "s"):
                    break

                print()

        case "2":
            # [print(student_name, subject, grade) for student_name, subject, grade in students_list]
            print(f"{'NOME':<10} {'MATÉRIA':<10} {'NOTA':>6}")
            for student_name, subject, grade in students_list:
                print(f"{student_name:<10} {subject:<10} {grade:>6}")
            
        case "3":
            break
        case _:
            print("Opção não encontrada")