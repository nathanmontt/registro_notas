from reportlab.pdfgen           import canvas
from reportlab.lib.pagesizes    import A4
from reportlab.lib              import colors
from reportlab.platypus         import Table, TableStyle

students_list = []

while True:
    menu_options = input("digite\n1 pra adicionar 2 pra remover e 3 pra sair").strip()
    match menu_options:
        case "1":
            break
        case "2":
            break
        case "3":
            break
        case _:
            print("Opção não encontrada")