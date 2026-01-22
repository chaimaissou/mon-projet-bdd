from config.database import get_connection
import pandas as pd

class DatabaseManager:
    
    @staticmethod
    def get_user_by_credentials(matricule, nom, prenom):
        conn = get_connection()
        if not conn:
            return None
        
        cursor = conn.cursor(dictionary=True)
        
        tables = [
            ('administrateurs', 'Administrateur'),
            ('professeurs', 'Professeur'),
            ('etudiants', 'Etudiant')
        ]
        
        for table, role in tables:
            query = f"""
                SELECT * FROM {table} 
                WHERE matricule = %s AND nom = %s AND prenom = %s
            """
            cursor.execute(query, (matricule, nom, prenom))
            user = cursor.fetchone()
            
            if user:
                user['role'] = role
                user['table'] = table
                conn.close()
                return user
        
        conn.close()
        return None
    
    @staticmethod
    def get_all_examens():
        conn = get_connection()
        if not conn:
            return pd.DataFrame()
        
        query = """
            SELECT 
                e.id,
                e.date_heure,
                e.duree_minutes,
                e.type_examen,
                m.nom as module,
                m.code as module_code,
                l.nom as salle,
                l.code as salle_code,
                l.capacite,
                f.nom as formation,
                d.nom as departement,
                CONCAT(p.nom, ' ', p.prenom) as professeur
            FROM examens e
            LEFT JOIN modules m ON e.module_id = m.id
            LEFT JOIN lieu_examen l ON e.salle_id = l.id
            LEFT JOIN formations f ON m.formation_id = f.id
            LEFT JOIN departements d ON f.dept_id = d.id
            LEFT JOIN professeurs p ON e.surveillant_principal_id = p.id
            ORDER BY e.date_heure
        """
        
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    
    @staticmethod
    def get_statistics():
        conn = get_connection()
        if not conn:
            return {}
        
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM vue_statistiques_globales")
        stats = cursor.fetchone()
        
        conn.close()
        return stats if stats else {}
    
    @staticmethod
    def get_available_rooms():
        conn = get_connection()
        if not conn:
            return pd.DataFrame()
        
        query = "SELECT * FROM lieu_examen WHERE disponibilite = 1"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    
    # Ajouter ces méthodes à la classe DatabaseManager

@staticmethod
def check_room_availability(room_id, date_heure, duree_minutes):
    """
    Vérifie si une salle est disponible à un créneau donné
    """
    conn = get_connection()
    if not conn:
        return False
    
    cursor = conn.cursor()
    
    query = """
        SELECT COUNT(*) as count
        FROM examens e
        WHERE e.salle_id = %s
        AND e.date_heure < DATE_ADD(%s, INTERVAL %s MINUTE)
        AND DATE_ADD(e.date_heure, INTERVAL e.duree_minutes MINUTE) > %s
    """
    
    try:
        cursor.execute(query, (room_id, date_heure, duree_minutes, date_heure))
        result = cursor.fetchone()
        conn.close()
        return result[0] == 0  # True si aucun conflit
    except:
        conn.close()
        return False

@staticmethod
def get_room_occupation(room_id, date_heure, duree_minutes):
    """
    Retourne l'examen qui occupe la salle si elle n'est pas disponible
    """
    conn = get_connection()
    if not conn:
        return None
    
    query = """
        SELECT m.code, m.nom, e.date_heure
        FROM examens e
        JOIN modules m ON e.module_id = m.id
        WHERE e.salle_id = %s
        AND e.date_heure < DATE_ADD(%s, INTERVAL %s MINUTE)
        AND DATE_ADD(e.date_heure, INTERVAL e.duree_minutes MINUTE) > %s
        LIMIT 1
    """
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (room_id, date_heure, duree_minutes, date_heure))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return f"{result['code']} - {result['nom']} à {result['date_heure']}"
        return None
    except:
        conn.close()
        return None
    
    
    @staticmethod
    def get_modules_by_formation(formation_id):
        conn = get_connection()
        if not conn:
            return pd.DataFrame()
        
        query = """
            SELECT m.*, CONCAT(p.nom, ' ', p.prenom) as professeur
            FROM modules m
            LEFT JOIN professeurs p ON m.professeur_id = p.id
            WHERE m.formation_id = %s
        """
        df = pd.read_sql(query, conn, params=(formation_id,))
        conn.close()
        return df
    
    @staticmethod
    def get_all_modules():
        conn = get_connection()
        if not conn:
            return pd.DataFrame()
        
        query = """
            SELECT m.*, 
                   CONCAT(p.nom, ' ', p.prenom) as professeur,
                   f.nom as formation,
                   d.nom as departement
            FROM modules m
            LEFT JOIN professeurs p ON m.professeur_id = p.id
            LEFT JOIN formations f ON m.formation_id = f.id
            LEFT JOIN departements d ON f.dept_id = d.id
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    
    @staticmethod
    def get_all_professeurs():
        conn = get_connection()
        if not conn:
            return pd.DataFrame()
        
        query = """
            SELECT p.*, d.nom as departement
            FROM professeurs p
            LEFT JOIN departements d ON p.dept_id = d.id
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    
    @staticmethod
    def insert_examen(module_id, date_heure, duree, salle_id, surveillant_id):
        conn = get_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        
        query = """
            INSERT INTO examens 
            (module_id, date_heure, duree_minutes, salle_id, surveillant_principal_id, statut)
            VALUES (%s, %s, %s, %s, %s, 'Planifié')
        """
        
        try:
            cursor.execute(query, (module_id, date_heure, duree, salle_id, surveillant_id))
            conn.commit()
            success = True
        except Exception as e:
            print(f"Erreur insertion: {e}")
            conn.rollback()
            success = False
        
        conn.close()
        return success
    
    @staticmethod
    def delete_all_examens():
        conn = get_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        
        try:
            cursor.execute("DELETE FROM examens")
            conn.commit()
            success = True
        except Exception as e:
            print(f"Erreur suppression: {e}")
            conn.rollback()
            success = False
        
        conn.close()
        return success