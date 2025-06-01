import re
import sys
import codecs

# Configurar la salida para UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Ejemplo de dataset: comentarios de la red social X
comments = [
    "¡Hola! 😊 ¿Cómo estás? Mira este enlace: https://example.com",
    "<p>Este es un comentario con HTML.</p>",
    "¡Genial! 😎 #BigData #Python",
    "Visita nuestro sitio web en http://www.example.org para más información.",
    "Texto limpio, sin emojis ni URLs."
]

def clean_text(text):
    # Eliminar etiquetas HTML
    text = re.sub(r'<.*?>', '', text)
    # Eliminar URLs
    text = re.sub(r'http[s]?://\S+', '', text)
    # Eliminar emojis y caracteres especiales
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Limpiar todos los comentarios
cleaned_comments = [clean_text(comment) for comment in comments]

# Mostrar resultados
print("Comentarios originales:")
for comment in comments:
    print(comment)

print("\nComentarios limpiados:")
for cleaned_comment in cleaned_comments:
    print(cleaned_comment)