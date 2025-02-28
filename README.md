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
git clone https://github.com/seu-repositorio/mobat.git
cd mobat
```

2. Instale as dependências:
```sh
pip install -r requirements.txt
```

3. Configure o MongoDB e inicie o serviço.
4. Execute o servidor FastAPI:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

5. Para visualizar a interface, acesse `http://localhost:8000`.

---

## Teste Mínimo

1. Certifique-se de que todas as dependências estão instaladas.
2. Execute o comando abaixo para testar a obtenção de dados de um IP suspeito:
```sh
python run_mobat.py --ip 8.8.8.8
```
3. Se a instalação estiver correta, a saída deverá conter informações sobre o IP, incluindo histórico e reputação.

---

## Experimentos

Os seguintes experimentos são fornecidos para validação das reivindicações do artigo:

### Reivindicação #1: Classificação de IPs
**Passos:**
1. Execute o script de análise de IPs:
```sh
python analyze_ips.py --dataset dataset.csv
```
2. Aguarde o processamento e visualize os gráficos gerados.
3. O tempo estimado de execução é de 2 minutos para 10.000 IPs.

### Reivindicação #2: Clustering de IPs Maliciosos
**Passos:**
1. Execute o script de clustering:
```sh
python clustering.py --clusters 5
```
2. Verifique os grupos de IPs formados.
3. O tempo estimado de execução é de 3 minutos para 15.000 IPs.

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

