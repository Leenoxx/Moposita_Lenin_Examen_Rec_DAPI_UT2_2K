import csv


countries_dict = {"30":  "Grecia", "33": "Francia", "34": "España", "351": "Portugal",
                  "380": "Ucrania", "39": "Italia", "41": "Suiza", "44": "Reino Unido",
                  "49": "Alemania", "7": "Rusia"}

nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M", "6": "Y", "7": "F",
            "8": "P", "9": "D", "10": "X", "11": "B", "12": "N", "13": "J", "14": "Z", "15": "S",
            "16": "Q", "17": "V", "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}


def check_username(nombre):
    """Función que comprueba que el nombre y apellido estén
    en formato capitalizado, independientemente de que el
    nombre sea simple o compuesto.
    -Parámetros:
        nombre: nombre del usuario del fichero
        apellidos: apellido del usuario del fichero
    -Salida:
        devuelve un str con los datos corregidos
    """
    nombre_nuevo = nombre.title()
    return nombre_nuevo


def check_nif(nif_usuario):
    """Función que realiza una comprobación matemática para
    determinar si el nif introducido corresponde con la letra
    asociada.
    Parámetros:
        -nif_usuario: str que contiene el nif del usuario
        compuesto por 8 números y una letra
    Salida:
        -str con el nif corregido
    """
    resto = int(nif_usuario[0:8]) % 23
    nif_corregido = nif_usuario[0:8] + nif_dict[str(resto)]
    return nif_corregido


def check_phone(num_tlf):
    """Función que chequea e idnetifica si un número de tlf
    está bien escrito y a que país corresponde su prefijo
    Parámetros:
        -num_tlf: str con el número de teléfono completo
    Salida:
        -str con el país al que corresponde el número basándose
        en el diccionario countries_dict.
        -str con el número de teléfono reformateado
        correctamente.
    """
    separar = num_tlf.split(")")
    prefijo = separar[0][1:]
    numero = separar[1].split("-")
    return countries_dict[prefijo], "+" + prefijo + "-" + numero[0] + numero[1]


def calculate_bill(multas_radar, multas_itv, multas_estupefacientes):
    """Función que realiza la suma de la cantidad de multas
    y devuelve el total a pagar por el usuario.
    Parámetros:
        -multas_radar:
        -param multas_ITV:
        -param multas_estupefacientes:
    Salida:
        -variable de tipo int siendo el total a pagar por multas.
    """
    return int(multas_radar) + int(multas_itv) + int(multas_estupefacientes)


def check_DGT(fichero):
    """Función que abre, comprueba y sobreescribe datos de
    un fichero de texto que contiene datos de todas las
    personas pendientes de pago de multas.
    Parámetros:
        -fichero: str con la ruta del fichero a abrir
    Salida:
        -Ninguna ya que sobreescribimos los datos en el mismo fichero
    """
    dict_personas = []
    datos_nuevos = ["Nombre", "Apellidos", "DNI", "Teléfono", "País", "Vehículo", "Total Multas"]
    with open(fichero, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
        for persona in reader:
            dict_personas.append(persona)
    dict_personas.pop(0)
    for usuario in dict_personas:
        usuario[0] = check_username(usuario[0])
        usuario[1] = check_username(usuario[1])
        usuario[2] = check_nif(usuario[2])
        numero = check_phone(usuario[3])[0]
        usuario[3] = check_phone(usuario[3])[1]
        usuario[5] = calculate_bill(usuario[5], usuario[6], usuario[7])
        usuario.pop(6)
        usuario.pop(6)
        usuario.insert(4, numero)
    dict_personas.insert(0, datos_nuevos)
    with open(fichero, encoding='utf-8') as end:
        final = open(fichero, "w", newline="")
        end = csv.writer(final, quotechar=' ', quoting=csv.QUOTE_ALL)
        for linea in dict_personas:
            end.writerow(linea)
