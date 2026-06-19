"""
analyze_interface.py
====================
PyMOL script to analyze the interface between two proteins in a complex.

Usage (from PyMOL command line):
    run analyze_interface.py

Requirements:
    - PyMOL (open-source or commercial)
    - A loaded structure containing PROTEIN1 and PROTEIN2 as named selections
      OR modify PROTEIN1_NAME / PROTEIN2_NAME to match your object names.

Author: Miguel Perez Gallego
Date:   05/10/2026
"""

from pymol import cmd


# ──────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────

PROTEIN1_NAME = "PROTEIN1"   # Name of the first  protein object in PyMOL
PROTEIN2_NAME = "PROTEIN2"   # Name of the second protein object in PyMOL
DISTANCE_CUTOFF = 3.0        # Å cutoff to define interface residues


# ──────────────────────────────────────────────
# FUNCTIONS
# ──────────────────────────────────────────────

def select_interface_residues(protein1: str, protein2: str, cutoff: float) -> None:
    """
    Select residues at the interface between two proteins.

    A residue is considered part of the interface if any of its atoms
    lies within *cutoff* Å of the partner protein.

    Parameters
    ----------
    protein1 : str
        PyMOL object/selection name for the first protein.
    protein2 : str
        PyMOL object/selection name for the second protein.
    cutoff : float
        Distance threshold in Ångströms.
    """
    cmd.select(f"iface_{protein1}",
               f"byres ({protein1} within {cutoff} of {protein2})")

    cmd.select(f"iface_{protein2}",
               f"byres ({protein2} within {cutoff} of {protein1})")

    print(f"[INFO] Interface selections created: "
          f"'iface_{protein1}' and 'iface_{protein2}'")


def visualize_interface(protein1: str, protein2: str) -> None:
    """
    Display interface residues as sticks.
    Parameters
    ----------
    protein1 : str
        PyMOL object/selection name for the first protein.
    protein2 : str
        PyMOL object/selection name for the second protein.
    """
    cmd.show("sticks", f"iface_{protein1} or iface_{protein2}")
    print("[INFO] Interface residues shown as sticks.")


def print_interface_residues(protein1: str, protein2: str) -> None:
    """
    Print residue name, residue index, and chain for every Cα atom
    in the interface selections.

    Parameters
    ----------
    protein1 : str
        PyMOL object/selection name for the first protein.
    protein2 : str
        PyMOL object/selection name for the second protein.
    """
    print(f"\n── Interface residues of {protein1} ──")
    cmd.iterate(f"iface_{protein1} and name CA",
                "print(resn, resi, chain)")

    print(f"\n── Interface residues of {protein2} ──")
    cmd.iterate(f"iface_{protein2} and name CA",
                "print(resn, resi, chain)")


def calculate_contacts(protein1: str, protein2: str, cutoff: float) -> None:
    """
    Draw distance objects for all atom pairs within *cutoff* Å
    across the interface.

    Parameters
    ----------
    protein1 : str
        PyMOL object/selection name for the first protein.
    protein2 : str
        PyMOL object/selection name for the second protein.
    cutoff : float
        Distance threshold in Ångströms.
    """
    cmd.distance("contacts",
                 f"iface_{protein1}",
                 f"iface_{protein2}",
                 cutoff)

    print(f"[INFO] Contact distances (≤ {cutoff} Å) stored in object 'contacts'.")


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────

def main():
    """Run the full interface analysis pipeline."""

    print(f"\n{'='*50}")
    print(f"  Protein–Protein Interface Analysis")
    print(f"  {PROTEIN1_NAME}  ↔  {PROTEIN2_NAME}")
    print(f"  Distance cutoff: {DISTANCE_CUTOFF} Å")
    print(f"{'='*50}\n")

    select_interface_residues(PROTEIN1_NAME, PROTEIN2_NAME, DISTANCE_CUTOFF)
    visualize_interface(PROTEIN1_NAME, PROTEIN2_NAME)
    print_interface_residues(PROTEIN1_NAME, PROTEIN2_NAME)
    calculate_contacts(PROTEIN1_NAME, PROTEIN2_NAME, DISTANCE_CUTOFF)

    print("\n[DONE] Interface analysis complete.\n")


main()
