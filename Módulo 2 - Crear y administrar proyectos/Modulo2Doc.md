# Resolucion de kata del Módulo 2

En esta práctica se explica como generar un entorno virtual para poder trabajar de manera Aislada, esto con la finalidad de no afecta a los paquetes globales que se tengan instalados en el equipo.

## Crear un entorno virtual
Generaremos el entorno virtual mediante ``venv``, a continuación se detallan los pasos para dicho procedimiento.

Cabe mencionar que los pasos que aquí se describen fueron realizados en una computadora con sistema operativo Windows.

* Abrimos una consola 
* Ejecutar en la consola el siguiente comando: ``python3 -m venv env``

    ```
       python3 -m venv env 
    ```
* una vez ejecutado el comando nos crea una carpeta con nombre env tal como se muestra en la imagen.

![image](./assets/Comando1.jpg)

* una vez generada procedemos a la activación del entorno, para ello ejecutamos el comando ``env\bin\activate``

```
env\Scripts\activate
```
![image](./assets/Comando2.jpg)

