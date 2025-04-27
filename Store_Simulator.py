#Proyecto1 : Store Simulator -Shopping Cart

WAREHOUSE = [
        {
            "code": "A001",
            "name": "Pan" , 
            "prize": 1.50
        },

        {
            "code": "B203",
            "name": "Leche",
            "prize": 3.80
        }

    ]

SHOPPING_CART = []

def show_menu():

    print("""
        Bienvenido a la Tienda Virtual 
        ¿Que deseas hacer?
        
        1. Ver catálogo
        2. Agregar producto al carrito
        3. Eliminar producto del carrito
        4. Vaciar carrito
        5. Mostrar carrito
        6. Finalizar compra
        7. Salir
        """)


def show_catalog():

    for product in WAREHOUSE:
        print(f"Código: {product['code']:<8}|  Producto:{product['name']:<7}|  Precio:{product['prize']:.2f} ")

def add_product_to_cart(code_product):
    
    for product in WAREHOUSE:
        if product['code'] == code_product:
            try:
                cantidad = int(input("Cantidad: "))
                if cantidad <=0:
                    print("Ingrese una cantidad válidad")
            except ValueError: 
                print("Ingrese un número válido")
                return


            for items in SHOPPING_CART:
                if items['code'] == product['code'] :
                    items['quantity'] +=cantidad
                    print(f"✔ Producto agregado al carrito.")
                    return

            SHOPPING_CART.append({
                "code" : product['code'],
                "name" : product['name'],
                "prize": product['prize'],
                "quantity" : cantidad
            })
            print("✔ Producto agregado al carrito.")
            return

    print("Producto no encontrado")

def remove_cart(product_delete):

    for product in SHOPPING_CART:
        if product["code"] == product_delete:
            SHOPPING_CART.remove(product)
            print(f"✔ Producto eliminado del carrito.")
            break

    return 

def empty_cart():
    SHOPPING_CART.clear()
    print("El carrito esta vacio")

def show_cart():

    if len(SHOPPING_CART)  == 0:
        print("El carrito esta vacio")
    else:
        print("Tu carrito: ")
        total = 0
        for product in SHOPPING_CART:
            cantidad = product["quantity"] 
            precio = product["prize"]
            subtotal = cantidad * precio
            total += subtotal
            print(f"Producto : {product['name']} (x{product['quantity']}) -> S/.{subtotal:.2f} ")


def compra_finalizada():
    
    if len(SHOPPING_CART) == 0:
        print("No realizo ninguna compra")
    else:
        print("Resumen de compra: ")
        total = 0
        for product in SHOPPING_CART:
            cantidad = product["quantity"]
            precio = product["prize"]
            subtotal  = cantidad * precio
            total +=subtotal
            print(f"{product['name']} (x{cantidad}) -> S/.{subtotal:.2f} ")

        print(f"Total a pagar :{total:.2f} ")    
        print("Gracias por su compra ")

    SHOPPING_CART.clear()


def main():
    
    while True:

        show_menu()
        option = input("Eliga una opcion:")
        
        try :
            if option == "1":
                show_catalog()
            elif option == "2":
                add_product = input("Ingrese el producto :")
                add_product_to_cart(add_product)
            elif option =="3":
                remove_product = input("Ingrese el producto a eliminar:")
                remove_cart(remove_product)
            elif option =="4":
                empty_cart()
            elif option == "5":
                show_cart()
            elif option == "6":
               compra_finalizada()
            elif option == "7":
                break
                

        except ValueError : 
            print("Ingrese un número válido para la opcion")

            
main()