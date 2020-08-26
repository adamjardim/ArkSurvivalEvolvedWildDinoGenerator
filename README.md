# Ark: Survival Evolved Wild Dinosaur Code Generator
pyinstaller xXxXx.py --onefile

Game:
Ark: Survival Evolved

Description:
This project contains the source code and executables for generating Server code for Ark: Survival Evolved.  It allows you to select from any of the previously released maps, and within each region, specific dinos (including any variants) that will spawn naturally in those regions, and at what specific rates.  This includes dinosaurs that do not spawn naturally on those maps or specific regions.

The output is server-safe code that will configure the map to automatically spawn the chosen dinosaurs in the chosen regions at the chosen rates.  When visiting those regions on any server that is using the generated codes, players can find the chosen dinosaurs.  Behaviors and abilities are unchanged.

Prebuilt executables can be found in the "Dist" folder, and can be run from the Desktop or through the command line/terminal.

Interface: Command Prompt/Terminal

Supported DLCs:
- The Island
- The Center
- Scorched Earth
- Ragnarok
- Aberration
- Genesis
- Extinction
- Crystal Isles

Unsupported DLCs:
- None

Code is written in Python 3.  This is a work in progress, but is currently functional.
