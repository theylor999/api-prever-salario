# 🔮 Previsão Salarial com Machine Learning

Este projeto utiliza Machine Learning para prever o salário base médio de uma vaga de emprego no Brasil, considerando o nome da vaga, a empresa e a senioridade.

## 📊 Como foi feito

1. **Coleta de Dados**  
   Realizei web scraping e consumo de APIs para coletar os salários que funcionários informaram voluntariamente no site Glassdoor.
   Foram obtidos dados de mais de **74 mil cargos de 3382 empresas** em diferentes regiões do Brasil.

3. **Limpeza e Processamento**  
   Os dados foram tratados com Pandas para padronizar nomes de cargos e empresas, extrair informações de **senioridade** (como Júnior, Pleno, Sênior, etc.) e remover inconsistências.

4. **Treinamento do Modelo**  
   Com os dados limpos, treinei modelos de Ridge Regression específicos para cada nível de senioridade, além de um modelo geral para casos em que a senioridade não é identificada. Utilizei o Scikit-Learn para prever o salário com base nas seguintes variáveis:
   - Nome da vaga
   - Nome da empresa
   - Senioridade

5. **API com FastAPI**  
   Criei uma API usando **FastAPI** para servir o modelo em produção. A API recebe os dados de entrada via `POST` e retorna a previsão salarial.

      🔸 **Importante:** a **senioridade deve ser incluída no nome da vaga** (ex: `"Analista de Dados Pleno"`), pois a API faz o **processamento automático** e separa internamente a senioridade do nome do cargo.

6. **Deploy**  
   A API foi publicada via [Render](https://render.com) e o site demo com front-end foi implementado em [https://prever-salarios.vercel.app](https://prever-salarios.vercel.app).

---

## 🧪 Exemplo de uso da API com Python

Você pode consultar a API diretamente com um código simples em Python:

```python
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
    
print(buscar_salario_api("Analista de Dados Pleno"))
