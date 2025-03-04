import xml.etree.ElementTree as ET
import csv

def parse_nmap_vulns(xml_file, output_csv):
    """
    Parsea un archivo XML de Nmap con el script "vuln" y extrae información sobre vulnerabilidades detectadas.
    Guarda los resultados en un archivo CSV.
    
    Parámetros:
    xml_file (str): Ruta del archivo XML de Nmap.
    output_csv (str): Ruta del archivo CSV de salida.
    """
    # Cargar el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    data = []  # Lista para almacenar la información extraída
    
    # Iterar sobre los hosts detectados en el escaneo
    for host in root.findall("host"):
        ip_address = host.find("address").attrib.get("addr")  # Obtener la dirección IP del host
        
        # Buscar los puertos abiertos en el host
        for port in host.findall("ports/port"):
            port_id = port.attrib.get("portid")  # Obtener el número de puerto
            service = port.find("service").attrib.get("name") if port.find("service") is not None else "Unknown"
            
            # Buscar vulnerabilidades asociadas al puerto
            for script in port.findall("script"):
                vuln_id = script.attrib.get("id")  # ID del script de vulnerabilidad
                vuln_output = script.attrib.get("output")  # Descripción de la vulnerabilidad
                
                data.append([ip_address, port_id, service, vuln_id, vuln_output])
    
    # Guardar los datos extraídos en un archivo CSV
    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP Address", "Port", "Service", "Vulnerability ID", "Description"])  # Encabezado del CSV
        writer.writerows(data)  # Escribir los datos extraídos
    print("Script ejecutado correctamente")
    print(f"Datos guardados en {output_csv}")

# Ejemplo de uso con un archivo XML de Nmap de ejemplo
parse_nmap_vulns("vulnerabilidades.xml", "nmap_vulnerabilities.csv")
