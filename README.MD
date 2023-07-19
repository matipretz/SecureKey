<p align="center">
  <h1 align="center">SecureKey</h1>
</p>

1. [Introducción](#introducción)
2. [Descripción](#descripción)
   - [Funcionalidad](#funcionalidad)
   - [Contenido por paquetes](#contenido-por-paquetes)
   - [Librerías](#librerías)
   - [Documentación](#documentación)
   - [Ejecución y compilación](#ejecución-y-compilación)
3. [Ayuda](#ayuda)
4. [Autor](#autor)
5. [Historial de versiones](#historial-de-versiones)
6. [Licencia](#licencia)
7. [Roadmap](#roadmap)

## Introducción

SecureKey es una aplicación de gestión de contraseñas que te permite almacenar y proteger tus contraseñas de forma segura.

Con SecureKey , puedes crear, editar, eliminar y acceder a tus contraseñas de manera conveniente y segura.

La aplicación utiliza algoritmos de cifrado avanzados para proteger tus contraseñas y garantizar la confidencialidad de tus datos.  

## Descripción
Repositorio para el Trabajo Final Integrador de Codo 4.0 (2023) comison 23438 Java Inicial.  

Gestor de contraseñas en Java basado en passtorage (https://github.com/matipretz/passtorage)  

### Funcionalidad

1.  Al ejecutar el programa, se muestra un mensaje de bienvenida con información relevante y se carga el sistema.

2.  El usuario puede crear una cuenta nueva si aún no tiene una o puede iniciar sesión con una cuenta existente.

3.  Una vez que el usuario ha iniciado sesión, se le presenta un menú principal con opciones para crear, mostar, editar y eliminar contraseñas, o salir del programa.

4.  Al seleccionar la opción de crear contraseñas, se solicita el nombre y la contraseña, la que se encripta y guarda en la cuenta del usuario.

5.  Al seleccionar la opción de mostrar contraseñas, se muestran todas las contraseñas almacenadas en la cuenta del usuario.

6.  Al seleccionar la opción de editar contraseñas, se permite al usuario modificar las contraseñas almacenadas en su cuenta.

7.  Al seleccionar la opción de borrar contraseñas, se permite al usuario eliminar las contraseñas almacenadas en su cuenta.

8.  El usuario puede salir del programa seleccionando la opción correspondiente, devolviendolo a la pantalla de logueo.  

En resumen, "SecureKey " es una aplicación que brinda a los usuarios una forma conveniente de almacenar y acceder a sus contraseñas, evitando la necesidad de recordar múltiples contraseñas o anotarlas en lugares no seguros.

### Contenido por paquetes

* dist: Archivos de distribucion.
* docs: Documentación generada por javadoc.
* img: Repositorio de imagenes utilizadas por este archivo.
* src/paq: Codigo fuente

### Librerias

* java.io.File

* java.util.Base64

* java.util.List

* java.util.Scanner

* javax.crypto.Cipher

* javax.crypto.SecretKey

* javax.crypto.spec.SecretKeySpec

### Documentación
La documentación generada por javadoc puede consultarse en: [GitHub Pages](https://matipretz.github.io/SecureKey/)


### Ejecucion y compilacion

El paquete "dist" incluye un archivo de ejecucion por lotes "Run.bat" que ejecuta el programa en sistemas Windows.

Tambien se incluye la compilacion "SecureKey.jar".

El programa fue compilado bajo Java SE 17, por lo que debe correr bajo esa version o una superior.

Para saber qué versión de Java tienes instalada en tu sistema, puedes seguir estos pasos:

1.  Abre una ventana de línea de comandos (Terminal en macOS/Linux o Command Prompt en Windows).
    
2.  Escribe el siguiente comando y presiona Enter:

```
java -version
```
3.  Se mostrará la versión de Java instalada en tu sistema. La salida será similar a esto:
```
java version "17.0.6" 2023-01-17 LTS
Java(TM) SE Runtime Environment (build 17.0.6+9-LTS-190)
Java HotSpot(TM) 64-Bit Server VM (build 17.0.6+9-LTS-190, mixed mode, sharing)
```

## Ayuda
Se tiene conocimiento sobre posibles errores al escribir y leer datos encriptados relacionados con la imprementacion del algoritmo de cifrado. 
De presentarse este problema, desabilitar los mecanismos de cifrado y eliminar el contendio del directorio "data" es una forma de resolverlo.

## Autor

Matias Martin Murad Pretz (https://github.com/matipretz)

## Historial de versiones

* 0.2
Implementa criptografia.

* 0.1
Version inicial.  

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE.md para más detalles.

## Roadmap
En el futuro se planea incorporar llaves de incriptado dinamicas y metodos que soporten el cambio de llave sin perdida de datos. Si bien esto es complejo por que hacerlo implica desencriptar y reencriptar valiendose de un atributo de usuario todavia no implementado, no es imposible.

Si bien este programa se basa en una version sencilla y monousuario sin funcionalidades avanzadas como el acceso en linea desde multiples dispositivos, es desable para el futuro que se convierta en un servicio en la nube que permita sortear esta dificultad.
