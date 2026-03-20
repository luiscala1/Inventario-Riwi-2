


inventario = []  

# Función para validar y agregar un producto al inventario
def agregar_producto():
    

    print("\n=== AGREGAR PRODUCTO ===")
    
    
    nombre = ""
    while not nombre.isalpha():
        nombre = input("Ingresa nombre del producto: ").strip()
        if not nombre.isalpha():
            print("Solo se permiten letras")
    print("Nombre válido")
    
    # Validación del precio
    precio = 0
    while True:
        try:
            precio = float(input("Ingresa precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor que 0, intenta nuevamente")
                continue
            break
        except ValueError:
            print("Solo se aceptan números, intenta nuevamente")
    
    # Validación de la cantidad 
    cantidad = 0
    while True:
        try:
            cantidad = int(input("Ingresa cantidad del producto: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0, intenta nuevamente")
                continue
            break
        except ValueError:
            print("Solo se aceptan números enteros, intenta nuevamente")
    
    producto = {
        "nombre": nombre.capitalize(),
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f"\n Producto '{producto['nombre']}' agregado exitosamente!")

def mostrar_inventario():
    
    print("\n=== INVENTARIO ACTUAL ===")
    if not inventario:  # Si la lista está vacía
        print(" El inventario está vacío. Agrega productos primero.")
        return
    
    print("-" * 45)
    for i, producto in enumerate(inventario, 1):
        print(f"{i}. Producto: {producto['nombre']} | "
              f"Precio: ${producto['precio']:,.2f} | "
              f"Cantidad: {producto['cantidad']}")
    print("-" * 45)


def calcular_estadisticas():
    
    if not inventario:
        print("\n No hay productos para calcular estadísticas.")
        return
    
    print("\n=== FACTURA FINAL Y ESTADÍSTICAS ===")
    valor_total = 0
    total_productos = len(inventario)
    
    print("-" * 60)
    print(f"{'PRODUCTO':<15} {'PRECIO':<12} {'CANT':<6} {'SUBTOTAL':<12}")
    print("-" * 60)
    
    # Calcula subtotal por producto y acumulacion total
    for producto in inventario:
        subtotal = producto['precio'] * producto['cantidad']
        valor_total += subtotal
        print(f"{producto['nombre']:<15} "
              f"${producto['precio']:>9,.2f}  "
              f"{producto['cantidad']:<6} "
              f"${subtotal:>10,.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL PRODUCTOS:':<35} {total_productos}")
    print(f"{'VALOR TOTAL INVENTARIO:':<35} ${valor_total:>10,.2f}")
    print("-" * 60)

def main():
    
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        print("-" * 25)
        
        try:
            opcion = int(input("Selecciona una opción (1-4): "))
        except ValueError:
            print(" Opción inválida. Ingresa un número del 1 al 4.")
            continue
        
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_inventario()
        elif opcion == 3:
            calcular_estadisticas()
        elif opcion == 4:
            print("\n ¡Gracias por usar el sistema de inventario!")
            print("Hasta pronto!")
            break
        else:
            print(" Opción inválida. Selecciona 1, 2, 3 o 4.")

# Iniciar el programa
if __name__ == "__main__":
    main()