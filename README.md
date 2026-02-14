## 🛑 Skip the XCrySDen Headache
Visualizing Quantum ESPRESSO structures often requires legacy software like **XCrySDen**, which can be difficult to install and maintain on modern operating systems. 

**QE-2-CIF** removes this dependency. Instead of wrestling with outdated display drivers, this script lets you:
1.  Convert your output directly to a modern **CIF** format.
2.  Open your structure immediately in **VESTA**, **CrystalMaker**, or **Avogadro**.
3.  Generate publication-quality figures without needing legacy X11 tools.

**Key Features**
1. Optimization-Aware: Specifically optimized for vc-relax and relax jobs. It uses "greedy" pattern matching to extract only the final, converged coordinates.

2. Automatic Unit Handling: Smart detection for Angstrom, Bohr, and Crystal (fractional) units.

3. Fault-Tolerant: Built to handle inconsistencies across different QE versions, including robust handling for missing unit tags.

**🛠 Setup & Execution (Using VS Code)**

While you can use any terminal, VS Code is recommended for a better development experience.
1. Clone & Open
Bash

git clone https://github.com/rohitnongmaithem57-lang/QE-2-CIF.git

Open the folder in VS Code (File > Open Folder...).
2. Configure the Environment

Open the internal terminal in VS Code (Ctrl + ~) and run:
Bash

# Create and activate environment
python3 -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

3. Run the Script

    Place your QE file (.in or .out) in the folder.

    Open QE.py and modify the filename in the function call at the bottom:
    Python

    universal_qe_to_cif("YOUR_FILENAME.out", "output.cif")

    Run the script by clicking the "Run" button in the top-right of VS Code or typing python QE.py in the terminal.

**Technical Requirements**

    Python 3.8+

    Pymatgen: For high-fidelity CIF generation and lattice math.

    Re: Standard library for regex-based pattern extraction.

**License**

This project is licensed under the MIT License—see the LICENSE file for details.

## 🎓 How to Cite
If you use **QE-2-CIF** in your research, please cite it as follows:

**Nongmaithem, R. (2026). QE-2-CIF: A Universal Quantum ESPRESSO Structure Converter.** Retrieved from: https://github.com/rohitnongmaithem57-lang/QE-2-CIF
