from pymatgen.core import Structure, Lattice
import re

def universal_qe_to_cif(filename, cif_filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()

        # 1. Extract the LAST Cell Parameters (3x3 matrix)
        cell_match = re.findall(r'CELL_PARAMETERS.*?\n([\s\S]+?)(?=\n\n|\n[A-Z]|\Z)', content, re.IGNORECASE)
        if not cell_match:
            raise ValueError(f"Could not find CELL_PARAMETERS in {filename}.")
        
        cell_lines = cell_match[-1].strip().split('\n')
        matrix = [[float(x) for x in line.split()] for line in cell_lines[:3]]
        lattice = Lattice(matrix)

        # 2. Extract the LAST Atomic Positions
        pos_match = re.findall(r'ATOMIC_POSITIONS.*?\n([\s\S]+?)(?=\n/|\n\n|\Z|End|CELL_PARAMETERS)', content, re.IGNORECASE)
        if not pos_match:
            raise ValueError(f"No ATOMIC_POSITIONS found in {filename}.")

        last_block = pos_match[-1].strip().split('\n')
        species, coords = [], []
        for line in last_block:
            parts = line.split()
            if len(parts) >= 4:
                species.append(parts[0])
                coords.append([float(x) for x in parts[1:4]])

        # 3. Detect Unit Type safely (Fix for the NoneType error)
        unit_search = re.search(r'ATOMIC_POSITIONS\s*{?(\w+)}?', content, re.IGNORECASE)
        unit_type = unit_search.group(1).lower() if unit_search else "angstrom"
        is_cartesian = "crystal" not in unit_type

        # 4. Build and Save
        structure = Structure(lattice, species, coords, coords_are_cartesian=is_cartesian)
        structure.to(filename=cif_filename)
        
        print(f"✅ Success! {filename} -> {cif_filename}")
        print(f"Final count: {len(species)} atoms. Units detected: {unit_type}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Usage
universal_qe_to_cif("espresso.opt.in", "final_structure.cif")