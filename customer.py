from database import get_db_connection

class Cliente:
    def __init__(self, nome, email, telefone, historico_compras=None, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.historico_compras = historico_compras or []

    def save(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute('''
                    INSERT INTO clientes (nome, email, telefone, historico_compras)
                    VALUES (?, ?, ?, ?)
                ''', (self.nome, self.email, self.telefone, str(self.historico_compras)))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE clientes
                    SET nome = ?, email = ?, telefone = ?, historico_compras = ?
                    WHERE id = ?
                ''', (self.nome, self.email, self.telefone, str(self.historico_compras), self.id))
            conn.commit()

    def delete(self):
        if self.id is not None:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM clientes WHERE id = ?', (self.id,))
                conn.commit()

    def adicionar_compra(self, venda_id):
        if venda_id not in self.historico_compras:
            self.historico_compras.append(venda_id)
            self.save()

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM clientes')
            clientes = [Cliente(row['nome'], row['email'], row['telefone'], 
                              eval(row['historico_compras']), row['id'])
                       for row in cursor.fetchall()]
            return clientes

    @staticmethod
    def get_by_id(cliente_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM clientes WHERE id = ?', (cliente_id,))
            row = cursor.fetchone()
            if row:
                return Cliente(row['nome'], row['email'], row['telefone'], 
                             eval(row['historico_compras']), row['id'])
            return None

    def __str__(self):
        return f"Cliente: {self.nome} - Email: {self.email} - Telefone: {self.telefone}" 