import random
import os 
from datetime import date

class menu:

    def principal_menu(self):
        whileMenu = True
        while(whileMenu):
            os.system('cls')
            print("Bienvenido al menu principal USSD")
            print("1 .- Consulta de monto a vencer")
            print("2 .- Contatacion de servicio")
            print("3 .- Fecha de vencimiento proxima factura")
            print("4 .- Salir")
            opcion = int(input("Ingresa un numero de opcion: "))

            if(opcion == 1 ):
                self.ammount_overcome_menu()
            
            if(opcion == 2 ):
                self.contract_service_menu()
            
            if(opcion == 3 ):
                self.date_overcome_menu()

            if(opcion == 4):
                print("!ADIOS¡")
                whileMenu = False

    def ammount_overcome_menu(self):
        os.system('cls')
        print("El pago a vencer es de $ "+ str(random.random()))
        input("Presiona cualquier tecla para regresar al menu principal...")
    
    def contract_service_menu(self):
        os.system('cls')
        print("1.-Nomal")
        print("2.-Plus+")
        option = int(input("Ingresa un numero de opcion del plan que quieres contratar: "))

        plan_name = ""
        if(option == 1):
            plan_name = "Normal"
        elif(option == 2):
            plan_name = "Plus+"
        
        print("Felicidades has contratado el plan: "+ plan_name)

        input("Presiona cualquier tecla para regresar al menu principal...")
    
    def date_overcome_menu(self):
        os.system('cls')
        print("La proxima factura vence el dia: "+str(date.today()))
        input("Presiona cualquier tecla para regresar al menu principal...")
    

if __name__ == '__main__':
    menu().principal_menu()