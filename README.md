Nmap Vulnerability Parser

Descripción

Este repositorio alberga un script desarrollado en Python cuyo propósito es analizar archivos XML generados por Nmap, extrayendo información detallada sobre vulnerabilidades detectadas. Los datos extraídos se almacenan en un archivo CSV estructurado, lo que facilita su posterior inspección y correlación con otros conjuntos de información en evaluaciones de seguridad.

Este proyecto está orientado a profesionales emergentes en pruebas de penetración y a investigadores en ciberseguridad que deseen optimizar la interpretación de resultados obtenidos mediante escaneos de red.

Características

✅ Procesamiento de archivos XML de Nmap generados con el script "vuln"✅ Extracción sistemática de datos clave: direcciones IP, puertos, servicios y vulnerabilidades detectadas✅ Almacenamiento estructurado en formato CSV, facilitando el análisis automatizado y la correlación de hallazgos✅ Manejo robusto de excepciones y validaciones de entrada, garantizando la integridad de los datos procesados✅ Interfaz de línea de comandos (CLI) intuitiva, permitiendo una configuración flexible de los archivos de entrada y salida

Requisitos

Python 3.x

Biblioteca xml.etree.ElementTree (incluida en la distribución estándar de Python)

Instalación y Uso

1️⃣ Clonar el repositorio

git clone https://github.com/tuusuario/nmap-vuln-parser.git
cd nmap-vuln-parser

2️⃣ Ejecutar el script

python3 parse_nmap_vulns.py -i data/vulnerabilidades.xml -o data/nmap_vulnerabilities.csv

3️⃣ Inspeccionar los resultados

El archivo CSV resultante se almacenará en data/nmap_vulnerabilities.csv y puede visualizarse mediante:

cat data/nmap_vulnerabilities.csv


Contribuciones

Las mejoras y optimizaciones son bienvenidas. Si deseas contribuir, puedes realizar un fork del repositorio, implementar tus modificaciones y enviar una pull request para su revisión.

Contacto

💼 LinkedIn: Domingo José Juan César 
📧 Email: domingojosejuancesar@gmail.com🐦 

Si consideras este proyecto útil, ¡no dudes en otorgarle una estrella en GitHub!
