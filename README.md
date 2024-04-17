
# Automatização de Quebra de Planilha Excel

Este script em Python utiliza a biblioteca Pandas para automatizar o processo de quebra de um grande arquivo
Excel em pedaços menores. Esse processo, que anteriormente levava mais de 4 horas para ser realizado
manualmente, agora pode ser concluído em poucos minutos com a execução deste código.

## Requisitos

Certifique-se de ter o Pandas instalado. Você pode instalá-lo executando o seguinte comando no terminal:


```bash
pip install pandas
```

## Uso

1. Baixe o arquivo Excel original que deseja dividir em pedaços menores e renomeie-o para `base.xlsx`. Certifique-se de que este arquivo esteja no mesmo diretório que o script Python.

2. Execute o script Python usando o seguinte comando no terminal:

```bash
python quebrar_planilha.py
```

## Funcionamento

1. O script lê o arquivo Excel original usando a função `pd.read_excel()` do Pandas.

2. Define o tamanho de cada pedaço menor (chunk) como 49999 linhas, embora isso possa ser ajustado conforme necessário.

3. Calcula o número total de chunks necessários com base no tamanho do DataFrame.

4. Itera sobre cada chunk, criando um arquivo Excel separado para cada pedaço. Os arquivos de saída são nomeados como `Padrão-{i}.xlsx`, onde `{i}` representa o número do chunk.

## Resultado

Após a execução do script, você encontrará vários arquivos Excel, cada um contendo uma parte do arquivo original dividido de acordo com o tamanho especificado.

