var = 5

try:
    integer_result = int(var)
except ValueError:
    print("not a valid integer")

# ****************************************************
# cronossomo = ["02;21;18;03", "10;04;13;14", "12;05;23;08", "20;05;17;01", "10;04;13;14", "20;01;10;06"]
# novo_cronossomo = cronossomo[:]
# cs = [0, 3, 4]
#
# for i in range(len(cs)):
#     a, b, c, d = cronossomo[cs[i]].split(";")
#     if i == len(cs) - 1:
#         va = 2
#         a0, b0, c0, d = cronossomo[cs[0]].split(";")
#     else:
#         va = 1
#         a0, b0, c0, d = cronossomo[cs[i + 1]].split(";")
#     if va == 1:
#         b = b0
#         c = c0
#     if va == 2:
#         c = c0
#     # b = b if va == 1 else b0 #Por cuá desta forma da errado ?
#     # c = c if va == 2 else c0
#     novo_cronossomo[cs[i]] = str(a) + ";" + str(b) + ";" + str(c) + ";" + str(d)
#     print("Cortando a partir do " + str(va + 1) + "º gene do cronossomo {}".format(cs[i]))
# print("Cronossomo após crossover")
# print(novo_cronossomo)
# print(novo_cronossomo[0])
# print(novo_cronossomo[3])
# print(novo_cronossomo[4])
# *************************************************************
# Como eu achava que era
# novo_cronossomo = cronossomo[:]
# if len(cs) > 1:
#     print("Cortando gene(s): ")
#     for i in range(len(cs)):
#         va = random.randint(0, 2)
#         a, b, c, d = cronossomo[cs[i]].split(";")
#         if i == len(cs) - 1:
#             a0, b0, c0, d0 = cronossomo[cs[0]].split(";")
#         else:
#             a0, b0, c0, d0 = cronossomo[cs[i + 1]].split(";")
#         a = a if va == 0 else a0
#         b = b if va == 1 else b0
#         c = c if va == 2 else c0
#         d = d if va == 3 else d0
#         novo_cronossomo[cs[i]] = str(a) + ";" + str(b) + ";" + str(c) + ";" + str(d)
#         print(str(va) + "º gene do cronossomo {}".format(cs[i]))
#
#     print("Cronossomo após crossover")
#     print(novo_cronossomo)