#Sala
#Atributos: número, tipo, capacidade.
#Métodos: criarSala(), atualizarSala(), removerSala().

from database import get_db_connection

class Room:
    def __init__(self, number, type, capacity, id=None):
        self.id = id
        self.number = number
        self.type = type
        self.capacity = capacity

    def add_room(self):
        self.save()
        return f"Room {self.number} added successfully."

    def update_room(self, number=None, type=None, capacity=None):
        if number is not None:
            self.number = number
        if type is not None:
            self.type = type
        if capacity is not None:
            self.capacity = capacity
        self.save()
        return f"Room {self.number} updated successfully."

    def remove_room(self):
        self.delete()
        return f"Room {self.number} removed successfully."

    def save(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute('''
                    INSERT INTO rooms (number, type, capacity)
                    VALUES (?, ?, ?)
                ''', (self.number, self.type, self.capacity))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE rooms
                    SET number = ?, type = ?, capacity = ?
                    WHERE id = ?
                ''', (self.number, self.type, self.capacity, self.id))
            conn.commit()

    def delete(self):
        if self.id is not None:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM rooms WHERE id = ?', (self.id,))
                conn.commit()

    def adicionar_assento(self, fileira, numero):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO assentos (sala_id, fileira, numero, ocupado)
                VALUES (?, ?, ?, 0)
            ''', (self.id, fileira, numero))
            assento_id = cursor.lastrowid
            conn.commit()
            return assento_id

    def get_assentos(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM assentos WHERE sala_id = ?', (self.id,))
            assentos = cursor.fetchall()
            return assentos

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM rooms')
            rooms = [Room(row['number'], row['type'], row['capacity'], row['id'])
                    for row in cursor.fetchall()]
            return rooms

    @staticmethod
    def get_by_id(room_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM rooms WHERE id = ?', (room_id,))
            row = cursor.fetchone()
            if row:
                return Room(row['number'], row['type'], row['capacity'], row['id'])
            return None

    def __str__(self):
        return (f"Room: {self.number}\n"
                f"Type: {self.type}\n"
                f"Capacity: {self.capacity} seats")