# StormGuard.ai — Paquete de despliegue

Este ZIP contiene únicamente los archivos de infraestructura y CI/CD generados en el chat.
El código de aplicación (app.py, paquete engine/ con SQLAlchemy, modelo ML y reglas de
política) NO está incluido porque no fue compartido en esta conversación.

## Qué falta completar antes de subir el repo
1. Colocar tu `app.py` real en la raíz del proyecto.
2. Colocar tu paquete `engine/` completo dentro de la carpeta `engine/` (se incluye vacía como placeholder).
3. Completar `requirements.txt` con las versiones exactas de tus dependencias.
4. Agregar tus tests de pytest (por ejemplo en una carpeta `tests/`) para que el paso
   `pytest -v` del workflow tenga algo que ejecutar.

## Archivos incluidos
- `Dockerfile`
- `render.yaml`
- `.github/workflows/deploy.yml`
- `.gitignore`
- `requirements.txt` (placeholder)
