# Exercícios HBase:

1. Criar a tabela dentro do Hbase
1. Criar um script python que:
    - Consulta o MySQL
    - Calcula o portfolio total do **usuário 1** no dia **12 de junho de 2020**. 
    - Fazer a exportação do cálculo em um CSV 
    - Importar no HBASE
1. Criar um shell script que execute este exercício com um único comando de terminal

> 💡 Tip: Fazer o Script Python na máquina Ubuntu, exceto a importação no HBASE.

> ⚠ Ainda não tenho certeza como será feita a importação do CSV na VM Cloudera.

## Acesso ao BD de preço de açoes

Execute o seguinte comando para criar o arquivo **.env**:

`cat .env.example > .env`

Contate o proprietário do Banco de Dados para obter os acessos.

## SQL
Criado por: Profº Fabrizio
```sql
select s.date_ as 'date',	
		p.shares, 
		p.symbol, 
		s.close, 
		ROUND(s.close * p.shares, 2) total
	from stockfgv.stocks s 
		INNER JOIN stockfgv.portfolio p 
			ON p.symbol = s.symbol 
		WHERE 
			s.date_ = '2020-06-12';
```

## HBase
`hbase shell`

Criar coluna usando o 'date' como rowkey:
`create 'portfolio','shares', 'symbol', 'close', 'total'`

`scan portfolio`

Importar CSV para o HDFS
`hdfs dfs -put file.csv / tmp`

Importar arquivo do HDFS para o HBase considerando o 'date' como rowkey:
```shell
hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=',' -Dimporttsv.columns=HBASE_ROW_KEY,shares,symbol,close,total portfolio /tmp/portfolio.csv
```
### Comandos HBase úteis
Disabilitar a tabela
`disable 'portfolio'`
Para "dropar" a tabela
`drop 'portfolio'`