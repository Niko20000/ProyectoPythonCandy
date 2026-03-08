def calcular_precio_dulceria():
    
    inventario = {
        "bombones": {"precio": 12000, "paquete": 12 "cantidad" :100},
        "chocolates": {"precio": 15000, "paquete": 30 "cantidad" :100},
        "papas": {"precio": 20000, "paquete": 12 "cantidad" :100}
    }

    print("=== Calculadora de Dulcería ===")
    total_compra = 0

    for producto, datos in inventario.items():
        precio = datos["precio"]
        stock = datos["stock"]

        print(f"\nProducto: {producto.capitalize()}")
        print(f"Precio: ${precio:,}")
        print(f"Stock disponible: {stock}")

        cantidad = int(input("¿Cuántas unidades desea comprar? "))

        subtotal = cantidad * precio
        total_compra += subtotal

        print(f"Subtotal de {producto}: ${subtotal:,}")

    print("\n" + "-" * 30)
    print(f"TOTAL A PAGAR: ${total_compra:,}")
    print("-" * 30)


calcular_precio_dulceria()