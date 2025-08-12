🔌 MCJarAnalyzer - Checking JAR files for Minecraft mods

Why This Tool?
Many Minecraft servers and competitions prohibit mods that provide unfair advantages. Some mods might contain code that:

Modifies hitboxes to make PvP easier
Alters game mechanics in unintended ways
Contains hidden functionality not disclosed by the mod author
MCJarAnalyzer helps server administrators and players verify that mods don't contain potentially problematic code before installation.

Features
Quick Mod Scanning: Upload and analyze multiple JAR files at once
Modrinth Verification: Checks if mods are published on Modrinth, a trusted mod repository
Hitbox Modification Detection: Identifies common code patterns used to modify entity hitboxes
Simple Web Interface: User-friendly design for easy mod verification
Batch Processing: Analyze multiple mods in one go

Installation
1) Clone the repository:
git clone https://github.com/Map4yk/MCJarAnalyzer.git
cd MCJarAnalyzer
2) Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3) Install dependencies:
pip install flask requests
4) Run the application:
python main.py
5) Open your browser and navigate to:
http://localhost:5000
