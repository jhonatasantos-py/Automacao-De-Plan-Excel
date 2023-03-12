import pandas as pd

# Carregando o arquivo Excel
df = pd.read_excel('auto3.xlsx')

# Definindo o tamanho de cada planilha
chunk_size = 10000

# Calculando o número total de planilhas
num_chunks = int(len(df) / chunk_size) + 1

# Dividindo o arquivo em planilhas
for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, len(df))
    chunk = df[start_idx:end_idx]
    chunk.to_excel(f'promo50ecom_{i}.xls', index=False)