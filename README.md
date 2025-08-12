# MCJarAnalyzer - Minecraft Mod JAR Analysis Tool

🔍 A tool for checking Minecraft mod JAR files for potentially unfair advantages
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

## Why This Tool?

Many Minecraft servers and competitions prohibit mods that provide unfair advantages. Some mods might contain code that:
- Modifies hitboxes to make PvP easier
- Alters game mechanics in unintended ways
- Contains hidden functionality not disclosed by the mod author

MCJarAnalyzer helps server administrators and players verify that mods don't contain potentially problematic code before installation.

## Features

✅ Quick Mod Scanning: Upload and analyze multiple JAR files at once  
✅ Modrinth Verification: Checks if mods are published on Modrinth, a trusted mod repository  
⚠️ Hitbox Modification Detection: Identifies common code patterns used to hitboxes  
🌐 Simple Web Interface: User-friendly design for easy mod verification  
📦 Batch Processing: Analyze multiple mods in one go  

## Current Limitations

This is a minimal example project. For production use, consider adding:
- Database integration for caching scan results
- Additional function pattern checks
- Integration with CurseForge API for more comprehensive mod verification

## Installation
```bash
git clone https://github.com/Map4yk/MCJarAnalyzer.git
cd MCJarAnalyzer

pip install flask requests
python main.py
```





