class BloomFilter:
    """
    Una implementación simple de un Filtro de Bloom.
    Los filtros de Bloom son estructuras de datos probabilísticas que se utilizan
    para comprobar si un elemento es miembro de un conjunto.
    Pueden ocurrir falsos positivos, pero no falsos negativos.
    """

    def __init__(self, size: int, hash_count: int):
        """
        :param size: El tamaño del array de bits.
        :param hash_count: El número de funciones de hash a utilizar.
        """
        # Escribe tu lógica de inicialización aquí
        pass

    def add(self, item):
        # Escribe la lógica para añadir un item al filtro
        pass

    def __contains__(self, item) -> bool:
        # Escribe la lógica para comprobar si un item está en el filtro
        # Esto permite usar el operador "in" (ej: "manzana" in mi_filtro)
        pass
