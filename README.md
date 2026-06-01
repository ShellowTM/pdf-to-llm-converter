# PDF to LLM-Ready Markdown Converter 🚀

Este proyecto automatiza la conversión masiva o individual de archivos PDF a formato Markdown limpio, optimizado específicamente para Modelos de Lenguaje (LLMs) y sistemas RAG. 

Soluciona de raíz el problema de codificación de caracteres en Windows (Mojibake), garantizando que las tildes (`á, é, í...`) y las eñes (`ñ`) se guarden perfectamente en formato UTF-8.

## 🛠️ Características
- **Modo Híbrido**: Convierte un único archivo escribiendo su nombre o procesa directorios completos de forma automática si ejecutas el comando solo.
- **Formato Limpio**: Remueve ruido visual del PDF gracias al motor `markitdown` de Microsoft.
- **Codificación Segura**: Forzado nativo a `utf-8-sig` compatible con el Bloc de notas y scripts de IA.

## 🚀 Instalación rápida
1. Descarga los archivos de este repositorio.
2. Instala la dependencia necesaria en tu computadora:
   ```bash
   pip install markitdown
   ```

## 💻 Modo de uso en la Terminal
- **Procesar toda la carpeta actual**:
  ```bash
  reparar
  ```
- **Procesar un archivo específico**:
  ```bash
  reparar "mi_documento.pdf"
  ```
