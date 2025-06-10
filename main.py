import csv

def agregar_rubro(lista, descripcion, unidad, cantidad, precio_unitario):
    rubro = {
        "Descripción": descripcion,
        "Unidad": unidad,
        "Cantidad": float(cantidad),
        "Precio Unitario": float(precio_unitario),
        "Subtotal": float(cantidad) * float(precio_unitario)
    }
    lista.append(rubro)

def guardar_csv(lista, nombre_archivo="presupuesto.csv"):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        campos = ["Descripción", "Unidad", "Cantidad", "Precio Unitario", "Subtotal"]
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista)

def mostrar_presupuesto(lista):
    total = 0
    print(f"{'Descripción':<30} {'Unidad':<10} {'Cantidad':<10} {'P.Unit':<10} {'Subtotal':<10}")
    for rubro in lista:
        print(f"{rubro['Descripción']:<30} {rubro['Unidad']:<10} {rubro['Cantidad']:<10} {rubro['Precio Unitario']:<10} {rubro['Subtotal']:<10}")
        total += rubro["Subtotal"]
    print(f"
TOTAL: ${total:.2f}")

if __name__ == "__main__":
    presupuesto = []
    while True:
        print("\nAgregar nuevo rubro al presupuesto:")
        desc = input("Descripción: ")
        unidad = input("Unidad (m2, m3, etc.): ")
        cant = input("Cantidad: ")
        p_unit = input("Precio unitario: ")
        agregar_rubro(presupuesto, desc, unidad, cant, p_unit)
        continuar = input("¿Deseas agregar otro rubro? (s/n): ").lower()
        if continuar != 's':
            break

    mostrar_presupuesto(presupuesto)
    guardar_csv(presupuesto)
    print("Presupuesto guardado en 'presupuesto.csv'")
