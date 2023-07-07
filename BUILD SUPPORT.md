# If you want to build the code with PyInstaller module:
The code can be build on Windows and Linux too, but you need to use the --add-data subcommand for customtkinter .json.
> If the path not working bellow user this command: pip show customtkinter, then at the end type \customtkinter;customtkinter!
### Windows:
```python -m PyInstaller --noconfirm --onedir --windowed --add-data "C:\Users\ !! YOUR USERNAME HERE !!\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\customtkinter;customtkinter" --add-data "C:\Users\ !! YOUR USERNAME HERE !!\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\pykakasi;pykakasi" --icon=Icon.ico --noconsole KanaRenshu.py```
READ! THE BUILD FOLDER MUST NEED TO CONTAIN THE BANNER.PNG, THEN THE PROGRAM WILL CRASH!!!
