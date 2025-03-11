# 🚀 Desafio UiPath + Python: Extração e Análise de Preços da Amazon

## 📌 Objetivo
Criar um robô em **UiPath** que acesse a **Amazon**, extraia informações de produtos, processe os dados utilizando **Python** e exporte os resultados para uma planilha **Excel**.

## 📋 Descrição do Desafio
O robô deverá:
1. **Abrir o site da Amazon** e buscar um produto especificado.
2. **Extrair dados de uma lista de produtos**, incluindo:
   - Nome do produto
   - Preço
   - Avaliação (quantidade de estrelas)
   - Quantidade de reviews
   - Link do produto
3. **Salvar os dados extraídos em um arquivo CSV**.
4. **Usar Python para tratamento de dados**, incluindo:
   - Limpeza de valores nulos ou inconsistentes
   - Conversão de valores monetários para números
   - Cálculo do preço médio e avaliação média
5. **Exportar os dados processados para uma planilha Excel** organizada.
6. **Gerar um gráfico de distribuição de preços dos produtos**.

## 🛠️ Tecnologias Utilizadas
- **UiPath** (Web Scraping, manipulação de arquivos, integração com Python, Excel)
- **Python** (Pandas, Matplotlib para análise e visualização dos dados)
- **Excel** (Armazenamento dos dados processados)

## 🎯 Requisitos
- UiPath instalado (com **UiPath Python Activities Package**)
- Python 3.x instalado (com Pandas e Matplotlib)
- Conta na Amazon para acessar as páginas de produto

## 📝 Passo a Passo
### 1️⃣ Criar o fluxo no UiPath:
- Usar **Open Browser** para abrir a Amazon
- Utilizar **Type Into** para inserir o nome do produto na barra de pesquisa
- Usar **Click** para pressionar o botão de busca
- Utilizar **Data Scraping** para capturar os dados da página
- Salvar os dados em um arquivo **CSV**

### 2️⃣ Criar um script Python para processar os dados:
- Ler o arquivo CSV usando Pandas
- Remover linhas com valores nulos
- Converter preços para valores numéricos
- Calcular estatísticas (preço médio, avaliação média)
- Criar um gráfico de distribuição de preços
- Salvar os dados tratados em um arquivo **Excel**

### 3️⃣ Integrar o UiPath com Python:
- Utilizar **Invoke Python Method** para chamar o script Python
- Aguardar o processamento e recuperar os dados tratados
- Utilizar **Write Range** para salvar os dados no Excel

## 📊 Resultado Esperado
No final do desafio, você terá um arquivo Excel contendo:
1. **Lista de produtos extraídos da Amazon**
2. **Preço médio, avaliação média e outras estatísticas**
3. **Gráfico da distribuição de preços**

## 🔥 Desafio Extra
- Automatizar a extração de várias categorias de produtos.
- Implementar um alerta para notificar quando um produto estiver abaixo de um certo preço.
- Criar um bot que faça isso diariamente e envie relatórios por e-mail.

💡 **Boa sorte e bom aprendizado!** 🚀

