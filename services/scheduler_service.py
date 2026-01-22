import pandas as pd
from datetime import datetime, timedelta
import random
from models.db_manager import DatabaseManager

class SchedulerService:
    
    @staticmethod
    def generate_schedule_with_modules(date_debut, date_fin, selected_modules, duree_creneau):
        salles = DatabaseManager.get_available_rooms()
        
        if not selected_modules or salles.empty:
            return [], []
        
        examens = []
        conflits = []
        
        current_date = datetime.strptime(date_debut, '%Y-%m-%d')
        end_date = datetime.strptime(date_fin, '%Y-%m-%d')
        
        horaires = ['08:00', '10:30', '14:00', '16:30']
        
        module_idx = 0
        
        while current_date <= end_date and module_idx < len(selected_modules):
            for heure in horaires:
                if module_idx >= len(selected_modules):
                    break
                
                module = selected_modules[module_idx]
                salle = salles.iloc[module_idx % len(salles)]
                
                date_heure = f"{current_date.strftime('%Y-%m-%d')} {heure}"
                
                examen = {
                    'module_id': module['module_id'],
                    'module': module['module_nom'],
                    'module_code': module['module_code'],
                    'date_heure': date_heure,
                    'duree': duree_creneau,
                    'salle_id': salle['id'],
                    'salle': salle['nom'],
                    'capacite': salle['capacite'],
                    'surveillant_id': module['surveillant_id'],
                    'surveillant': module['surveillant_nom']
                }
                
                examens.append(examen)
                module_idx += 1
            
            current_date += timedelta(days=1)
        
        nb_etudiants = random.randint(60, 90)
        if examens and nb_etudiants > examens[0]['capacite']:
            conflits.append({
                'type': 'Capacité insuffisante',
                'details': f"{examens[0]['salle']}: {nb_etudiants} étudiants pour {examens[0]['capacite']} places",
                'gravite': 'warning'
            })
        
        return examens, conflits
    
    @staticmethod
    def generate_schedule(date_debut, date_fin):
        modules = DatabaseManager.get_modules_by_formation(1)
        salles = DatabaseManager.get_available_rooms()
        
        if modules.empty or salles.empty:
            return [], []
        
        examens = []
        conflits = []
        
        current_date = datetime.strptime(date_debut, '%Y-%m-%d')
        end_date = datetime.strptime(date_fin, '%Y-%m-%d')
        
        horaires = ['08:00', '10:30', '14:00', '16:30']
        
        module_idx = 0
        
        while current_date <= end_date and module_idx < len(modules):
            for heure in horaires:
                if module_idx >= len(modules):
                    break
                
                module = modules.iloc[module_idx]
                salle = salles.iloc[module_idx % len(salles)]
                
                date_heure = f"{current_date.strftime('%Y-%m-%d')} {heure}"
                
                examen = {
                    'module_id': module['id'],
                    'module': module['nom'],
                    'date_heure': date_heure,
                    'duree': 120,
                    'salle_id': salle['id'],
                    'salle': salle['nom'],
                    'capacite': salle['capacite'],
                    'surveillant': module.get('professeur', 'Non assigné')
                }
                
                examens.append(examen)
                module_idx += 1
            
            current_date += timedelta(days=1)
        
        return examens, conflits
    
    @staticmethod
    def save_schedule_to_db(examens):
        DatabaseManager.delete_all_examens()
        
        success_count = 0
        for exam in examens:
            surveillant_id = exam.get('surveillant_id', 1)
            
            if DatabaseManager.insert_examen(
                exam['module_id'],
                exam['date_heure'],
                exam['duree'],
                exam['salle_id'],
                surveillant_id
            ):
                success_count += 1
        
        return success_count == len(examens)