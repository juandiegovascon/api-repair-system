#!/usr/bin/env python3
"""
Script de prueba para la Repair System API
Ejecuta este script para probar todos los endpoints
"""

import requests
import json
import time

# URL base de la API
BASE_URL = "http://localhost:5000"

def test_status_endpoint():
    """Prueba el endpoint /status"""
    print("🧪 Probando GET /status...")
    try:
        response = requests.get(f"{BASE_URL}/status")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Éxito: {data}")
            return data.get("damaged_system")
        else:
            print(f"❌ Error: Status code {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar a la API. ¿Está ejecutándose?")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None

def test_repair_bay_endpoint():
    """Prueba el endpoint /repair-bay"""
    print("🧪 Probando GET /repair-bay...")
    try:
        response = requests.get(f"{BASE_URL}/repair-bay")
        if response.status_code == 200:
            print("✅ Éxito: Página HTML generada")
            # Verificar que contiene la clase anchor-point
            if "anchor-point" in response.text:
                print("✅ Verificado: Contiene div con clase 'anchor-point'")
                # Extraer el código de reparación
                import re
                match = re.search(r'<div class="anchor-point">([^<]+)</div>', response.text)
                if match:
                    print(f"✅ Código de reparación: {match.group(1)}")
                else:
                    print("⚠️  No se pudo extraer el código de reparación")
            else:
                print("❌ Error: No contiene div con clase 'anchor-point'")
        else:
            print(f"❌ Error: Status code {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_teapot_endpoint():
    """Prueba el endpoint /teapot"""
    print("🧪 Probando POST /teapot...")
    try:
        response = requests.post(f"{BASE_URL}/teapot")
        if response.status_code == 418:
            print("✅ Éxito: Código HTTP 418 (I'm a teapot)")
            print(f"   Respuesta: {response.text}")
        else:
            print(f"❌ Error: Status code {response.status_code}, esperado 418")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_home_endpoint():
    """Prueba el endpoint raíz /"""
    print("🧪 Probando GET /...")
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("✅ Éxito: Página de inicio cargada")
            if "Repair System API" in response.text:
                print("✅ Verificado: Contiene título de la API")
            else:
                print("⚠️  Advertencia: No contiene el título esperado")
        else:
            print(f"❌ Error: Status code {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Función principal de pruebas"""
    print("🚀 Iniciando pruebas de la Repair System API")
    print("=" * 50)
    
    # Verificar que la API esté ejecutándose
    print("🔍 Verificando conexión con la API...")
    try:
        response = requests.get(BASE_URL, timeout=5)
        print("✅ API está ejecutándose")
    except requests.exceptions.ConnectionError:
        print("❌ No se puede conectar a la API")
        print("💡 Asegúrate de ejecutar 'python app.py' en otra terminal")
        return
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return
    
    print("\n" + "=" * 50)
    
    # Ejecutar todas las pruebas
    test_home_endpoint()
    print()
    
    test_status_endpoint()
    print()
    
    test_repair_bay_endpoint()
    print()
    
    test_teapot_endpoint()
    print()
    
    print("=" * 50)
    print("🎉 Pruebas completadas!")
    print("\n💡 Para probar manualmente:")
    print(f"   🌐 Abre tu navegador en: {BASE_URL}")
    print("   📱 Usa Postman o similar para probar los endpoints")
    print("   🔧 Verifica que cada llamada funcione según lo esperado")

if __name__ == "__main__":
    main()
