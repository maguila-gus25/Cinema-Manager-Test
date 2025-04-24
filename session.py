#Sessão
#Atributos: filme, sala, horário, data, ingressos disponíveis.
#Métodos: criarSessao(), atualizarSessao(), cancelarSessao().

from filme import Filme
from sala import Sala
from database import get_db_connection
from datetime import datetime

class Session:
    def __init__(self, movie_id, room_id, time, date, available_tickets, id=None):
        self.id = id
        self.movie_id = movie_id
        self.room_id = room_id
        self.time = time
        self.date = date
        self.available_tickets = available_tickets

    def create_session(self):
        self.save()
        return f"Session created successfully."

    def update_session(self, movie_id=None, room_id=None, time=None, date=None, available_tickets=None):
        if movie_id is not None:
            self.movie_id = movie_id
        if room_id is not None:
            self.room_id = room_id
        if time is not None:
            self.time = time
        if date is not None:
            self.date = date
        if available_tickets is not None:
            self.available_tickets = available_tickets
        self.save()
        return f"Session updated successfully."

    def cancel_session(self):
        self.delete()
        return f"Session cancelled successfully."

    def get_available_seats(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT s.id, s.number, s.status
                FROM seats s
                WHERE s.room_id = ? AND s.status = 'available'
            ''', (self.room_id,))
            return cursor.fetchall()

    def save(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute('''
                    INSERT INTO sessions (movie_id, room_id, time, date, available_tickets)
                    VALUES (?, ?, ?, ?, ?)
                ''', (self.movie_id, self.room_id, self.time, self.date, self.available_tickets))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE sessions
                    SET movie_id = ?, room_id = ?, time = ?, date = ?, available_tickets = ?
                    WHERE id = ?
                ''', (self.movie_id, self.room_id, self.time, self.date, self.available_tickets, self.id))
            conn.commit()

    def delete(self):
        if self.id is not None:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM sessions WHERE id = ?', (self.id,))
                conn.commit()

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM sessions')
            sessions = [Session(row['movie_id'], row['room_id'], row['time'],
                              row['date'], row['available_tickets'], row['id'])
                       for row in cursor.fetchall()]
            return sessions

    @staticmethod
    def get_by_id(session_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM sessions WHERE id = ?', (session_id,))
            row = cursor.fetchone()
            if row:
                return Session(row['movie_id'], row['room_id'], row['time'],
                             row['date'], row['available_tickets'], row['id'])
            return None

    def __str__(self):
        return (f"Session ID: {self.id}\n"
                f"Movie ID: {self.movie_id}\n"
                f"Room ID: {self.room_id}\n"
                f"Time: {self.time}\n"
                f"Date: {self.date}\n"
                f"Available Tickets: {self.available_tickets}")
