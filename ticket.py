#Ingresso
#Atributos: sessão, assento, preço, status.
#Métodos: emitirIngresso(), cancelarIngresso(), verificarDisponibilidade().

from database import get_db_connection

class Ticket:
    def __init__(self, session_id, seat_id, price, status='available', id=None):
        self.id = id
        self.session_id = session_id
        self.seat_id = seat_id
        self.price = price
        self.status = status

    def issue_ticket(self):
        if self.status == 'available':
            self.status = 'sold'
            self.save()
            return f"Ticket issued successfully."
        return "Ticket is not available."

    def cancel_ticket(self):
        if self.status == 'sold':
            self.status = 'available'
            self.save()
            return f"Ticket cancelled successfully."
        return "Ticket cannot be cancelled."

    def check_availability(self):
        return self.status == 'available'

    def save(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute('''
                    INSERT INTO tickets (session_id, seat_id, price, status)
                    VALUES (?, ?, ?, ?)
                ''', (self.session_id, self.seat_id, self.price, self.status))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE tickets
                    SET session_id = ?, seat_id = ?, price = ?, status = ?
                    WHERE id = ?
                ''', (self.session_id, self.seat_id, self.price, self.status, self.id))
            conn.commit()

    def delete(self):
        if self.id is not None:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM tickets WHERE id = ?', (self.id,))
                conn.commit()

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tickets')
            tickets = [Ticket(row['session_id'], row['seat_id'], row['price'],
                            row['status'], row['id'])
                      for row in cursor.fetchall()]
            return tickets

    @staticmethod
    def get_by_id(ticket_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tickets WHERE id = ?', (ticket_id,))
            row = cursor.fetchone()
            if row:
                return Ticket(row['session_id'], row['seat_id'], row['price'],
                            row['status'], row['id'])
            return None

    def __str__(self):
        return (f"Ticket ID: {self.id}\n"
                f"Session ID: {self.session_id}\n"
                f"Seat ID: {self.seat_id}\n"
                f"Price: ${self.price:.2f}\n"
                f"Status: {self.status}")
