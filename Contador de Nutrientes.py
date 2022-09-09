from Project.interface import *

listaal = ['', 'ARROZ', 'OVO', 'PÃO', 'BANANA', 'Tapioca c/ queijo', 'Barra de ceral', 'Barra de proteína', 'Peito de Frango', 'Purê de batata docê', 'Leite com Nescau', 'Aveia', 'Iogurte', 'Leite Puro', 'Crepioca com frango desfiado', 'Pasta de amendoim']
carboidratos = [0, 0.28, 0.52, 26, 25, 55.2, 16, 12, 0, 0.2766, 0.134, 0.666, 8.4, 0.05, 24.03, 0.2]
proteinas = [0, 0.027, 6, 5, 1.3, 10, 1.3, 10, 32, 0.0129, 0.0335, 0.139, 6.6, 0.033, 18.35, 0.273]
calorias = [0, 1.3, 70, 155, 100, 358, 91, 98, 159, 1.33, 0.775, 3.94, 117, 0.585, 292.05, 6.066]

totalcarbo = totalprot = totalcal = contador = 0


while True:
    alimento = menu(listaal[1:])
    if alimento == 1 or alimento == 9 or alimento == 11:
        g = leiaInt('\033[32mQuantos gramas?: \033[m')
        totalcarbo += g * carboidratos[alimento]
        totalprot += g * proteinas[alimento]
        totalcal += g * calorias[alimento]
        print(f'\033[33mNutrientes com a quantidade de {g}g de {listaal[alimento]} é:\nCarboídratos: {g * carboidratos[alimento]:.2f}G, proteínas: {g * proteinas[alimento]:.2f}G, calorias:{g * calorias[alimento]:.2f}KCL\033[m')

    elif alimento == 10 or alimento == 13:
        ml = leiaInt('\033[32mQuantos mls?: \033[m')
        totalcarbo += ml * carboidratos[alimento]
        totalprot += ml * proteinas[alimento]
        totalcal += ml * calorias[alimento]
        print(f'\033[33mNutrientes com a quantidade de {ml}ml de {listaal[alimento]} é:\nCarboídratos: {ml * carboidratos[alimento]:.2f}G, proteínas: {ml * proteinas[alimento]:.2f}G, calorias:{ml * calorias[alimento]:.2f}KCL\033[m')

    else:
        u = leiaInt('\033[32mQuantas unidades: \033[m')
        totalcarbo += u * carboidratos[alimento]
        totalprot += u * proteinas[alimento]
        totalcal += u * calorias[alimento]
        print(f'\033[33mNutrientes com a quantidade de {u} unidades de {listaal[alimento]} é:\nCarboídratos: {u * carboidratos[alimento]:.2f}G, proteínas: {u * proteinas[alimento]:.2f}G, calorias:{u * calorias[alimento]:.2f}KCL\033[m')
    print()
    resposta = str(input('Quer continuar?[S/N]: '))[0].upper()
    if resposta == 'N':

        break

print(f'\033[32mO total de nutrientes consumidos foi de:\nCaboídratos {totalcarbo:.2f}G\nTotal de proteinas {totalprot:.2f}G\nTotal de calorias {totalcal:.2f}KCL\033[m')
