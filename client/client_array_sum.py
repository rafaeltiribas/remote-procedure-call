import rpyc
import sys
import time

start = time.time()

if len(sys.argv) < 2:
    exit("Usage: python client.py SERVER_IP")

server_ip = sys.argv[1]

# Conexão sem timeout
conn = rpyc.connect(
    server_ip,
    18861,
    config={"sync_request_timeout": None}
)

n = int(input("Digite o tamanho do vetor: "))
vector = list(range(n))

result = conn.root.sum_vector(vector)

end = time.time()

print(f"A soma dos elementos do vetor é: {result}")
print(f"Tempo de execução no cliente: {end - start:.6f} segundos")
