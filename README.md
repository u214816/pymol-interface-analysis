# PyMOL Protein Interface Analysis

This repository contains a simple PyMOL script to analyze the interface between two proteins in a structural complex.

The script identifies interface residues based on an atom–atom distance cutoff, displays them as sticks, prints the selected residues, and creates distance objects for contacts across the interface.

## Requirements

- PyMOL
- A protein complex loaded in PyMOL
- Two protein objects or selections named `PROTEIN1` and `PROTEIN2`

## Usage

1. Open PyMOL.
2. Load your protein complex structure.
3. Rename or select the two proteins as `PROTEIN1` and `PROTEIN2`.
4. Run the script from the PyMOL command line:

```python
run analyze_interface.py
