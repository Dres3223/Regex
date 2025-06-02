import re

# Ejemplo de dataset: texto con correos electrónicos
dataset = [
    "Puedes contactarme en juan.perez@example.com para más información.",
    "Mi correo alternativo es maria_gomez123@domain.org.",
    "No olvides enviar el reporte a soporte@empresa.com antes del viernes.",
    "Este texto no contiene correos electrónicos.",
    "Otro ejemplo: contacto@miweb.net."
]

def extract_emails(text):
    # Expresión regular para detectar correos electrónicos
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    # Buscar todos los correos electrónicos en el texto
    return re.findall(email_pattern, text)

# Detectar correos electrónicos en el dataset
emails_detected = [extract_emails(entry) for entry in dataset]

# Mostrar resultados
print("Correos electrónicos detectados:")
for i, emails in enumerate(emails_detected):
    print(f"Texto {i + 1}: {emails}")