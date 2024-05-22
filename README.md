
<h1>FTP to Oracle Database ETL Script</h1>
Este repositório contém um script em Python desenvolvido para realizar a extração, transformação e carga (ETL) de dados de um servidor FTP para um banco de dados Oracle. O script foi criado com o intuito de aprimorar habilidades de programação.

<h3>Funcionalidades</h3>
<strong>Conexão com Servidor FTP:</strong> Acessa um servidor FTP público e navega até o diretório específico para localizar e baixar um arquivo ZIP.

<strong>Download e Extração de Arquivo:</strong> Baixa o arquivo ZIP contendo os dados e o extrai no diretório local.

<Strong>Processamento de Dados:</Strong> Lê o arquivo TXT extraído e processa suas linhas para preparação dos dados.

<Strong>Conexão com Banco de Dados Oracle:</Strong> Conecta-se a um banco de dados Oracle XE (ou qualquer outra versão Oracle preferida) utilizando o Oracle Instant Client.

<Strong>Inserção de Dados no Banco:</Strong> Insere os dados processados no banco de dados Oracle em uma tabela específica.
