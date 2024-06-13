from .config import conn, cursor

class Client:

    def __init__(
        self, first_name, last_name, phone, email, feedback, location,id=None
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email=email
        self.feedback = feedback 
        self.location = location 
        

    def __repr__(self):
        return f"<Client {self.first_name} {self.last_name}  {self.phone} {self.email} {self.feedback} {self.location} >"

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS clients;
        """

        cursor.execute(sql)
        conn.commit()
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE clients (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            feedback TEXT,
            location TEXT
            )
        """

        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO clients (
            first_name, last_name, phone, email, feedback, location
            ) VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            sql,
            (
                self.first_name,
                self.last_name,
                self.phone,
                self.email,
                self.feedback,
                self.location,
            ),
        )
        conn.commit()
         
        self.id = cursor.lastrowid

    @classmethod
    def create(cls, first_name, last_name, phone, email, feedback, location):
        
        Client = cls(first_name, last_name, phone, email,feedback, location)
        
        Client.save()
        return Client

    def update(self):
        sql = """
            UPDATE clients SET first_name = ?, last_name= ?, phone = ?,  email = ?, feedback = ?, location = ?
            WHERE id = ?
        """

        cursor.execute(
            sql,
            (
                self.first_name,
                self.last_name,
                self.phone,
                self.email,
                self.feedback,
                self.location,
                self.id,
            ),
        )

        conn.commit()

    def delete(self):
        sql = """
            DELETE FROM clients
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()
        
    
    @classmethod
    def fetch_by_id(cls,row):
        pass
    
    @classmethod
    def fetch_by_one(clsd,row):
        pass
    @classmethod   
    def fetch_by_phone(cls,phone):
        pass
    
    @classmethod
    def fetch_by_first_name(cls,first_name):
        pass
    
    