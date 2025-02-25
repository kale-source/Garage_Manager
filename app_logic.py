import sqlite3 as sql

conn = sql.Connection('database/garage_controller.db')
s = conn.cursor()

class Oficina:
    carsList = []

    def __init__(self, model, mark, year: int, plaque, color, fipeTable: int, defect, km: int):
        self.model = model
        self.mark = mark
        self.year = year
        self.plaque = plaque
        self.color = color
        self.fipeTable = fipeTable
        self.defect = defect
        self.km = km
        Oficina.carsList.append(self) # Todo objeto será acrescentado na lista

    @staticmethod
    def listiningCars():
        for cars in Oficina.carsList:
            print(f'{cars.model} | {cars.mark} | {cars.year} | {cars.plaque} | {cars.color} | {cars.fipeTable:.3f} | {cars.defect} | {cars.km:.3f}')

    @staticmethod
    def insertCars(model, mark, year, plaque, color, fipeTable, defect, km):
        with sql.Connection('database/garage_controller.db') as conn:
            s = conn.cursor()

            idCars = s.execute('SELECT max(id) FROM cars')
            lastIdCars = idCars.fetchone()[0]
            if lastIdCars == None: lastIdCars = 0
            
            sqlInjectCars = [lastIdCars + 1, model, mark, year, plaque, color, fipeTable, defect, km]
            s.execute('INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(sqlInjectCars))

            conn.commit()
    
    @staticmethod
    def viewCars():
        infoCars = ''
        db = s.execute('SELECT * FROM cars')
        print('-'*50)
        print('CARS LIST | MOTORS CLUB')
        print('-'*50)
        for cars in db:
            for infos in cars:
                infoCars += f' | {str(infos)}'
            print(infoCars.strip(' |'))
            infoCars = ''
        print('-'*50)
        
class Clientes:
    clientsList = []

    def __init__(self, name, age: int):
        self.name = name
        self.age = age
        Clientes.clientsList.append(self)

    @staticmethod
    def listiningClients():
        for clients in Clientes.clientsList:
            print(f'Nome: {clients.name} | Idade: {clients.age}')

    @staticmethod
    def insertClientes(client, age, plaque):
        with sql.Connection('database/garage_controller.db') as conn:
            s = conn.cursor()

            idClients = s.execute('SELECT max(id) FROM clients')
            lastIdClients = idClients.fetchone()[0]
            if lastIdClients == None: lastIdClients = 0

            sqlInjectClints = [lastIdClients + 1, client, age, plaque]
            s.execute('INSERT INTO clients VALUES (?, ?, ?, ?)', tuple(sqlInjectClints))

            conn.commit()
    
    @staticmethod
    def viewClients():
        infoClients = ''
        db = s.execute('SELECT * FROM clients')
        print('-'*50)
        print('CLIENTS LIST | MOTORS CLUB')
        print('-'*50)
        for clients in db:
            for infos in clients:
                infoClients += f' | {str(infos)}'
            print(infoClients.strip(' |'))
            infoClients = ''
        print('-'*50)