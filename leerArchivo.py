

class Comentarios:
    _tipo_comentario1 = '#'
    _tipo_comentario2 = '\'\'\''
    _numero_lineas_codigo = 0
    _numero_comentarios_codigo = 0

    def obtener_densidad_comentarios(self, lineas):
        es_comentario_multiple = False
        for index in range(len(lineas)):
            linea = lineas[index].lstrip()
            #si la linea contiene caracteres entra
            if len(linea) > 0:
                if not es_comentario_multiple:
                    #si empieza con # es comentario
                    if linea.startswith(self._tipo_comentario1): 
                        self._numero_comentarios_codigo += 1
                    # si empieza con''' es comentario
                    elif linea.startswith(self._tipo_comentario2): 
                        self._numero_comentarios_codigo += 1
                        long = len(linea)
                        # la logitud de la linea es <= a 3 por logica no cerro el comentario y se vuelve comentario multiple
                        if  long <= 3: 
                            es_comentario_multiple = True
                        if not linea.endswith(self._tipo_comentario2) and long > 3:
                            es_comentario_multiple = True
                    #Es linea Codigo
                    else:
                       self._numero_lineas_codigo += 1
                elif es_comentario_multiple and linea.endswith(self._tipo_comentario2):
                    es_comentario_multiple = False
        if self._numero_comentarios_codigo < 1 or self._numero_lineas_codigo < 1:
            return 'Faltan comentarios o Codigo'
        else:
            return self._numero_comentarios_codigo / self._numero_lineas_codigo  
