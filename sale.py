#Venda
#Atributos: cliente, ingresso, método de pagamento, total.
#Métodos: registrarVenda(), cancelarVenda(), gerarRecibo().

from database import get_db_connection
from datetime import datetime

class Sale:
    def __init__(self, client_id, ticket_id, payment_method, total, id=None):
        self.id = id
        self.client_id = client_id
        self.ticket_id = ticket_id
        self.payment_method = payment_method
        self.total = total

    def register_sale(self):
        self.save()
        return f"Sale registered successfully."

    def cancel_sale(self):
        self.delete()
        return f"Sale cancelled successfully."

    def generate_receipt(self):
        return f"Receipt for Sale #{self.id}\n" \
               f"Client ID: {self.client_id}\n" \
               f"Ticket ID: {self.ticket_id}\n" \
               f"Payment Method: {self.payment_method}\n" \
               f"Total: ${self.total:.2f}"

    def save(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute('''
                    INSERT INTO sales (client_id, ticket_id, payment_method, total)
                    VALUES (?, ?, ?, ?)
                ''', (self.client_id, self.ticket_id, self.payment_method, self.total))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE sales
                    SET client_id = ?, ticket_id = ?, payment_method = ?, total = ?
                    WHERE id = ?
                ''', (self.client_id, self.ticket_id, self.payment_method, self.total, self.id))
            conn.commit()

    def delete(self):
        if self.id is not None:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM sales WHERE id = ?', (self.id,))
                conn.commit()

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM sales')
            sales = [Sale(row['client_id'], row['ticket_id'], row['payment_method'],
                         row['total'], row['id'])
                    for row in cursor.fetchall()]
            return sales

    @staticmethod
    def get_by_id(sale_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM sales WHERE id = ?', (sale_id,))
            row = cursor.fetchone()
            if row:
                return Sale(row['client_id'], row['ticket_id'], row['payment_method'],
                          row['total'], row['id'])
            return None

    def __str__(self):
        return (f"Sale ID: {self.id}\n"
                f"Client ID: {self.client_id}\n"
                f"Ticket ID: {self.ticket_id}\n"
                f"Payment Method: {self.payment_method}\n"
                f"Total: ${self.total:.2f}")