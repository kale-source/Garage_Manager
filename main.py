from app_logic import Oficina
from app_logic import Clientes
import sqlite3 as sql
import time

connect = sql.Connection('database/garage_controller.db')
s = connect.cursor()

def problems():
    breakWhile = True
    
    while breakWhile == True:
        print('='*30)
        print('ACESSO A OFICINA MOTORS CLUB')
        print('='*30)
        print('[1] Cadastrar carros e clientes') # Ok
        print('[2] Concluir reparo de um carro') 
        print('[3] Visualizar carros da oficina') # Ok
        print('[4] Visualizar clientes da oficina') # Ok
        print('[0] Finalizar aplicação') # Ok
        n = int(input('Digite o que você deseja: '))
        print('-'*30)
        if n < 0 or n > 4: print('Digite a opção correta de 0 a 4')

        while n == 1: # Cadastrar carros na oficina
            client = input('Enter client name: ')
            age = int(input('Enter client age: '))
            model = input('Enter the car model: ')
            mark = input('Enter the car mark: ')
            year = int(input('Enter the car year: '))
            plaque = input('Enter the car plaque: ')
            color = input('Enter the car color: ')
            fipeTable = float(input('Enter Fipe Table: '))
            defect = input('Enter car defect: ')
            km = float(input("Enter car KM's: "))
            
            try:
                Oficina.insertCars(model, mark, year, plaque, color, fipeTable, defect, km)
                Clientes.insertClientes(client, age, plaque)
            except ValueError:
                print('SQL Error!')

            check = int(input('[0] STOP | [1] CONTINUE: '))
            if check == 0: break
        
            Oficina(model, mark, year, plaque, color, fipeTable, defect, km) # Classe oficina
            Clientes(client, age) # Classe clientes

            Clientes.listiningClients() # Chama a função para traz2er no console o que foi adicionado
            Oficina.listiningCars() # Chama a função para trazer no console o que foi adicionado

        if n == 0: break

        if n == 2: # Remove da tabela os carros que foram arrumados ou selecionados pelo mecanico
            plaqueCar = str(input('Enter the car plaque to complete: ')).upper()
            db = s.execute("SELECT * FROM cars WHERE plaque = ?", (plaqueCar, ))

            if db == None:
                print('SQL ERROR!')
            else:
                s.execute("DELETE FROM cars WHERE plaque = ?", (plaqueCar, ))
                connect.commit()
                time.sleep(3)
                print('COMPLETE SUCCESSFULL!')

            while True:
                check = int(input('[0] STOP | [1] CONTINUE: '))
                if check == 0:
                    breakWhile = False
                    break
                elif check == 1:
                    break
                elif check != 0 and check != 1:
                    print('Digite a opção correta!')
        
        if n == 3:
            Oficina.viewCars()
            while True:
                check = int(input('[0] STOP | [1] CONTINUE: '))
                if check == 0:
                    breakWhile = False
                    break
                elif check == 1:
                    break
                elif check != 0 and check != 1:
                    print('Digite a opção correta!')
        
        if n == 4:
            Clientes.viewClients()
            while True:
                check = int(input('[0] STOP | [1] CONTINUE: '))
                if check == 0:
                    breakWhile = False
                    break
                elif check == 1:
                    break
                elif check != 0 and check != 1:
                    print('Digite a opção correta!')


problems()
connect.commit()
connect.close()