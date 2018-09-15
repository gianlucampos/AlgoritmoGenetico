# Etapas:

# 1- Determinar o número de cronossomos e gerações, taxa de mutação e valor de crossover - OK
# 2- Gerar um nº de população de cronossomo-cronossomo e definir seus genes com          - OK
# valores aleatórios
# 3-Executar etapas 4-7 até que o nº de gerações seja atingido                           - OK
# 4-Avaliar o valor adequado dos cronossomos utilizando a função [a + 2b + 3c + 4d = 30] - OK
# c1[a,b,c,d] => usando a+2b+3c+4d = 30 ?
# 5-Selecionar cronossomos                                                               - OK
# 6-Crossover                                                                            - OK
# 7-Mutação
# 8-Resultado final (melhores cronossomos)

import random

# 1
n_cronossomos = 6
n_geracoes = 4
pc = 0.25  # taxa crossover
pm = 10  # taxa mutacao

# 2
n_populacao = 6  # nº população == nº cronossomos
for inicio in range(n_geracoes):
    cronossomo = []
    fx = []
    fit = []
    total = 0
    i = 0

    print("\n****************************************")
    print("{}ª geração de cronossomos".format(inicio + 1))
    print("****************************************")

    for i in range(n_cronossomos):
        a = random.randint(0, 30)
        b = random.randint(0, 30)
        c = random.randint(0, 30)
        d = random.randint(0, 30)
        cronossomo.insert(i, str(a) + ";" + str(b) + ";" + str(c) + ";" + str(d))

        # 3 Executando etapas 4 a 7

        # 4 Avaliação

        a, b, c, d = cronossomo[i].split(';')
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        fx.insert(i, abs((a + (2 * b) + (3 * c) + (4 * d)) - 30))

        # Fitness

        ft = round((1 / (1 + fx[i])), 4)
        fit.insert(i, ft)
        total = round((ft + total), 4)

    print("Cronossomos:")
    print(cronossomo)
    print("F(x):")
    print(fx)
    print("Fitness:")
    print(fit)
    print("Total:")
    print(total)

    # 5 Calculando Probabilidade (roulette)

    p = []
    for i in range(n_cronossomos):
        p.insert(i, round((fit[i] / total), 4))

    print("Probabilidade P: ")
    print(p)

    ''' Não serve pra nada por isso deixar assim
    # Probabilidade cumulativa 
    c = []
    acumula = 0
    for i in range(n_cronossomos):
        acumula += p[i]
        c.insert(i, round(acumula, 4))
    
    print("Probabilidade acumulativa C:")
    print(c)
    '''
    # 6 Crossover
    print("Crossover:\nValores Aleatórios:")
    # Seleção de cronossomos
    r = []
    cs = []  # cronossomos selecionados possui o indice dos cronossomos
    for i in range(n_cronossomos):
        r.insert(i, round(random.uniform(0, 1), 4))
        print("R[{}]: {}".format(i, r[i]))

        if r[i] < pc:
            cs.insert(i, i)

    # Dúvida, se tivermos apenas menos de 2 cronossomos selecionados, vai p próxima geração ou gera valores novos ?
    if len(cs) <= 1:
        print("Não possui valores suficientes para gerar crossover, Regerar valores \nOU\nPular geração ?")
    else:
        print("Cronossomos selecionados Cs: ")
        print(cs)

    # Determinar posição do crossover
    novo_cronossomo = cronossomo[:]
    if len(cs) > 1:
        print("Cortando a partir do ")
        for i in range(len(cs)):
            va = random.randint(1, 3)
            a, b, c, d = cronossomo[cs[i]].split(";")
            if i == len(cs) - 1:
                a0, b0, c0, d = cronossomo[cs[0]].split(";")
            else:
                a0, b0, c0, d = cronossomo[cs[i + 1]].split(";")
            if va == 1:
                b = b0
                c = c0
            if va == 2:
                c = c0
            novo_cronossomo[cs[i]] = str(a) + ";" + str(b) + ";" + str(c) + ";" + str(d)
            print(str(va) + "º gene do cronossomo {}".format(cs[i]))

        print("Cronossomo após crossover")
        print(novo_cronossomo)

    # 7 Mutação
    print("O nº da população será o mesmo nas próximas gerações ?")
    total_genes = 4 * n_populacao
