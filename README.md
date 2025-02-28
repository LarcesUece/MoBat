# MoBat

## Resumo

MoBat (Monitoramento e Análise de Dados de Bases de Ameaças) é uma ferramenta de Threat Intelligence projetada para coletar e analisar automaticamente dados de diversas bases de ameaças, incluindo VirusTotal, AbuseIPDB, Shodan, IBM X-Force e AlienVault. O objetivo principal do MoBat é fornecer indicadores valiosos sobre IPs e domínios suspeitos, permitindo que empresas e instituições se mantenham informadas sobre ameaças emergentes.

O MoBat utiliza tecnologias modernas como FastAPI para construção de APIs, Seaborn para visualização de dados, Scikit-learn para seleção de características e aprendizado de máquina, além de Docker para implantação da infraestrutura. O banco de dados utilizado é o MongoDB, enquanto o Nginx gerencia as requisições HTTP, e o Celery processa tarefas assíncronas.

Por meio de análises detalhadas de desempenho, o MoBat demonstrou eficácia na manipulação de grandes volumes de dados, garantindo respostas rápidas para profissionais de segurança cibernética. A ferramenta oferece gráficos de comportamento, mapeamento de características, agrupamento de dados (clustering), avaliação de modelos de aprendizado de máquina e visualização da reputação de IPs por país.

---

## Estrutura do README.md

1. **Resumo**
2. **Estrutura do repositório**
3. **Selos Considerados**
4. **Informações básicas**
5. **Dependências**
6. **Preocupações com segurança**
7. **Instalação**
8. **Teste mínimo**
9. **Experimentos**
10. **Licença**

---

## Selos Considerados

Os selos considerados para avaliação do artefato são:
- **Artefatos Disponíveis (SeloD)**
- **Artefatos Funcionais (SeloF)**
- **Artefatos Sustentáveis (SeloS)**
- **Experimentos Reprodutíveis (SeloR)**

---

## Informações Básicas

### Requisitos de hardware:
- Processador: Intel i5 ou superior
- Memória RAM: Mínimo de 8GB
- Armazenamento: Mínimo de 20GB de espaço disponível
- Sistema Operacional: Linux (Ubuntu 20.04+), Windows 10+, macOS 12+

### Requisitos de software:
- Python 3.12+
- Docker e Docker Compose
- MongoDB
- Nginx
- FastAPI
- Celery

---

## Dependências

MoBat utiliza diversas bibliotecas e pacotes para sua execução. As principais dependências incluem:
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Seaborn
- Tkinter
- Geopandas
- Pytz
- JSON
- Regular Expressions (re)
- Pycountry
- Time

Para instalar todas as dependências necessárias, utilize:
```sh
pip install -r requirements.txt
```

---

## Preocupações com Segurança

A execução do artefato pode envolver a manipulação de dados sensíveis sobre ameaças cibernéticas. Para mitigar riscos:
- O uso da ferramenta deve ser restrito a ambientes de teste e pesquisa.
- Recomenda-se que a execução ocorra em redes isoladas ou máquinas virtuais.
- Evitar o uso de credenciais públicas ao acessar APIs de terceiros.

---

## Instalação

Para instalar e configurar o MoBat, siga os passos abaixo:

1. Clone o repositório:
```sh
git clone https://github.com/LarcesUece/MoBat.git
cd Mobat
```

2. Crie um ambiente virtual
```sh
python3 -m venv venv
```

3. Ativar o ambiente virtual:
```sh
source venv/bin/activate
```

4. Instale as dependências:
```sh
pip install -r requirements.txt
```

5. Configure o ambiente virtual ao vscode.

6. Entre na pasta /Ferramenta_MoBAt:
```sh
cd Ferramenta_MoBAt
```

7. Execute o código Monitoring.py:
```sh
python3 Monitoring.py
```
---

## Teste Mínimo

1. Certifique-se de que todas as dependências estão instaladas.
```sh
pip list
```
2. Execute o comando abaixo para testar a exibição das tabelas de dados coletados e iniciar a interface de análise:
```sh
python3 Monitoring.py
```
3. Se a instalação estiver correta, o menu de seleção de tabelas será exibido, permitindo a escolha de períodos de coleta de dados. Para validar a funcionalidade básica:
   + Selecione a opção "4" para carregar todos os dados coletados.
   + Escolha a opção "1" para visualizar os gráficos de comportamento de um IP.
   + Insira um IP listado para análise.
4. Se tudo estiver configurado corretamente, a saída deverá conter gráficos e informações detalhadas sobre o comportamento do IP.
---

## Experimentos

Os seguintes experimentos são fornecidos para validação das reivindicações do artigo:

### Reivindicação #1: Análise de Comportamento de IPs
**Passos:**
1. Execute o script principal:
```sh
python3 Monitoring.py
```
2. Escolha uma das tabelas de dados disponíveis:
    + Abril-Maio (2023)
    + Setembro-Novembro (2023)
    + Janeiro-Março (2024)
    + Total Coletado
3. Selecione a opção "1" para visualizar os gráficos de comportamento de um IP específico.
4. Escolha um IP da lista fornecida.
5. Verifique os gráficos gerados, incluindo:
    + Localização geográfica do IP.
    + Quantidade de reports ao longo do tempo.
    + Score médio do IP em diferentes fontes de dados (AbuseIPDB, IBM, VirusTotal).
    + Horários com maior atividade suspeita.

### Reivindicação #2: Clustering de IPs Maliciosos
**Passos:**
1. Execute o script principal:
```sh
python3 Monitoring.py
```
2. Escolha a tabela de dados desejada.
3. Selecione a opção "3" para realizar análise de clusters.
4. Escolha a feature a ser utilizada como base para o agrupamento.
5. Defina a quantidade de clusters desejada.
6. Visualize os resultados nos gráficos gerados.
7. (Opcional) Escolha salvar os clusters gerados em um arquivo Excel.

### Reivindicação #3: Mapeamento de Características dos Dados
**Passos:**
1. Execute o script principal:
```sh
python3 Monitoring.py
```
2. Escolha a tabela de dados desejada.
3. Selecione a opção "2" para visualizar o mapeamento das features.
4. Examine os gráficos gerados mostrando a distribuição das características.
5. (Opcional) Escolha salvar um arquivo Excel com os mapeamentos.

### Reivindicação #4: Heatmap de Ocorrências por País
**Passos:**
1. Execute o script principal:
```sh
python3 Monitoring.py
```
2. Escolha a tabela de dados desejada.
3. Selecione a opção "9" para visualizar o heatmap de ocorrências por país.
4. Verifique o mapa gerado, onde as cores indicam a frequência de reports.
---

## Licença

Este projeto é licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo LICENSE.

---

## Equipe do Projeto

**Coordenador:**
- Rafael Lopes Gomes - [Lattes](http://lattes.cnpq.br/5212299313885086)

**Back-end e Data Analysts:**
- Yago Melo da Costa - [Lattes](http://lattes.cnpq.br/0381069814979157)
- Davi Oliveira - [Lattes](http://lattes.cnpq.br/6275027161080881)
- Ramon Araújo - [Lattes](http://lattes.cnpq.br/4482457290815759)
- Lyedson Silva - [Lattes](http://lattes.cnpq.br/6321492413240258)
- Francisco Nobre - [Lattes](http://lattes.cnpq.br/8242344331454843)

