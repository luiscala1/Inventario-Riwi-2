# Inventario-Riwi-2
# 🛒 Inventario RIWI

## 📌 Descripción  
Inventario RIWI es un programa en Python que permite registrar productos ingresando su **nombre, precio y cantidad**.  
El sistema valida los datos y calcula automáticamente el costo total del producto (**precio × cantidad**).  

Además, el programa permite **gestionar múltiples productos**, visualizar el inventario completo y calcular estadísticas generales.

---

## ⚙️ ¿Qué hace el programa?

### 🔹 Menú interactivo
Al ejecutar el programa, aparece un menú con varias opciones:


=== MENÚ PRINCIPAL ===

Agregar producto
Mostrar inventario
Calcular estadísticas
Salir

---

### 🔹 1. Agregar producto
- Solicita el nombre del producto  
  - Solo permite letras  
  - Si es inválido, lo vuelve a pedir  
  - Muestra: `Nombre válido`

- Solicita el precio  
  - Debe ser un número mayor que 0  
  - Valida errores (letras o negativos)

- Solicita la cantidad  
  - Debe ser un número entero positivo  

- Guarda el producto en una lista (inventario)

- Muestra confirmación:

Producto 'Nombre' agregado exitosamente!


---

### 🔹 2. Mostrar inventario
- Muestra todos los productos registrados
- Incluye:
  - Nombre
  - Precio formateado
  - Cantidad

- Si no hay productos:

El inventario está vacío. Agrega productos primero.


---

### 🔹 3. Calcular estadísticas
El programa genera una **factura completa con estadísticas**, incluyendo:

- Lista de todos los productos
- Precio unitario
- Cantidad
- Subtotal por producto
- Total de productos registrados
- Valor total del inventario

Ejemplo:


=== FACTURA FINAL Y ESTADÍSTICAS ===

PRODUCTO PRECIO CANT SUBTOTAL
Arroz $2,000.00 3 $6,000.00
Leche $3,500.00 2 $7,000.00

TOTAL PRODUCTOS: 2
VALOR TOTAL INVENTARIO: $13,000.00


---

### 🔹 4. Salir
Finaliza el programa con un mensaje:

¡Gracias por usar el sistema de inventario!
Hasta pronto!


---

## 🚀 Cómo usar este programa

### 🔧 Requisitos previos
- Tener instalado **Python 3**
- Descargar desde: https://python.org/downloads/

---

## 💻 Ejecución

### 🪟 Windows
1. Descargar `inventario.py`
2. Clic derecho → **Abrir con → Python**
3. ¡Listo!

### 🍎 Mac
1. Clic derecho → **Abrir con → Python 3.x**

### 🐧 Linux
1. Clic derecho → **Abrir con → Python 3**

---

### 💡 Si Python no aparece
- Instalar Python marcando **"Add Python to PATH"**
- O seleccionar manualmente `python.exe`

---

## 🆕 Funcionalidades

- ✅ Menú interactivo
- ✅ Manejo de múltiples productos
- ✅ Visualización del inventario
- ✅ Cálculo de subtotales
- ✅ Cálculo del valor total
- ✅ Conteo de productos
- ✅ Formato tipo factura
- ✅ Validación de datos (try/except)

---

## 👨‍💻 Autor  
**Luis Cala**  
📍 Barranquilla, Atlántico, Colombia  
🌐 RIWI  
🗓 2026
