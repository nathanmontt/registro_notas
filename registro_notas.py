from reportlab.pdfgen           import canvas
from reportlab.lib.pagesizes    import A4
from reportlab.lib              import colors
from reportlab.platypus         import Table, TableStyle

students_list = []
student_tuple = ()

while True:
    menu_options = input("digite\n1 pra adicionar 2 pra mostrar e 3 pra sair: ").strip()
    match menu_options:
        case "1":
            while True:
                student_name = input("nome do aluno: ")
                student_subject = input("nome da materia: ")
                student_grade = float(input("nota: "))


                continue_option = input("deseja continuar - s para sim, n para não: ")
                if not continue_option.lower() in ("sair", "cancelar", "s"):
                    break

                student_tuple = (student_name, student_subject, student_grade)
                students_list.append(student_tuple)
        case "2":
            [print(student_name, subject, grade) for student_name, subject, grade in students_list]
            # for student_name, subject, grade in students_list+1:
            
        case "3":
            break
        case _:
            print("Opção não encontrada")