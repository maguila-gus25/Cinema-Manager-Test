from database import get_db_connection

class Client:
    def __init__(self, name, email, phone, purchase_history=None, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.purchase_history = purchase_history or []

    def add_purchase(self, purchase_id):
        self.purchase_history.append(purchase_id)
        self.save()
        return f"Purchase added to client's history."

    def save(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute('''
                    INSERT INTO clients (name, email, phone, purchase_history)
                    VALUES (?, ?, ?, ?)
                ''', (self.name, self.email, self.phone, str(self.purchase_history)))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE clients
                    SET name = ?, email = ?, phone = ?, purchase_history = ?
                    WHERE id = ?
                ''', (self.name, self.email, self.phone, str(self.purchase_history), self.id))
            conn.commit()

    def delete(self):
        if self.id is not None:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM clients WHERE id = ?', (self.id,))
                conn.commit()

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM clients')
            clients = [Client(row['name'], row['email'], row['phone'],
                            eval(row['purchase_history']), row['id'])
                      for row in cursor.fetchall()]
            return clients

    @staticmethod
    def get_by_id(client_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM clients WHERE id = ?', (client_id,))
            row = cursor.fetchone()
            if row:
                return Client(row['name'], row['email'], row['phone'],
                            eval(row['purchase_history']), row['id'])
            return None

    def __str__(self):
        return (f"Client: {self.name}\n"
                f"Email: {self.email}\n"
                f"Phone: {self.phone}\n"
                f"Purchase History: {len(self.purchase_history)} purchases") 