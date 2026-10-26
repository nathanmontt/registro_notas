from reportlab.pdfgen           import canvas
from reportlab.lib.pagesizes    import A4
from reportlab.lib              import colors
from reportlab.platypus         import Table, TableStyle
from time                       import sleep

def generate_pdf():
    if not students_list:
        print("Não há informações para gerar o PDF.")
        return

    pdf = canvas.Canvas("registro_notas.pdf", pagesize=A4)
    pdf.setTitle("Registro de notas")

    pdf.setFontSize(18)
    pdf.drawCentredString(300, 800, "REGISTRO DE NOTAS")

    table_data = [["Nome", "Matéria", "Nota", "Situação"]]

    for student_name, subject, grade in students_list:
        if grade >= 7:
            result = "Aprovado"
        elif grade >= 5:
            result = "Recuperação"
        else:
            result = "Reprovado"

        table_data.append([
            student_name,
            subject,
            f"{grade:.2f}",
            result
        ])

    students_table = Table(
        table_data,
        colWidths=[150, 150, 70, 100]
    )

    students_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (2, 1), (2, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    table_width, table_height = students_table.wrapOn(pdf, 0, 0)
    students_table.drawOn(pdf, 40, 740 - table_height)

    pdf.save()
    print("Criando pdf", end="")
    for i in range(5):
        sleep(.4)
        print(".", end="")

    print("PDF criado: registro_notas.pdf")
    print()

students_list = []
student_tuple = ()
subjects = ["Matemática", "Matematica", "Gramática", "Gramatica", "Português", "Portugues",
            "Álgebra", "Algebra", "História", "Historia", "Inglês", "Ingles",  
            "Espanhol", "Artes"]

while True:
    print("SISTEMA DE NOTAS DE ALUNOS")
    menu_options = input(
        "Digite uma das opções:\n"
        "1 - Adicionar informações\n"
        "2 - Visualizar informações\n"
        "3 - Gerar .pdf\n"
        "4 - Sair\n"
        ": "
    ).strip()

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
            print()
            
        case "3":
            generate_pdf()

        case "4":
            break

        case _:
            print("Opção não encontrada")