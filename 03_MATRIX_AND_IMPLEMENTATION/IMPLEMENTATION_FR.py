#!/usr/bin/env python3
"""
LA MATRICE DES INNOMMABLES - IMPLÉMENTATION
Version : 1.0
Date : 17 janvier 2026

Matrice de référence 9×9×9 pour le calcul du hasard
Issu du Théorème des Innommables

COLLABORATIONS & FORMALISATION :
Auteur et Concepteur Principal : Jérôme Garidel
Systèmes de Formalisation : Claude (Anthropic), Gemini (Google), Grok (xAI)

Protection : INPI e-Soleau (DSO2026001939)
Licence : CC BY-NC-SA
Contact : JeromeGaridel@outlook.fr
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# ============================================================
# MATRICE DE BASE
# ============================================================

class MatriceInnommables:
    """
    Matrice des Innommables - Framework 9×9×9
    
    Calcule la position angulaire θ à partir de Xₛ (= ⧉ₛ)
    """
    
    def __init__(self, theta_0=120, phi=40):
        """
        Initialise la matrice
        
        Args:
            theta_0: Point d'entrée (défaut: 120°, charge mo)
            phi: Phase constante (défaut: 40° = 360°/9)
        """
        self.theta_0 = theta_0
        self.phi = phi
    
    def calculer_theta(self, Xs):
        """
        Calcule la position angulaire θ
        
        Args:
            Xs: Xₛ = ⧉ₛ (composante provisoire)
        
        Returns:
            float: θ dans [0, 360°[
        """
        theta = self.theta_0 + (Xs * self.phi)
        return theta % 360
    
    def position_tenseur(self, Xs):
        """
        Calcule la position (i,j,k) dans le tenseur 9×9×9
        
        Args:
            Xs: Xₛ = ⧉ₛ
        
        Returns:
            tuple: (i, j, k) où i,j,k ∈ [0,8]
        """
        theta = self.calculer_theta(Xs)
        
        i = int((theta / 40) % 9)
        j = int((theta / 40 + 3) % 9)
        k = int((theta / 40 + 6) % 9)
        
        return (i, j, k)
    
    def determiner_bloc(self, Xs):
        """
        Détermine dans quel BLOC se trouve θ
        
        Args:
            Xs: Xₛ = ⧉ₛ
        
        Returns:
            tuple: (nom_bloc, polarite)
        """
        theta = self.calculer_theta(Xs)
        
        if theta < 120:
            return ('mo', +1)
        elif theta < 240:
            return ('ch', 0)
        else:
            return ('cy', -1)

# ============================================================
# APPLICATION : DÉ À 6 FACES
# ============================================================

class De6Faces(MatriceInnommables):
    """
    Application de la Matrice des Innommables à un dé
    
    Xₛ = nombre de rebonds
    """
    
    def calculer_face(self, Xs):
        """
        Calcule la face du dé
        
        Args:
            Xs: Xₛ = ⧉ₛ = Nombre de rebonds
        
        Returns:
            int: ⧉ = Face (1-6)
        """
        theta = self.calculer_theta(Xs)
        face = int(theta / 60) + 1
        return face
    
    def trouver_Xs_pour_face(self, face_cible):
        """
        Trouve les valeurs de Xₛ qui donnent une face
        
        Args:
            face_cible: Face désirée (1-6)
        
        Returns:
            list: Liste des Xₛ dans un cycle de 9
        """
        Xs_valides = []
        
        for Xs in range(1, 10):
            if self.calculer_face(Xs) == face_cible:
                Xs_valides.append(Xs)
        
        return Xs_valides
    
    def analyser_distribution(self, n_cycles=6):
        """
        Analyse la distribution sur plusieurs cycles
        
        Args:
            n_cycles: Nombre de cycles de 9 à tester
        
        Returns:
            tuple: (stats dict, faces list)
        """
        faces = []
        n_total = n_cycles * 9
        
        for Xs in range(1, n_total + 1):
            face = self.calculer_face(Xs)
            faces.append(face)
        
        counter = Counter(faces)
        
        stats = {}
        for f in range(1, 7):
            count = counter.get(f, 0)
            pct = count / n_total * 100
            stats[f] = {
                'count': count,
                'pourcentage': pct,
                'ecart': abs(pct - 100/6)
            }
        
        return stats, faces

# ============================================================
# EXEMPLES ET TESTS
# ============================================================

if __name__ == "__main__":
    print("="*80)
    print("MATRICE DES INNOMMABLES - DÉMONSTRATION")
    print("="*80)
    
    # Créer une instance pour un dé
    de = De6Faces()
    
    # Exemple 1 : Obtenir face 4
    print("\n--- Exemple 1 : Obtenir face 4 ---\n")
    
    Xs_pour_4 = de.trouver_Xs_pour_face(4)
    print(f"Pour obtenir face 4, utiliser Xₛ ∈ {Xs_pour_4}")
    
    for Xs in Xs_pour_4:
        theta = de.calculer_theta(Xs)
        face = de.calculer_face(Xs)
        bloc, pol = de.determiner_bloc(Xs)
        print(f"  Xₛ = {Xs} → θ = {theta:.0f}° → BLOC {bloc} ({pol:+d}) → Face {face}")
    
    # Exemple 2 : Périodicité
    print("\n--- Exemple 2 : Périodicité ---\n")
    
    for Xs in [2, 11, 20]:
        theta = de.calculer_theta(Xs)
        face = de.calculer_face(Xs)
        print(f"Xₛ = {Xs:2d} → θ = {theta:.0f}° → Face {face}")
    
    # Analyse distribution
    print("\n--- Analyse distribution (54 lancers = 6 cycles) ---\n")
    
    stats, faces = de.analyser_distribution(n_cycles=6)
    
    print("Face | Count | %     | Écart")
    print("-----|-------|-------|------")
    for f in range(1, 7):
        s = stats[f]
        print(f"  {f}  |  {s['count']:2d}   | {s['pourcentage']:5.1f} | {s['ecart']:5.2f}%")
    
    ecart_moyen = np.mean([s['ecart'] for s in stats.values()])
    print(f"\nÉcart moyen à l'uniforme : {ecart_moyen:.2f}%")
    
    # Graphique
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Graph 1 : Séquence
    Xs_vals = list(range(1, 55))
    faces_vals = [de.calculer_face(Xs) for Xs in Xs_vals]
    colors_map = {1:'red', 2:'blue', 3:'green', 4:'orange', 5:'purple', 6:'brown'}
    colors = [colors_map[f] for f in faces_vals]
    
    ax1.scatter(Xs_vals, faces_vals, c=colors, s=50, alpha=0.6, edgecolors='black')
    ax1.set_xlabel('Xₛ (nombre de rebonds)', fontsize=11)
    ax1.set_ylabel('Face du dé', fontsize=11)
    ax1.set_yticks([1,2,3,4,5,6])
    ax1.set_title('Séquence des faces (Matrice des Innommables)', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Graph 2 : Distribution
    faces_list = list(range(1, 7))
    counts = [stats[f]['count'] for f in faces_list]
    colors_bars = [colors_map[f] for f in faces_list]
    
    ax2.bar(faces_list, counts, color=colors_bars, alpha=0.7, edgecolor='black', linewidth=2)
    ax2.axhline(y=9, color='red', linestyle='--', linewidth=2, label='Uniforme (1/6)')
    ax2.set_xlabel('Face du dé', fontsize=11)
    ax2.set_ylabel("Nombre d'occurrences", fontsize=11)
    ax2.set_title('Distribution sur 54 lancers', fontsize=12, fontweight='bold')
    ax2.set_xticks(faces_list)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/matrice_innommables_demo.png', dpi=150)
    
    print("\n📊 Graphique sauvegardé : matrice_innommables_demo.png")
    print("\n" + "="*80)
    print("✅ DÉMONSTRATION TERMINÉE")
    print("="*80)
