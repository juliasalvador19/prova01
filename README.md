# Projeto de Análise de Acidentes e Incidentes Aeronáuticos no Brasil

Este projeto visa a análise de dados de acidentes e incidentes aeronáuticos no Brasil utilizando uma base de dados disponível em formato `.xlsx`.

## 1. Base de Dados

A base de dados escolhida contém informações detalhadas sobre acidentes e incidentes aeronáuticos no Brasil. O arquivo pode ser encontrado na pasta `/data/`.

### 2. Classificação das colunas conforme modelo multidimensional (4W1H):
- **Who (Quem):**
  - `aeronave_fabricante`
  - `aeronave_modelo`
  - `aeronave_segmento_aviacao`
- **What (O quê):**
  - `ocorrencia_tipo`
  - `ocorrencia_classificacao`
  - `aeronave_equipamento`
  - `aeronave_nivel_dano`
- **Where (Onde):**
  - `ocorrencia_cidade`
  - `ocorrencia_uf`
- **When (Quando):**
  - `ocorrencia_dia`
  - `aeronave_ano_fabricacao`
- **How (Como):**
  - `aeronave_quantidade_motores`
  - `aeronave_peso_maximo_decolagem`
  - `aeronave_valor`

## 3. Implementação de Cubo de Dados

Foi implementado um cubo de dados conforme a base escolhida.

## 4. Tipos de Visualizações

Os quatro tipos de visualizações foram implementados e podem ser visualizados facilmente, no entanto, o Gráfico de Dispersão só aparecerá se houver pelo menos duas medidas e o Gráfico de Bolhas caso haja três medidas.

