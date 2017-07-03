# processes_monitor

## instalación
en la carpeta del proyecto corra el siguiente comando:
`pip install -r requirements.txt`

luego, se debe correr los archivos cpu_handler y processes_handler, enviando las variables de entorno:

* `export MAX_CPU=15 OK_CPU=50 && python cpu_handler.py`
* `export MAX_MEM=60 && python memory_handler.py`
