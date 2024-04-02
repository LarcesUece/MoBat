import pandas as pd
import json
import re
import os

pd.set_option('future.no_silent_downcasting', True)

def processar_diretorio(diretorio, nome_arquivo_csv):
    dados_unificados = {}

    def extrair_arquivos_json(diretorio):
        for pasta_raiz, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                if arquivo.endswith('.json'):
                    caminho_arquivo_origem = os.path.join(pasta_raiz, arquivo)
                    with open(caminho_arquivo_origem, 'r') as file:
                        dados = json.load(file)
                        chave = os.path.splitext(arquivo)[0]  
                        if chave in dados_unificados:
                            count = 1
                            while chave + '_' + str(count) in dados_unificados:
                                count += 1
                            chave += '_' + str(count)
                        dados_unificados[chave] = dados

    extrair_arquivos_json(diretorio)

    dados_unificados = {str(k): v for k, v in dados_unificados.items()}

    df = pd.DataFrame.from_dict(dados_unificados, orient='index')

    ips = []
    horarios = []

    for indice in df.index:
        match = re.match(r'([\d.]+)[->_]+(\d{2}-\d{2}-\d{2})', indice)
        if match:
            ip, horario = match.groups()
        else:
            ip = indice
            horario = ''
        ips.append(ip)
        horarios.append(horario)

    df['IP'] = ips
    df['Horario'] = horarios

    if 'virustotal_last_analysis_stats' in df.columns:
        df['harmless'] = df['virustotal_last_analysis_stats'].apply(lambda x: x.get('harmless') if isinstance(x, dict) else None)
        df['malicious'] = df['virustotal_last_analysis_stats'].apply(lambda x: x.get('malicious') if isinstance(x, dict) else None)
        df['suspicious'] = df['virustotal_last_analysis_stats'].apply(lambda x: x.get('suspicious') if isinstance(x, dict) else None)
        df['undetected'] = df['virustotal_last_analysis_stats'].apply(lambda x: x.get('undetected') if isinstance(x, dict) else None)
        df['timeout'] = df['virustotal_last_analysis_stats'].apply(lambda x: x.get('timeout') if isinstance(x, dict) else None)

    df = df.drop(columns=['virustotal_last_analysis_stats'])

    for col in df.columns:
        if df[col].dtype == 'object' and 'ASNone' in df[col].values:
            df[col] = df[col].replace('ASNone', None)

    df['virustotal_asn'] = df['virustotal_asn'].apply(lambda x: 'AS' + str(int(float(x))) if isinstance(x, (int, float)) and not pd.isnull(x) else x)

    df = df[['IP', 'Horario'] + [col for col in df.columns if col not in ['IP', 'Horario']]]

    columns_to_replace_none = [
        'abuseipdb_confidence_score',
        'abuseipdb_total_reports',
        'abuseipdb_num_distinct_users',
        'virustotal_reputation',
        'harmless',
        'malicious',
        'suspicious',
        'undetected',
        'IBM_score',
        'IBM_average history Score',
        'IBM_most common score',
        'ALIENVAULT_reputation'
    ]

    df[columns_to_replace_none] = df[columns_to_replace_none].replace('None', None).infer_objects()
    df[columns_to_replace_none] = df[columns_to_replace_none].fillna(0).infer_objects()

    invert_columns = ['abuseipdb_confidence_score', 'undetected', 'malicious', 'suspicious']
    df[invert_columns] = 100 - df[invert_columns]

    numeric_columns = ['harmless', 'malicious', 'suspicious', 'undetected', 'IBM_score', 'virustotal_reputation', 'abuseipdb_confidence_score']
    df['score_average_Mobat'] = df[numeric_columns].replace('None', 0).astype(float).mean(axis=1, skipna=True)

    selected_columns = [
        'IP',
        'abuseipdb_is_whitelisted',
        'abuseipdb_confidence_score',
        'abuseipdb_country_code',
        'abuseipdb_isp',
        'abuseipdb_domain',
        'abuseipdb_total_reports',
        'abuseipdb_num_distinct_users',
        'abuseipdb_last_reported_at',
        'virustotal_reputation',
        'virustotal_regional_internet_registry',
        'virustotal_as_owner',
        'harmless',
        'malicious',
        'suspicious',
        'undetected',
        'IBM_score',
        'IBM_average history Score',
        'IBM_most common score',
        'virustotal_asn',
        'SHODAN_asn',
        'SHODAN_isp',
        'ALIENVAULT_reputation',
        'ALIENVAULT_asn',
        'score_average_Mobat'
    ]

    df = df[selected_columns]
    df['abuseipdb_is_whitelisted'] = df['abuseipdb_is_whitelisted'].replace({1: True, 0: False, "FALSO": False, "VERDADEIRO": True, "Falso": False, "Verdadeiro": True, "False": False, "True": True, "FALSE": False, "TRUE": True})
    csv_file = nome_arquivo_csv
    df['ALIENVAULT_reputation'] = df['ALIENVAULT_reputation'].apply(lambda x: "True" if x == 1 else "False")
    df.to_csv(csv_file, index=False, na_rep='None')

diretorios = [
    'JSON/April-May(2023)',
    'JSON/September-October-November(2023)',
    'JSON/January-February-March(2024)'
]
nomes_arquivos_csv = [
    'Seasons/PrimeiroSemestre.csv',
    'Seasons/SegundoSemestre.csv',
    'Seasons/TerceiroSemestre.csv'
]

for diretorio, nome_arquivo_csv in zip(diretorios, nomes_arquivos_csv):
    processar_diretorio(diretorio, nome_arquivo_csv)

dfs = [pd.read_csv(arquivo) for arquivo in nomes_arquivos_csv]

df_total = pd.concat(dfs)

arquivo_csv_total = 'Seasons/Total.csv'
df_total.to_csv(arquivo_csv_total, index=False)