from flask import Flask, jsonify, render_template_string
import random
import os

app = Flask(__name__)

# Sistemas disponibles y sus códigos de reparación
SYSTEMS = {
    "navigation": "NAV-01",
    "communications": "COM-02", 
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Variable global para almacenar el sistema averiado
damaged_system = None

@app.route('/status', methods=['GET'])
def get_status():
    """Primera llamada: GET /status - Retorna un sistema averiado aleatorio"""
    global damaged_system
    damaged_system = random.choice(list(SYSTEMS.keys()))
    
    return jsonify({
        "damaged_system": damaged_system
    })

@app.route('/repair-bay', methods=['GET'])
def get_repair_bay():
    """Segunda llamada: GET /repair-bay - Genera página HTML con código de reparación"""
    global damaged_system
    
    # Si no hay sistema averiado, generar uno
    if damaged_system is None:
        damaged_system = random.choice(list(SYSTEMS.keys()))
    
    # Obtener el código de reparación correspondiente
    repair_code = SYSTEMS.get(damaged_system, "UNKNOWN")
    
    # Plantilla HTML simplificada y corregida
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Repair</title>
</head>
<body>
<div class="anchor-point">{repair_code}</div>
</body>
</html>"""
    
    return html

@app.route('/teapot', methods=['GET', 'POST'])
def teapot():
    """Tercera llamada: GET/POST /teapot - Retorna código HTTP 418"""
    return "I'm a teapot", 418

@app.route('/')
def home():
    """Página de inicio con información de la API"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair System API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #1a1a1a;
                color: #ffffff;
                padding: 40px;
                line-height: 1.6;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: #2d2d2d;
                padding: 30px;
                border-radius: 10px;
                border: 1px solid #00ff00;
            }
            h1 {
                color: #00ff00;
                text-align: center;
            }
            .endpoint {
                background-color: #1a1a1a;
                padding: 15px;
                margin: 15px 0;
                border-radius: 5px;
                border-left: 4px solid #00ff00;
            }
            .method {
                color: #00ff00;
                font-weight: bold;
            }
            code {
                background-color: #333;
                padding: 2px 6px;
                border-radius: 3px;
                color: #00ff00;
            }
            .example {
                background-color: #1a1a1a;
                border: 1px solid #00ff00;
                border-radius: 5px;
                padding: 15px;
                margin: 10px 0;
            }
            .anchor-point {
                background-color: #2d2d2d;
                border: 2px solid #00ff00;
                border-radius: 10px;
                padding: 20px;
                font-size: 24px;
                font-weight: bold;
                color: #00ff00;
                text-align: center;
                min-width: 200px;
                box-shadow: 0 0 20px rgba(0, 255, 0, 0.3);
                display: inline-block;
            }
            .note {
                background-color: #2d2d2d;
                border: 1px solid #ffff00;
                border-radius: 5px;
                padding: 10px;
                margin: 10px 0;
                color: #ffff00;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Repair System API</h1>
            
            <div class="endpoint">
                <h3><span class="method">GET</span> /status</h3>
                <p>Primera llamada: Retorna un sistema averiado aleatorio en formato JSON.</p>
                <code>{"damaged_system": "engines"}</code>
            </div>
            
            <div class="endpoint">
                <h3><span class="method">GET</span> /repair-bay</h3>
                <p>Segunda llamada: Genera página HTML con el código de reparación del sistema averiado.</p>
                <p><strong>IMPORTANTE:</strong> El sistema averiado se mantiene anclado entre llamadas.</p>
                <p>El código se muestra en un &lt;div&gt; con clase "anchor-point".</p>
                
                <div class="example">
                    <h4>Ejemplo de respuesta HTML:</h4>
                    <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Repair&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div class="anchor-point"&gt;ENG-04&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
                    
                    <h4>Visualización:</h4>
                    <div class="anchor-point">ENG-04</div>
                </div>
            </div>
            
            <div class="endpoint">
                <h3><span class="method">GET/POST</span> /teapot</h3>
                <p>Tercera llamada: Retorna un código de estado HTTP 418 (I'm a teapot).</p>
                <div class="note">
                    <strong>💡 Nota:</strong> Este endpoint ahora acepta tanto GET como POST para facilitar las pruebas desde el navegador.
                </div>
            </div>
            
            <div class="endpoint">
                <h3>Sistemas y códigos de reparación:</h3>
                <table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
                    <tr style="border-bottom: 1px solid #00ff00;">
                        <th style="text-align: left; padding: 8px; color: #00ff00;">Sistema</th>
                        <th style="text-align: left; padding: 8px; color: #00ff00;">Código</th>
                    </tr>
                    <tr><td style="padding: 8px;">navigation</td><td style="padding: 8px; color: #00ff00;">NAV-01</td></tr>
                    <tr><td style="padding: 8px;">communications</td><td style="padding: 8px; color: #00ff00;">COM-02</td></tr>
                    <tr><td style="padding: 8px;">life_support</td><td style="padding: 8px; color: #00ff00;">LIFE-03</td></tr>
                    <tr><td style="padding: 8px;">engines</td><td style="padding: 8px; color: #00ff00;">ENG-04</td></tr>
                    <tr><td style="padding: 8px;">deflector_shield</td><td style="padding: 8px; color: #00ff00;">SHLD-05</td></tr>
                </table>
            </div>
            
            <div class="endpoint">
                <h3>Flujo de uso:</h3>
                <ol>
                    <li><strong>Primera llamada:</strong> <code>GET /status</code> → Obtiene sistema averiado</li>
                    <li><strong>Segunda llamada:</strong> <code>GET /repair-bay</code> → Genera HTML con código de reparación</li>
                    <li><strong>Tercera llamada:</strong> <code>GET/POST /teapot</code> → Retorna código HTTP 418</li>
                </ol>
                
                <div class="example">
                    <h4>Ejemplo de flujo:</h4>
                    <p><strong>1.</strong> GET /status → <code>{"damaged_system": "engines"}</code></p>
                    <p><strong>2.</strong> GET /repair-bay → HTML con <code>&lt;div class="anchor-point"&gt;ENG-04&lt;/div&gt;</code></p>
                    <p><strong>3.</strong> GET/POST /teapot → HTTP 418 "I'm a teapot"</p>
                </div>
            </div>
            
            <div class="endpoint">
                <h3>Características técnicas:</h3>
                <ul>
                    <li>✅ <strong>Sistema averiado anclado</strong> entre llamadas</li>
                    <li>✅ <strong>Clase "anchor-point"</strong> implementada correctamente</li>
                    <li>✅ <strong>HTML generado</strong> según especificación exacta</li>
                    <li>✅ <strong>Códigos de reparación</strong> mapeados correctamente</li>
                    <li>✅ <strong>Estado persistente</strong> durante la sesión</li>
                    <li>✅ <strong>Endpoint /teapot</strong> acepta GET y POST</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Obtener puerto de Railway o usar 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    
    print("🚀 Iniciando Repair System API Mejorada...")
    print("📡 Endpoints disponibles:")
    print("   GET  /status      - Primera llamada: Sistema averiado")
    print("   GET  /repair-bay  - Segunda llamada: HTML con código de reparación")
    print("   GET/POST /teapot  - Tercera llamada: Código HTTP 418")
    print("   GET  /            - Página de inicio con documentación")
    print("\n🔧 Características implementadas:")
    print("   ✅ Sistema averiado anclado entre llamadas")
    print("   ✅ Clase 'anchor-point' implementada")
    print("   ✅ HTML generado según especificación exacta")
    print("   ✅ Códigos de reparación mapeados correctamente")
    print("   ✅ Endpoint /teapot acepta GET y POST")
    print(f"\n🌐 La API estará disponible en: http://localhost:{port}")
    print("📱 Para hacer pública, usa Railway o similar")
    
    app.run(host='0.0.0.0', port=port, debug=False)
