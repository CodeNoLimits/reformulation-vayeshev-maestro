#!/usr/bin/env python3
"""
Script de compilation finale - Reformulation Vayeshev Maestro
Compile toutes les sections reformulées en un fichier final
"""

import os
import glob

def compile_reformulation():
    print("🔄 COMPILATION FINALE - Reformulation Vayeshev Maestro")
    print("=" * 60)

    # Fichier de sortie
    output_file = "VAYESHEV_REFORMULE_FINAL_MAESTRO.txt"

    # Récupérer le travail déjà fait
    current_work = ""
    if os.path.exists("reformule_en_cours.txt"):
        with open("reformule_en_cours.txt", "r", encoding="utf-8") as f:
            current_work = f.read()
        print(f"✅ Travail existant récupéré: {len(current_work.split())} mots")

    # Parcourir les sections des agents
    total_words = 0
    sections_compiled = 0

    with open(output_file, "w", encoding="utf-8") as final_file:
        # En-tête
        final_file.write("# VAYESHEV - REFORMULATION COMPLÈTE SELON LE PROTOCOLE MAESTRO\n\n")
        final_file.write("*Reformulation intégrale préservant 100% du sens avec 60-80% de restructuration textuelle*\n\n")
        final_file.write("---\n\n")

        # Ajouter le travail déjà fait
        if current_work:
            final_file.write(current_work)
            final_file.write("\n\n---\n\n")
            total_words += len(current_work.split())

        # Parcourir les dossiers de sections
        for i in range(1, 13):
            section_dir = f"../vayeshev-section-{i:02d}"
            output_path = os.path.join(section_dir, "output.txt")

            if os.path.exists(output_path):
                with open(output_path, "r", encoding="utf-8") as f:
                    section_content = f.read()

                words_count = len(section_content.split())
                final_file.write(f"## SECTION {i:02d} - REFORMULÉE\n\n")
                final_file.write(section_content)
                final_file.write("\n\n---\n\n")

                total_words += words_count
                sections_compiled += 1
                print(f"✅ Section {i:02d}: {words_count} mots")
            else:
                print(f"⏳ Section {i:02d}: En attente")

    print("=" * 60)
    print(f"📊 RÉSUMÉ DE COMPILATION:")
    print(f"   • Sections compilées: {sections_compiled}/12")
    print(f"   • Mots total: {total_words:,}")
    print(f"   • Objectif: 58,672 mots")
    print(f"   • Progression: {(total_words/58672)*100:.1f}%")
    print(f"   • Fichier final: {output_file}")

    return total_words, sections_compiled

if __name__ == "__main__":
    compile_reformulation()