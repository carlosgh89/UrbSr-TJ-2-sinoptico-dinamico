import ghpythonlib.treehelpers as th

root_path = camino
# Unir la ruta de la carpeta raíz con el nombre del archivo
file_path = os.path.join(root_path, 'objetos.json')

class Objeto:
    def __init__(self):
        self.material = random.choice(['PET','PEAD','ALUMINIO','ACERO','P/C','PP','BRIK','FILM','MOR'])
        self.densidad_relativa = round(random.uniform(0.1, max_densidad), 4)
        self.masa = round(random.uniform(0.1, max_masa), 3)  # Genera una masa aleatoria entre 0.1 y 0.6
        self.humedad = round(random.uniform(0.0, 0.6), 1)
        # Genera valores aleatorios para la matriz de propiedades geométricas
        self.BoolRodante = random.choice([True, False])
        self.dimX = round(random.uniform(0.01, 1), 2)
        self.dimY = round(random.uniform(0.01, 0.5), 2)
        self.dimZ = round(random.uniform(0.01, 0.4), 2)
        #self.timestamp = time.time()
        #creamos método que averigua el maximo valor entre dimX, dimY y dimZ
        self.maxDim = max(self.dimX, self.dimY, self.dimZ)
        #creamos método que averigua volumen
        #self.volumen = self.densidad_relativa*self.masa
    def to_json(self):
        return json.dumps(self.__dict__)

# Lista para almacenar los objetos
objetos = []

# Sumatoria de masa
masa_total = 0
salidaAlimentador=[]

# Generar objetos hasta alcanzar una masa total de 100
while masa_total < m_a_simular:
    objeto = Objeto()
    objetos.append(objeto.to_json())
    salidaAlimentador.append(objeto)
    masa_total += objeto.masa

# Guardar la lista de objetos JSON en un archivo
with open(file_path, 'w') as archivo_json:
    json.dump(objetos, archivo_json)

#def lista_a_arbol(lista):
    #crear lista de listas
    #lista_listas = [list(obj.__dict__.values()) for obj in lista]
    # Convertir la lista de listas en un árbol
    #return th.list_to_tree(lista_listas, source=[0])

#crea una version de la funcion lista_a_arbol que especifique el orden de claves de diccionario de los objetos. que serán los siguienetes: dimY,densidad_relativa,dimZ,maxDim,dimX,BoolRodante,material,masa,humedad
def lista_a_arbol(lista):
    #crear lista de listas
    lista_listas = [[obj.dimY,obj.densidad_relativa,obj.dimZ,obj.maxDim,obj.dimX,obj.BoolRodante,obj.material,obj.masa,obj.humedad] for obj in lista]
    # Convertir la lista de listas en un árbol
    return th.list_to_tree(lista_listas, source=[0])

b=lista_a_arbol(salidaAlimentador)

# Imprimir la masa total y el número de objetos generados
print('Masa total acumulada: ',{masa_total})
print('Número de objetos generados: ',{len(objetos)})
n=len(objetos)