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


## 📁 Estructura del Proyecto

```
api-repair-system/
├── app.py              # Archivo principal de la API
├── requirements.txt    # Dependencias de Python
└── README.md          # Este archivo
```

