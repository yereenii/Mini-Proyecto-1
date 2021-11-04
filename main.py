from leerArchivo import Comentarios
from FogCalculator.WSCount import WSCount
from halstead import Helstead as hd


class Main:
    nombre_archivo = 'D:\IS\AGO-DIC_2021\CalidadDeSoftware\miniproyecto\CodigoEjemplo.java'
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

    counting=wsc.globalCounting
    sentencecount=wsc.globalSentenceCount
    wordcount=wsc.globalWordCount

    try:
        fog_index_calculated = ((wordcount/sentencecount) + counting)*0.4
        gunning_fog_index = ((wordcount/sentencecount) + 100*(counting/wordcount))*0.4
    except ZeroDivisionError:
        fog_index_calculated = gunning_fog_index = 0
    
    print('Fog Index: {}'.format(fog_index_calculated))
    print('Gunning Fog Index: {}'.format(gunning_fog_index))

    hd.ruta(nombre_archivo)

    f.close