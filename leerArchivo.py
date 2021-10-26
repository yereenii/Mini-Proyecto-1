class LeerArchivos:
    lineas = []

    with open('CodigoEjemplo.java','r') as f:
        mensaje = f.readlines()
        for linea in mensaje:
            lineas.append(linea.strip('\n'))

    #print(lineas)
    for n in lineas:
        print(n)

    f.close