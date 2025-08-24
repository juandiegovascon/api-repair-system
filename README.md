# 🚀 Repair System API

Una API en Python que simula un sistema de reparación de naves espaciales con tres endpoints principales.

## 📋 Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación y Ejecución

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar la API
```bash
python app.py
```

La API estará disponible en `http://localhost:5000`

## 📡 Endpoints

### 1. GET /status
Retorna un sistema averiado aleatorio en formato JSON.

**Ejemplo de respuesta:**
```json
{
  "damaged_system": "engines"
}
```

### 2. GET /repair-bay
Genera una página HTML con el código de reparación del sistema averiado.
El código se muestra en un `<div>` con la clase `anchor-point`.

**Ejemplo de respuesta HTML:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Repair</title>
</head>
<body>
<div class="anchor-point">ENG-04</div>
</body>
</html>
```

### 3. POST /teapot
Retorna un código de estado HTTP 418 (I'm a teapot).

## 🔧 Sistemas y Códigos de Reparación

| Sistema | Código |
|---------|--------|
| navigation | NAV-01 |
| communications | COM-02 |
| life_support | LIFE-03 |
| engines | ENG-04 |
| deflector_shield | SHLD-05 |

## 🔄 Flujo de Uso

1. **Llamar a `GET /status`** para obtener un sistema averiado
2. **Llamar a `GET /repair-bay`** para obtener el código de reparación
3. **Opcional:** Llamar a `POST /teapot` para el código 418

## 🌐 Hacer la API Pública

Para hacer la API accesible desde el exterior, puedes usar:

### Opción 1: ngrok (Recomendado para pruebas)
```bash
# Instalar ngrok
# Descargar desde https://ngrok.com/

# Ejecutar ngrok
ngrok http 5000
```

### Opción 2: Desplegar en un servidor
- Heroku
- Railway
- Render
- DigitalOcean
- AWS

## 🧪 Pruebas con Postman

### Colección de Postman
1. **GET /status**
   - Method: GET
   - URL: `http://localhost:5000/status`

2. **GET /repair-bay**
   - Method: GET
   - URL: `http://localhost:5000/repair-bay`

3. **POST /teapot**
   - Method: POST
   - URL: `http://localhost:5000/teapot`

## 📁 Estructura del Proyecto

```
api-repair-system/
├── app.py              # Archivo principal de la API
├── requirements.txt    # Dependencias de Python
└── README.md          # Este archivo
```

## 🎯 Características

- ✅ Endpoint `/status` que retorna sistema averiado aleatorio
- ✅ Endpoint `/repair-bay` que genera HTML con código de reparación
- ✅ Endpoint `/teapot` que retorna código HTTP 418
- ✅ Página de inicio con documentación
- ✅ Diseño moderno y responsive
- ✅ Código limpio y bien documentado
- ✅ Fácil de desplegar y configurar

## 🐛 Solución de Problemas

### Puerto 5000 ocupado
Si el puerto 5000 está ocupado, puedes cambiar el puerto en `app.py`:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

### Error de dependencias
Asegúrate de tener Python 3.7+ y ejecuta:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📞 Soporte

Para cualquier pregunta o problema, revisa la documentación o crea un issue en el repositorio.
