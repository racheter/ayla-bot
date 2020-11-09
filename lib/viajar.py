from random import randint, choice

planeta1 = "https://media.discordapp.net/attachments/720684321224261752/753641607865303130/saturno.jpg"
planeta2 = "https://cdn.discordapp.com/attachments/720684321224261752/753641211448918041/jupter.jpg"
planeta3 = "https://cdn.discordapp.com/attachments/743307938499919926/755655391114952764/netuno.png"
planeta4 = "https://cdn.discordapp.com/attachments/720684321224261752/753641731559260170/tita.jpg"
planeta5 = "https://cdn.discordapp.com/attachments/720684321224261752/753640866207236227/venus.jpg"
planeta6 = "https://cdn.discordapp.com/attachments/720684321224261752/753641128955215983/eris.jpg"
planeta7 = "https://cdn.discordapp.com/attachments/720684321224261752/753641092867686480/ceres.jpg"
planeta8 = "https://cdn.discordapp.com/attachments/743307938499919926/755655378934693908/europa.JPG"
planeta9 = "https://cdn.discordapp.com/attachments/743307938499919926/755655390338875483/urano.jpg"
planeta10 = "https://cdn.discordapp.com/attachments/720684321224261752/753641336951013517/merte.jpg"
planeta11 = "https://cdn.discordapp.com/attachments/720684321224261752/753641363190579254/makemake.png"
planeta12 = "https://cdn.discordapp.com/attachments/743307938499919926/755657118148722738/Callisto.jpg"
planeta13 = "https://cdn.discordapp.com/attachments/720684321224261752/753640632139907184/mercurio.jpg"
planeta14 = "https://cdn.discordapp.com/attachments/743307938499919926/755657125778161714/Enceladusstripes_cassini.jpg"
planeta15 = "https://cdn.discordapp.com/attachments/743307938499919926/755657140873592933/PIA18185_Mirandas_Icy_Face.jpg"
planeta16 = "https://cdn.discordapp.com/attachments/743307938499919926/755657131360780338/Phobos_moon_large.jpg"
planeta17 = "https://cdn.discordapp.com/attachments/720684321224261752/753641174493036585/haumea.jpg"
planeta18 = "https://cdn.discordapp.com/attachments/720684321224261752/753641498234454076/plutao.jpg"
planeta19 = "https://cdn.discordapp.com/attachments/720684321224261752/753641241157042227/lua.jpg"
planeta20 = "https://cdn.discordapp.com/attachments/720684321224261752/753641000613839009/terra.jpg"

jupiter = [1, 5]
#3
netuno = [10, 300, 45]
#4
tita = [11, 113, 400, 333]
#5
venus = [12, 33, 55, 120, 340]
#6
eris = [3, 17, 350, 77, 80, 137]
#7
ceres = [4, 14, 44, 114, 334, 224, 240]
#8
europa = [7, 58, 88, 380, 140, 78, 38, 127]
#9
urano = [13, 43, 53, 133, 337, 383, 373, 34, 57, 87]
#10
marte = [18, 20, 30, 40, 50, 60, 70, 90, 100, 200, 223, 22, 56, 66, 74]
#11
makemake = [99, 110, 101, 220, 202, 330, 303, 15, 72, 222, 73, 273, 377, 107, 150, 130, 160, 170, 180, 190]
#12
calisto = [2, 6, 8, 9, 184, 16, 19, 21, 31, 41, 51, 61, 71, 81, 91, 121, 131, 141, 151, 161, 171]
#13
mercurio = [181, 191, 211, 221, 231, 241, 251, 261, 271, 281, 291, 321, 331, 341, 351, 361, 371, 381, 391, 364, 64, 54]
#14
encelado = [23, 24, 25, 26, 27, 28, 29, 32, 39, 35, 36, 37, 42, 46, 47, 48, 49, 52, 65, 75, 59, 62, 63, 67]
#15
miranda = [116, 232, 399, 355, 68, 69, 166, 76, 109, 79, 82, 83, 84, 85, 86, 89, 92, 93, 94, 95, 96, 97, 98, 102, 103]
#16
fobos = [104, 105, 106, 108, 199, 201, 203, 204, 205, 206, 207, 208, 209, 182, 230, 272, 297, 298, 299, 256, 375, 290, 324, 325, 343, 327, 328, 358]
#17
haumea = [301, 302, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 322, 323, 376, 379, 326, 344, 335, 329, 342, 345, 346, 347, 348]
#18
plutao = [112, 115, 117, 118, 119, 123, 124, 125, 260, 265, 266, 267, 268, 269, 270, 132, 134, 135, 136, 138, 139, 173, 174, 175, 176, 177, 178, 179, 390, 392, 393, 394, 395, 396, 397, 398]
#19
lua = [242, 243, 244, 245, 246, 247, 248, 249, 252, 253, 254, 255, 369, 257, 258, 259, 262, 263, 264, 172, 274, 275, 276, 277, 278, 279, 280, 282, 283, 284, 285, 286, 287, 288, 289, 292, 293, 294, 295, 296]
#20
terra = [122, 126, 128, 129, 210, 212, 213, 214, 215, 216, 217, 218, 219, 225, 226, 227, 228, 229, 233, 234, 235, 236, 237, 238, 239, 250, 349, 332, 197, 336, 198, 338, 339, 360, 362, 363, 365, 366, 367, 368, 389, 370, 372, 374]
#21
erro = [142, 143, 144, 145, 146, 147, 148, 149, 152, 153, 154, 155, 156, 157, 158, 159, 162, 163, 164, 165, 167, 168, 169, 189, 352, 353, 354, 356, 357, 378, 359, 382, 183, 384, 385, 386, 387, 388, 185, 186, 187, 188, 192, 193, 194, 195, 196]

def viajante():

    numero = randint(0, 400)

    if numero == 111:

        planeta = ["Saturno", planeta1, "#1", "Lendario"]

        return planeta

    for i in range(len(jupiter)):

        if numero == jupiter[i]:

            planeta = ["Júpiter", planeta2, "#2", "Épico"]

            return planeta

    for i in range(len(netuno)):

        if numero == netuno[i]:

            planeta = ["Netuno", planeta3, "#3", "Épico"]

            return planeta

    for i in range(len(tita)):

        if numero == tita[i]:

            planeta = ["Titã", planeta4, "#4", "Épico"]

            return planeta

    for i in range(len(venus)):

        if numero == venus[i]:

            planeta = ["Vênus", planeta5, "#5", "Épico"]

            return planeta

    for i in range(len(eris)):

        if numero == eris[i]:

            planeta = ["Éris", planeta6, "#6", "Épico"]

            return planeta

    for i in range(len(ceres)):

        if numero == ceres[i]:

            planeta = ["Ceres", planeta7, "#7", "Raro"]

            return planeta

    for i in range(len(europa)):

        if numero == europa[i]:

            planeta = ["Europa", planeta8, "#8", "Raro"]

            return planeta

    for i in range(len(urano)):

        if numero == urano[i]:

            planeta = ["Urano", planeta9, "#9", "Raro"]

            return planeta

    for i in range(len(marte)):

        if numero == marte[i]:

            planeta = ["Marte", planeta10, "#10", "Raro"]

            return planeta

    for i in range(len(makemake)):

        if numero == makemake[i]:

            planeta = ["Makemake", planeta11, "#11", "Raro"]

            return planeta

    for i in range(len(calisto)):

        if numero == calisto[i]:

            planeta = ["Calisto", planeta12, "#12", "Incomun"]

            return planeta

    for i in range(len(mercurio)):

        if numero == mercurio[i]:

            planeta = ["Mercúrio", planeta13, "#13", "Incomun"]

            return planeta

    for i in range(len(encelado)):

        if numero == encelado[i]:

            planeta = ["Encélado", planeta14, "#14", "Incomun"]

            return planeta

    for i in range(len(miranda)):

        if numero == miranda[i]:

            planeta = ["Miranda", planeta15, "#15", "Incomun"]

            return planeta

    for i in range(len(fobos)):

        if numero == fobos[i]:

            planeta = ["Fobos", planeta16, "#16", "Incomun"]

            return planeta

    for i in range(len(haumea)):

        if numero == haumea[i]:

            planeta = ["Haumea", planeta17, "#17", "Comun"]

            return planeta

    for i in range(len(plutao)):

        if numero == plutao[i]:

            planeta = ["Plutão", planeta18, "#18", "Comun"]

            return planeta

    for i in range(len(lua)):

        if numero == lua[i]:

            planeta = ["Lua", planeta19, "#19", "Comun"]

            return planeta

    for i in range(len(terra)):

        if numero == terra[i]:

            planeta = ["terra", planeta20, "#20", "Comun"]

            return planeta

    for i in range(len(erro)):

        if numero == erro[i]:

            planeta = ["Falhou", "null", "null", "null"]

            return planeta
