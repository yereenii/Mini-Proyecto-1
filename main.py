from leerArchivo import Comentarios
from FogCalculator.WSCount import WSCount


class Main:
    nombre_archivo = 'leerArchivo.py'
    lineas = []
    with open(nombre_archivo,'r') as f:
        mensaje = f.readlines()
        for linea in mensaje:
            lineas.append(linea.strip('\n'))
    #se manda llamar para obtener densidad de comentarios.
    c = Comentarios()
    print('densidad de comentarios: {}'.format(c.obtener_densidad_comentarios(lineas)))
    wsc = WSCount()
    wsc.get_wscount(nombre_archivo)

    f.close