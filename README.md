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

## 5. Rotinas com base na análise de dados

- **Análise Descritiva:** Entender o que aconteceu nos dados.

  - Rotina 1 - Estatísticas Básicas: Calcular a média, mediana, e outros números importantes para ver como os tipos de ocorrências e os danos às aeronaves se distribuem.
  - Rotina 2 - Distribuição Regional: Criar gráficos para mostrar em quais estados e cidades ocorreram mais incidentes.

- **Análise Diagnóstica:** Descobrir por que os eventos aconteceram.

  - Rotina 1 - Investigação de Causas: Verificar se há alguma relação entre o tipo de ocorrência e as características das aeronaves, como o fabricante ou modelo.
  - Rotina 2 - Análise de Picos: Analisar os momentos em que houve mais ou menos incidentes ao longo do tempo e ver se há relação com eventos externos, como mudanças nas regras ou condições climáticas.

- **Análise Preditiva:** Prever o que pode acontecer no futuro.

  - Rotina 1 - Previsão de Ocorrências: Usar modelos de previsão para estimar quantos incidentes podem ocorrer no futuro, com base em características como o ano de fabricação da aeronave e seu peso.
  - Rotina 2 - Tendências Futuras: Aplicar modelos para prever se o número de incidentes em determinadas regiões vai aumentar ou diminuir nos próximos meses ou anos.

- **Análise Prescritiva** Sugerir ações para melhorar os resultados futuros.

  - Rotina 1 - Recomendações de Manutenção: Sugerir ciclos de manutenção para aeronaves que têm maior probabilidade de falhas, com base nas previsões.
  - Rotina 2 - Alocação de Recursos: Indicar onde é melhor investir em segurança ou treinamento para reduzir o risco de futuros incidentes.


