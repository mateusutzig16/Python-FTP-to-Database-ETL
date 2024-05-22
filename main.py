from ftplib import FTP
import oracledb
import zipfile
import os


"""

- PARA A REALIZACAO DO PROGRAMA, FOI NECESSARIA CRIACAO DE UM BANCO DE DADOS ORACLE XE (OU UM OUTRO DE SUA PREFERENCIA).
    ESCOLHI O ORACLE POR JA TER FAMILIARIDADE COM AS FERRAMENTAS E A LINGUAGEM.

- ESSE PROGRAMA TEM O INTUITO UNICO E EXCLUSIVO DE AUXILIAR A DESENVOLVER E 
    APRIMORAR MINHAS HABILIDADES COMO PROGRAMADOR. PORÉM, A QUEM INTERESSAR, ESTÁ DISPONÍVEL.

- O SERVIDOR E OS DADOS UTILIZADOS ESTAO DISPONIVEIS DE FORMA GRATUITA A TODOS. (DADOS GOVERNAMENTAIS)

- LEMBRANDO QUE NÃO ME RESPONSABILIZO POR NENHUMA CONSEQUENCIA DE SEU USO.

- USE O ARQUIVO REQUIREMENTS.TXT QUE ACOMPANHA O PROGRAMA PARA OS MODULOS USADOS.


----------------------------------------------------
Desenvolvido por: Mateus Utzig.
Data: 22 de Maio de 2024.

Última Atualização: 22 de Maio de 2024.

linkedin: https://www.linkedin.com/in/mateus-utzig/
github: https://github.com/mateusutzig16
----------------------------------------------------


"""


#------------------------------------------------

filename = 'tgg_export_caepi.zip'
path = '/portal/fiscalizacao/seguranca-e-saude-no-trabalho/caepi/'

#ACESSANDO O SERVIDOR FTP E LOCALIZANDO O DIRETORIO ESPERADO
ftp = FTP('ftp.mtps.gov.br')
ftp.login()
ftp.cwd(path)

if not filename.lower() in ftp.nlst():
    print('Arquivo nao encontrado no diretorio, tente novamente as 20h!')
    exit()

#DOWNLOAD DO ARQUIVO .ZIP PARA O DIRETORIO LOCAL
ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)

#AGUARDANDO O ARQUIVO SER BAIXADO
while not os.path.exists(filename):
    continue

#EXTRAINDO ARQUIVO ZIP QUE FOI BAIXADO
with zipfile.ZipFile(filename, 'r') as zip:
    zip.extractall()

filename = 'tgg_export_caepi.txt' 

with open(filename, 'r') as txt:
    lines = txt.readlines()


#CONEXAO COM MEU BANCO DE DADOS LOCAL 
user = 'mati'
password = 'mati1234'
host = '192.168.0.112'
port = '1521'
service_name = 'xepdb1'

#DECLARO O LOCAL DO ORACLE INSTANT CLIENT (NECESSARIO PARA CONECTAR COM O BANCO DE DADOS USADO. PODE VARIAR DE ACORDO COM O SEU)
oracledb.init_oracle_client(lib_dir=r"C:\instantclient_21_13")

#AQUI REALIZO A CONEXAO COM O MESMO
try:
    connection = oracledb.connect(user=user, password=password,
                                    host=host,port=port,service_name=service_name)
except Exception as e:
    print('ERRO AO CONECTAR AO BANCO DE DADOS. SAINDO DO PROGRAMA')
    exit()   

#DECLARO A ABERTURA DO CURSOR PARA EXECUTAR O INSERT
cursor = connection.cursor()


#CONTADOR DE LINHAS
lineCount = 0

for line in lines:

    
    lineCount = lineCount + 1

    #COMO A PRIMEIRA LINHA EH O CABECALHO, PULO ELA
    if lineCount == 1:
        continue
    
    #DECLARACAO DE VARIAVEIS DE ACORDO COM OS PIPES E SUAS RESPECTIVAS COLUNAS (PODE-SE OBSERVAR NO ARQUIVO)
    nrRegistroCA = line.strip().split('|')[0]
    dataValidade = line.strip().split('|')[1]
    situacao = line.strip().split('|')[2]
    nrProcesso = line.strip().split('|')[3]
    cnpj = line.strip().split('|')[4]
    razaoSocial = line.strip().split('|')[5]
    natureza = line.strip().split('|')[6]
    nomeEquipamento = line.strip().split('|')[7]
    descricaoEquipamento = line.strip().split('|')[8]
    marcaCA = line.strip().split('|')[9]
    referencia = line.strip().split('|')[10]
    cor = line.strip().split('|')[11]
    aprovadoParaLaudo = line.strip().split('|')[12]
    restricaoLaudo = line.strip().split('|')[13]
    observacaoAnaliseLaudo = line.strip().split('|')[14]
    cnpjLaboratorio = line.strip().split('|')[15]
    razaoSocialLaboratorio = line.strip().split('|')[16]
    nrLaudo = line.strip().split('|')[17]
    norma = line.strip().split('|')[18]

    #INSERT NO BANCO DE DADOS
    insert_sql = """
    INSERT INTO P1_EPI (
        NRRegistroCA,
        DataValidade,
        Situacao,
        NRProcesso,
        CNPJ,
        RazaoSocial,
        Natureza,
        NomeEquipamento,
        DescricaoEquipamento,
        MarcaCA,
        Referencia,
        Cor,
        AprovadoParaLaudo,
        RestricaoLaudo,
        ObservacaoAnaliseLaudo,
        CNPJLaboratorio,
        RazaoSocialLaboratorio,
        NRLaudo,
        Norma
    ) VALUES (
        :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19
    )
    """
    cursor.execute(insert_sql, (
            nrRegistroCA, dataValidade, situacao, nrProcesso, cnpj, razaoSocial, natureza, 
            nomeEquipamento, descricaoEquipamento, marcaCA, referencia, cor, aprovadoParaLaudo, 
            restricaoLaudo, observacaoAnaliseLaudo, cnpjLaboratorio, razaoSocialLaboratorio, 
            nrLaudo, norma
        ))
    
    print(f'LINHA {lineCount} INSERIDA COM SUCESSO!')

print('TODOS OS REGISTROS FORAM INSERIDOS!')

#FECHO O CURSOR, COMMITO NO BANCO E ENCERRO A CONEXAO E O PROGRAMA.
cursor.close()
connection.commit()
connection.close()

exit()
    

