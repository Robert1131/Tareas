# Escritura de Archivo de Texto

# Abrimos (o creamos si no existe) el archivo 'my_notes.txt' en modo de escritura
with open('my_notes.txt', 'w') as file:
    # Escribimos las tres líneas de notas personales
    file.write("Soy Robert Reyes Neira, un estudiante de la Universidad Amazónica y estoy muy feliz de prepararme profesionalmente en esta prestigiosa universidad.\n")
    file.write("Estudio la carrera de Tecnologías de la Información y estoy muy feliz de la carrera que elegí.\n")
    file.write("Estoy orgulloso de poder formarme académicamente en la Universidad y más siguiendo esta hermosa carrera.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo 'my_notes.txt' en modo de lectura
with open('my_notes.txt', 'r') as file:
    # Leemos cada línea del archivo y la mostramos en la consola
    for line in file:
        print(line.strip())  # .strip() elimina los saltos de línea adicionales

# El uso de 'with' asegura que el archivo se cierre automáticamente después de realizar las operaciones.
