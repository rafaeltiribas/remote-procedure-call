import rpyc
from rpyc.utils.server import ThreadedServer
import time

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # Remove o timeout da conexão
        conn._config.update({
            "sync_request_timeout": None
        })

    def exposed_sum_vector(self, vector):
        start = time.time()
        
        result = sum(vector)
        
        end = time.time()
        print(f"Tempo de execução no servidor: {end - start:.6f} segundos")
        return result

if __name__ == "__main__":
    server = ThreadedServer(MyService, port=18861, hostname="0.0.0.0")
    server.start()
