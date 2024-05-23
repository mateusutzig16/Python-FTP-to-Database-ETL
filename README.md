
<h1>FTP to Oracle Database ETL Script</h1>
Este repositório contém um script em Python desenvolvido para realizar a extração, transformação e carga (ETL) de dados de um servidor FTP para um banco de dados Oracle. O script foi criado com o intuito de aprimorar habilidades de programação.

<h3>Funcionalidades</h3>
<strong>Conexão com Servidor FTP:</strong> Acessa um servidor FTP público e navega até o diretório específico para localizar e baixar um arquivo ZIP.

<strong>Download e Extração de Arquivo:</strong> Baixa o arquivo ZIP contendo os dados e o extrai no diretório local.

<Strong>Processamento de Dados:</Strong> Lê o arquivo TXT extraído e processa suas linhas para preparação dos dados.

<Strong>Conexão com Banco de Dados Oracle:</Strong> Conecta-se a um banco de dados Oracle XE (ou qualquer outra versão Oracle preferida) utilizando o Oracle Instant Client.

<Strong>Inserção de Dados no Banco:</Strong> Insere os dados processados no banco de dados Oracle em uma tabela específica.


------------------------------------------------------------------------------------------------------------------------------

<H2>ENGLISH - </H2>

This repository contains a Python script developed to perform the extraction, transformation, and loading (ETL) of data from an FTP server to an Oracle database. The script was created with the aim of enhancing programming skills.

<h3>Features</h3>
<strong>FTP Server Connection:</strong> Accesses a public FTP server and navigates to the specific directory to locate and download a ZIP file.

<strong>File Download and Extraction:</strong> Downloads the ZIP file containing the data and extracts it to the local directory.

<strong>Data Processing:</strong> Reads the extracted TXT file and processes its lines to prepare the data.

<strong>Oracle Database Connection:</strong> Connects to an Oracle XE database (or any other preferred Oracle version) using the Oracle Instant Client.

<strong>Data Insertion into the Database:</strong> Inserts the processed data into a specific table in the Oracle database.
