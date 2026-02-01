#!/usr/bin/env python3
"""
THE MATRIX OF THE UNNAMEABLE - IMPLEMENTATION
Version: 1.0
Date: January 17, 2026

9×9×9 Reference Matrix for Computing Randomness
Derived from the Theorem of the Unnameable

COLLABORATIONS & FORMALIZATION:
Author and Principal Conceptor: Jérôme Garidel
Formalization Systems: Claude (Anthropic), Gemini (Google), Grok (xAI)

Protection: INPI e-Soleau (DSO2026001939)
License: CC BY-NC-SA
Contact: JeromeGaridel@outlook.fr
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# ============================================================
# BASE MATRIX
# ============================================================

class MatrixUnnameable:
    """
    Matrix of the Unnameable - 9×9×9 Framework
    
    Calculates angular position θ from Xₛ (= ⧉ₛ)
    """
    
    def __init__(self, theta_0=120, phi=40):
        """
        Initialize the matrix
        
        Args:
            theta_0: Entry point (default: 120°, mo charge)
            phi: Phase constant (default: 40° = 360°/9)
        """
        self.theta_0 = theta_0
        self.phi = phi
    
    def calculate_theta(self, Xs):
        """
        Calculate angular position θ
        
        Args:
            Xs: Xₛ = ⧉ₛ (provisional component)
        
        Returns:
            float: θ in [0, 360°[
        """
        theta = self.theta_0 + (Xs * self.phi)
        return theta % 360
    
    def tensor_position(self, Xs):
        """
        Calculate position (i,j,k) in the 9×9×9 tensor
        
        Args:
            Xs: Xₛ = ⧉ₛ
        
        Returns:
            tuple: (i, j, k) where i,j,k ∈ [0,8]
        """
        theta = self.calculate_theta(Xs)
        
        i = int((theta / 40) % 9)
        j = int((theta / 40 + 3) % 9)
        k = int((theta / 40 + 6) % 9)
        
        return (i, j, k)
    
    def determine_block(self, Xs):
        """
        Determine which BLOCK contains θ
        
        Args:
            Xs: Xₛ = ⧉ₛ
        
        Returns:
            tuple: (block_name, polarity)
        """
        theta = self.calculate_theta(Xs)
        
        if theta < 120:
            return ('mo', +1)
        elif theta < 240:
            return ('ch', 0)
        else:
            return ('cy', -1)

# ============================================================
# APPLICATION: 6-SIDED DIE
# ============================================================

class Die6Faces(MatrixUnnameable):
    """
    Application of the Matrix of the Unnameable to a die
    
    Xₛ = number of bounces
    """
    
    def calculate_face(self, Xs):
        """
        Calculate the die face
        
        Args:
            Xs: Xₛ = ⧉ₛ = Number of bounces
        
        Returns:
            int: ⧉ = Face (1-6)
        """
        theta = self.calculate_theta(Xs)
        face = int(theta / 60) + 1
        return face
    
    def find_Xs_for_face(self, target_face):
        """
        Find Xₛ values that produce a given face
        
        Args:
            target_face: Desired face (1-6)
        
        Returns:
            list: List of Xₛ in one cycle of 9
        """
        valid_Xs = []
        
        for Xs in range(1, 10):
            if self.calculate_face(Xs) == target_face:
                valid_Xs.append(Xs)
        
        return valid_Xs
    
    def analyze_distribution(self, n_cycles=6):
        """
        Analyze distribution over multiple cycles
        
        Args:
            n_cycles: Number of 9-step cycles to test
        
        Returns:
            tuple: (stats dict, faces list)
        """
        faces = []
        n_total = n_cycles * 9
        
        for Xs in range(1, n_total + 1):
            face = self.calculate_face(Xs)
            faces.append(face)
        
        counter = Counter(faces)
        
        stats = {}
        for f in range(1, 7):
            count = counter.get(f, 0)
            pct = count / n_total * 100
            stats[f] = {
                'count': count,
                'percentage': pct,
                'deviation': abs(pct - 100/6)
            }
        
        return stats, faces

# ============================================================
# EXAMPLES AND TESTS
# ============================================================

if __name__ == "__main__":
    print("="*80)
    print("MATRIX OF THE UNNAMEABLE - DEMONSTRATION")
    print("="*80)
    
    # Create a die instance
    die = Die6Faces()
    
    # Example 1: Obtaining face 4
    print("\n--- Example 1: Obtaining face 4 ---\n")
    
    Xs_for_4 = die.find_Xs_for_face(4)
    print(f"To obtain face 4, use Xₛ ∈ {Xs_for_4}")
    
    for Xs in Xs_for_4:
        theta = die.calculate_theta(Xs)
        face = die.calculate_face(Xs)
        block, pol = die.determine_block(Xs)
        print(f"  Xₛ = {Xs} → θ = {theta:.0f}° → BLOCK {block} ({pol:+d}) → Face {face}")
    
    # Example 2: Periodicity
    print("\n--- Example 2: Periodicity ---\n")
    
    for Xs in [2, 11, 20]:
        theta = die.calculate_theta(Xs)
        face = die.calculate_face(Xs)
        print(f"Xₛ = {Xs:2d} → θ = {theta:.0f}° → Face {face}")
    
    # Distribution analysis
    print("\n--- Distribution analysis (54 rolls = 6 cycles) ---\n")
    
    stats, faces = die.analyze_distribution(n_cycles=6)
    
    print("Face | Count | %     | Deviation")
    print("-----|-------|-------|----------")
    for f in range(1, 7):
        s = stats[f]
        print(f"  {f}  |  {s['count']:2d}   | {s['percentage']:5.1f} | {s['deviation']:5.2f}%")
    
    avg_deviation = np.mean([s['deviation'] for s in stats.values()])
    print(f"\nAverage deviation from uniform: {avg_deviation:.2f}%")
    
    # Graphics
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Graph 1: Sequence
    Xs_vals = list(range(1, 55))
    faces_vals = [die.calculate_face(Xs) for Xs in Xs_vals]
    colors_map = {1:'red', 2:'blue', 3:'green', 4:'orange', 5:'purple', 6:'brown'}
    colors = [colors_map[f] for f in faces_vals]
    
    ax1.scatter(Xs_vals, faces_vals, c=colors, s=50, alpha=0.6, edgecolors='black')
    ax1.set_xlabel('Xₛ (number of bounces)', fontsize=11)
    ax1.set_ylabel('Die face', fontsize=11)
    ax1.set_yticks([1,2,3,4,5,6])
    ax1.set_title('Face Sequence (Matrix of the Unnameable)', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Graph 2: Distribution
    faces_list = list(range(1, 7))
    counts = [stats[f]['count'] for f in faces_list]
    colors_bars = [colors_map[f] for f in faces_list]
    
    ax2.bar(faces_list, counts, color=colors_bars, alpha=0.7, edgecolor='black', linewidth=2)
    ax2.axhline(y=9, color='red', linestyle='--', linewidth=2, label='Uniform (1/6)')
    ax2.set_xlabel('Die face', fontsize=11)
    ax2.set_ylabel('Number of occurrences', fontsize=11)
    ax2.set_title('Distribution over 54 rolls', fontsize=12, fontweight='bold')
    ax2.set_xticks(faces_list)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('/mnt/user-data/outputs/matrix_unnameable_demo.png', dpi=150)
    
    print("\n📊 Graphic saved: matrix_unnameable_demo.png")
    print("\n" + "="*80)
    print("✅ DEMONSTRATION COMPLETED")
    print("="*80)
