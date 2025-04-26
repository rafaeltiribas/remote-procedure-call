# Relatório do Projeto de RPC

## Divisão de Tarefas

- **Aluno 1**: Rafael Tiribás
- **Aluno 2**: Victor Filgueira

**Política de Divisão de Tarefas:**  
Não houve divisão formal de tarefas. Todo o trabalho foi realizado de maneira síncrona através de vídeo-chamadas no aplicativo Discord. Durante as sessões, todas as atividades foram feitas em conjunto, com a participação ativa dos membros, discutindo as soluções em tempo real e implementando o código.

---

## Abordagem de Comunicação Entre Máquinas

A comunicação entre cliente e servidor foi configurada utilizando o endereço IPv4 da máquina onde o servidor estava sendo executado.
O servidor rodou em um computador com sistema operacional Windows 11, conectado à rede local via cabo Ethernet, enquanto o cliente foi executado em um MacBook Air com chip M1, conectado à mesma rede via Wi-Fi.

Durante a execução, foi utilizado o IP do servidor para que o cliente pudesse estabelecer a conexão remota utilizando a biblioteca RPyC.
Não foi necessário realizar ajustes no firewall, pois as máquinas estavam na mesma rede local e a porta 18861 foi utilizada para o serviço. Essa configuração permitiu a comunicação direta entre as máquinas, possibilitando a execução remota dos procedimentos.

---

## Problemas Encontrados e Soluções

Durante o desenvolvimento, alguns problemas foram encontrados e corrigidos conforme descrito abaixo:

**Questão 1:**  
No início, ao tentar rodar o código, foi impresso no cliente uma mensagem de erro devido ao uso incorreto de um objeto para chamar os métodos. O erro ocorreu porque os métodos estavam sendo chamados através de `c.root` em vez de `conn.root`, o que gerou a falha na execução. O problema foi corrigido ajustando o código para usar corretamente `conn.root`.

**Questão 2:**  
Ao tentar executar o código do cliente, foi exibida a mensagem de erro: `"has no attribute 'get_question'"`. Isso aconteceu porque o método `get_question` não estava exposto corretamente no servidor. A solução foi renomear o método para `exposed_get_question` no lado do servidor, permitindo que ele fosse exposto e acessado remotamente pelo cliente.

**Questão 6:**  
Durante a execução em máquinas diferentes, o código gerava um erro de timeout devido ao tempo de execução maior quando comparado à execução local. Para resolver isso, foi necessário alterar o código do servidor, removendo o timeout de requisições. Essa mudança permitiu que o servidor pudesse lidar com requisições de maior duração, como aquelas associadas a vetores de grandes dimensões.

---

# Questões e Respostas

## Questão 1

**Explique o que foi impresso no cliente (máquinas diferentes).**

_Resposta:_  
No primeiro momento foi impresso no cliente a mensagem de erro pois a os métodos estavam sendo chamados pelo objeto errado, chamando através de c.root ao invés de conn.root. Após consertar este pequeno detalhe este foi o conteúdo impresso:

- <__main__.MyService object at 0x000002325C33AF90>
- 42
- 43

---

## Questão 2

**Explique o que foi impresso no cliente ao executar o código modificado na mesma máquina.**

_Resposta:_  
No primeiro momento foi impresso no cliente a mensagem de erro "has no atribute 'get_question'". Isto ocorreu pois o método get_question não estava exposto no lado do servidor. Para isso foi necessário alterar o nome do método para 'exposed_get_question' para expor está parte do código remotamente!

Após corrigir este erro, este foi o conteúdo impresso:

- Qual é a cor do cavalo branco de Napoleão?

---

## Questão 3

**Explique o que ocorreu ao implementar o programa que soma o vetor.**

_Resposta:_  
No programa desenvolvido, o cliente solicita ao usuário que informe o tamanho do vetor (`n`).  
Em seguida, é criado um vetor contendo `n` elementos, variando de `0` até `n-1`.  
Ou seja, se o usuário informou o valor `n = 4`, o vetor criado foi `[0, 1, 2, 3]`.

Este vetor é então enviado para o servidor utilizando o RPyC (Remote Python Call).  
No servidor, o procedimento remoto `sum_vector` recebe o vetor e calcula a soma dos seus elementos utilizando a função `sum()` do Python.

A operação realizada foi:

```
0 + 1 + 2 + 3 = 6
```

Assim, o servidor retorna o valor `6` para o cliente, que imprime o resultado na tela.

Portanto, o que ocorreu foi:
- O cliente criou o vetor `[0, 1, 2, 3]`.
- O cliente enviou este vetor para o servidor.
- O servidor somou os valores do vetor, obtendo `6`.
- O cliente recebeu e exibiu o resultado da soma.

O fluxo de comunicação entre cliente e servidor funcionou corretamente conforme o esperado.

---

## Questão 4

**Mostre o código do cliente e do servidor, incluindo a medição do tempo de execução.**

```python
# Código do cliente
import rpyc
import sys
import time

start = time.time()

if len(sys.argv) < 2:
    exit("Usage: python client.py SERVER_IP")

server_ip = sys.argv[1]

conn = rpyc.connect(server_ip, 18861)

n = int(input("Digite o tamanho do vetor: "))
vector = list(range(n))

result = conn.root.sum_vector(vector)

end = time.time()

print(f"A soma dos elementos do vetor é: {result}")
print(f"Tempo de execução no cliente: {end - start:.6f} segundos")
```

```python
# Código do servidor
import rpyc
from rpyc.utils.server import ThreadedServer
import time

class MyService(rpyc.Service):
    def exposed_sum_vector(self, vector):
        start = time.time()
        
        result = sum(vector)
        
        end = time.time()
        print(f"Tempo de execução no servidor: {end - start:.6f} segundos")
        return result

if __name__ == "__main__":
    server = ThreadedServer(MyService, port=18861, hostname="0.0.0.0")
    server.start()
```

---

## Questão 5

**Indique o tempo de execução no cliente e no servidor (máquinas iguais, n = 10000).**

Tempo de execução localmente:
- Cliente: 3,348211 segundos
- Servidor: 0,704899 segundos

## Questão 6

**Indique o tempo de execução no cliente e no servidor (máquinas diferentes, n = 10000).**

Para esta execução em máquinas diferentes foi necessário fazer uma alteração no código do servidor para eliminar o timeout de requisições. Foi necessário corrigir este erro nesta execução pois o tempo de execução dos procedimentos é consideravelmente maior remotamente do que na mesma máquina localmente.

Tempo de execução remotamente:
- Cliente: 67,524445 segundos
- Servidor: 64,688425 segundos

```python
# Novo Código do cliente
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
```

```python
# Novo Código do servidor
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
```

---

## Questão 7

**Existe diferença nos tempos obtidos? Explique a razão.**

_Resposta:_  
Existe uma diferença significativa nos tempos de execução entre a execução local e a execução remota.

- **Na execução local**, o tempo do cliente (3,35 segundos) e o tempo do servidor (0,70 segundos) são relativamente pequenos. Isso ocorre porque a comunicação entre cliente e servidor acontece dentro da mesma máquina, sem necessidade de transmissão de dados pela rede. A troca de dados é muito rápida e praticamente instantânea.

- **Na execução remota**, o tempo do cliente (67,52 segundos) e do servidor (64,68 segundos) são muito maiores. Isso acontece porque agora os dados precisam ser enviados pela rede entre duas máquinas diferentes. Como o vetor é grande (10.000 elementos), o tempo de transmissão dos dados (upload e download) influencia muito no tempo total. A comunicação pela rede gera latência, e dependendo da qualidade da conexão (Wi-Fi, Ethernet, velocidade da internet, etc.), o tempo pode aumentar ainda mais.

**Em resumo:**  
- A diferença existe devido ao custo da comunicação pela rede.  
- Quando cliente e servidor estão na mesma máquina, não há latência de rede.  
- Quando estão em máquinas diferentes, além do tempo de processamento, o tempo de transmissão dos dados influencia muito no tempo total de execução.

---

## Questão 8

**Tabela: Tempo de execução na mesma máquina para n = {100, 1000, 10000}**

| n    | Tempo Servidor | Tempo Cliente |
|------|-------------------|-------------------|
| 100  | 0.007578          | 1.314485       |
| 1000 | 0.071109      | 2.956589       |
| 10000| 0.712162        | 3.416994       |

**Observação:**

_Resposta:_  
É possível observar que o tempo aumenta gradativamente conforme o tamanho da entrada n é incrementada.

---

## Questão 9

**Tabela: Tempo de execução em máquinas diferentes para n = {100, 1000, 10000}**

| n    | Tempo Servidor | Tempo Cliente |
|------|-------------------|-------------------|
| 100  | 0.747229          | 2.810256         |
| 1000 | 6.827894            | 9.721219         |
| 10000| 67.828574           | 70.566986           |

**Observação:**

_Resposta:_  
O tempo de execução cresce de maneira exponencial comparado à execução local.

---

## Questão 10

**Compare as duas tabelas. Existem diferenças? Explique.**

_Resposta:_  
Existem diferenças claras entre a execução local e a execução remota.

| Execução   | Tempo Servidor (n=10000) | Tempo Cliente (n=10000) |
|------------|-------------------------|--------------------------|
| **Local**  | 0,71 s                   | 3,41 s                   |
| **Remoto** | 67,82 s                  | 70,57 s                  |

### Principais diferenças:

- **Localmente**, a diferença entre os tempos do cliente e do servidor é pequena (milissegundos) e cresce de forma quase linear conforme aumentamos `n`.
- **Remotamente**, o tempo cresce de forma exponencial com o aumento de `n`.
  - Para `n=10000`, o tempo do cliente é quase **100x maior** que o tempo local.
  - Isso acontece porque o tempo inclui:
    - Tempo de envio do vetor (via rede)
    - Tempo de processamento no servidor
    - Tempo de retorno do resultado para o cliente

### Explicação:

1. **Atraso de rede (latência):**
   - Quando o cliente e servidor estão em máquinas diferentes, há uma "fila" para envio e recebimento de dados (latência).
   - Mesmo que o servidor processe rápido, o cliente precisa esperar toda a comunicação terminar.

2. **Tamanho do vetor:**
   - Ao aumentar `n`, o vetor se torna maior, o que impacta:
     - **Upload**: Cliente precisa enviar mais dados.
     - **Download**: Cliente precisa receber mais dados.
   - Isso justifica o tempo aumentar drasticamente para `n=10000` no ambiente remoto.

3. **Wi-Fi vs Ethernet:**
   - A máquina cliente estava conectada via Wi-Fi, enquanto o servidor estava via Ethernet.
   - O Wi-Fi normalmente é mais lento e sujeito a interferências, aumentando ainda mais o tempo de resposta.

### Conclusão:

- **Sim**, existem diferenças significativas entre os tempos locais e remotos.
- Essas diferenças são causadas principalmente pela **latência** e pela **transmissão de dados** na rede.
- Localmente, o tempo é dominado pelo processamento.
- Remotamente, o tempo é dominado pelo custo de transmissão dos dados.

---

# Detalhes das Execuções

- **Número de execuções realizadas para medição de tempo**: 50

---

# Observações Finais

Este trabalho permitiu entender a comunicação remota entre cliente e servidor utilizando RPyC. Foi interessante observar as diferenças de tempo de resposta entre a execução local e remota, o que nos proporcionou uma visão prática dos desafios em sistemas distribuídos.
