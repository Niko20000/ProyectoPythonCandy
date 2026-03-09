def calcular_precio_dulceria():
    
    inventario = {
        "bombones": {"precio": 12000, "cantidad": 100},
        "chocolates": {"precio": 15000, "cantidad": 100},
        "papas": {"precio": 20000, "cantidad": 100}
    }

    total_compra = 0
    
    while True:
        print("\n---------------- Menú de Dulcería ----------------")
    
        for producto, datos in inventario.items():
            print(f"- {producto.capitalize()}: ${datos['precio']:,} (Stock: {datos['cantidad']})")
        
        print(" Salir (Escribe 'salir' para terminar y pagar)")
        

        eleccion = input("\n¿Qué producto desea comprar?: ").lower().strip()

        if eleccion == "salir":
            break

        if eleccion in inventario:
            try:
                cantidad_pedida = int(input(f"¿Cuántas unidades de {eleccion} llevarás?: "))
                
                stock_actual = inventario[eleccion]["cantidad"]
                precio_unitario = inventario[eleccion]["precio"]

                if cantidad_pedida <= stock_actual:
                    subtotal = cantidad_pedida * precio_unitario
                    total_compra += subtotal
                    
      
                    inventario[eleccion]["cantidad"] -= cantidad_pedida
                    
                    print(f" Agregado: {cantidad_pedida} {eleccion} por ${subtotal:,}")
                else:
                    print(f" No hay suficiente stock. Solo quedan {stock_actual}.")
            
            except ValueError:
                print(" Error: Ingresa un número válido para la cantidad.")
        else:
            print(" Ese producto no existe en nuestra tienda. Intenta de nuevo.")

    print("\n" + "=" * 30)
    print(f"RESUMEN DE COMPRA")
    print(f"TOTAL A PAGAR: ${total_compra:,}")
    print("=" * 30 + "\n¡Gracias por su compra!")

calcular_precio_dulceria()