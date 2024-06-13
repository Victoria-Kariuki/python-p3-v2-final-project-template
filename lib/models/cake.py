from .config import conn, cursor

class Cake:

    def __init__(
        self, cake_type, flavour, client_id,id=None
    ):
        self.id = id
        self.cake_type = cake_type
        self.flavour = flavour
        self.client_id = client_id
        
    def __repr__(self):
        return f"<Client {self.cake_type} {self.flavour}  {self.client_id} >"

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS cake;
        """

        cursor.execute(sql)
        conn.commit()
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE cake(
            id INTEGER PRIMARY KEY,
            cake_type TEXT NOT NULL,
            flavour TEXT NOT NULL,
            client_id TEXT NOT NULL
            )
        """

        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO cake (
            cake_type, flavour, client_id
            ) VALUES (?, ?, ?)
        """

        cursor.execute(
            sql,
            (
                self.cake_type,
                self.flavour,
                self.client_id,
            ),
        )
        conn.commit()
         
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, cake_type, flavour, client_id):
        
        Cake = cls(cake_type, flavour, client_id)
        
        Cake.save()
        return Cake

    def update(self):
        sql = """
            UPDATE cake SET cake_type = ?, flavour= ?, client_id = ?
            WHERE id = ?
        """

        cursor.execute(
            sql,
            (
                self.cake_type,
                self.flavour,
                self.client_id,
            ),
        )

        conn.commit()

    def delete(self):
        sql = """
            DELETE FROM cake
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
        
    
    @classmethod
    def fetch_by_id(cls, id):
        query = "SELECT * FROM cake WHERE id = ?"
        cursor.execute(query, (id,))
        cake = cursor.fetchone()
        
        return cls(*cake) if cake else None
    
    @classmethod
    def fetch_by_one(clsd,row):
        pass
    @classmethod   
    def fetch_by_client_id(cls,client_id):
        pass
    
    @classmethod
    def fetch_by_type(cls,cake_type):
        pass
    
    