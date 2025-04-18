import requests

def buscar_salario_api(vaga, empresa=""):
    try:
        url = "https://api-salario.onrender.com/prever_salario"
        payload = {"vaga": vaga, "empresa": empresa}
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            resultado = response.json()
            salario = resultado.get("salario_base_medio", None)
            if salario:
                return round(salario, 2)
        return None
    except:
        return None
    
print(buscar_salario_api("Analista de Dados"))
