# Relatório do Projeto de RPC

## Divisão de Tarefas

- **Aluno 1**: Rafael Tiribás
- **Aluno 2**: Vitor

**Política de Divisão de Tarefas:**  
[Descrever brevemente como as tarefas foram divididas entre os membros.]

---

## Abordagem de Comunicação Entre Máquinas

[Explicar como foi configurada a comunicação entre cliente e servidor em máquinas diferentes (por exemplo, uso de IP, ajustes de firewall, etc.)]

---

## Problemas Encontrados e Soluções

[Listar problemas enfrentados e como foram resolvidos.]

---

# Questões e Respostas

## Questão 1

**Explique o que foi impresso no cliente (máquinas diferentes).**

_Resposta:_  
No primeiro momento foi impresso no cliente a mensagem de erro pois a os métodos estavam sendo chamados pelo objeto errado, chamando através de c.root ao invés de conn.root. Após consertar este pequeno detalhe este foi o conteúdo impresso:

Após corrigir este erro, este foi o conteúdo impresso:
[imagem]

---

## Questão 2

**Explique o que foi impresso no cliente ao executar o código modificado na mesma máquina.**

_Resposta:_  
No primeiro momento foi impresso no cliente a mensagem de erro "has no atribute 'get_question'". Isto ocorreu pois o método get_question não estava exposto no lado do servidor. Para isso foi necessário alterar o nome do método para 'exposed_get_question' para expor está parte do código remotamente!

Após corrigir este erro, este foi o conteúdo impresso:
[imagem]
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
[Cole aqui o client.py]
```

```python
# Código do servidor
[Cole aqui o server.py]
```

---

## Questão 5

**Indique o tempo de execução no cliente e no servidor (mesma máquina, n = 10000).**

- **Tempo de execução no cliente**: [tempo em segundos]
- **Tempo de execução no servidor**: [tempo em segundos]

---

## Questão 6

**Indique o tempo de execução no cliente e no servidor (máquinas diferentes, n = 10000).**

- **Tempo de execução no cliente**: [tempo em segundos]
- **Tempo de execução no servidor**: [tempo em segundos]

---

## Questão 7

**Existe diferença nos tempos obtidos? Explique a razão.**

_Resposta:_  
[Sua explicação aqui]

---

## Questão 8

**Tabela: Tempo de execução na mesma máquina para n = {100, 1000, 10000}**

| n    | Tempo Cliente (s) | Tempo Servidor (s) |
|------|-------------------|-------------------|
| 100  | [tempo]            | [tempo]            |
| 1000 | [tempo]            | [tempo]            |
| 10000| [tempo]            | [tempo]            |

**Observação:**

_Resposta:_  
[Suas observações sobre o comportamento conforme n aumenta]

---

## Questão 9

**Tabela: Tempo de execução em máquinas diferentes para n = {100, 1000, 10000}**

| n    | Tempo Cliente (s) | Tempo Servidor (s) |
|------|-------------------|-------------------|
| 100  | [tempo]            | [tempo]            |
| 1000 | [tempo]            | [tempo]            |
| 10000| [tempo]            | [tempo]            |

**Observação:**

_Resposta:_  
[Suas observações sobre o comportamento em máquinas diferentes]

---

## Questão 10

**Compare as duas tabelas. Existem diferenças? Explique.**

_Resposta:_  
[Comparação e explicação]

---

# Detalhes das Execuções

- **Número de execuções realizadas para medição de tempo**: [Indique quantas execuções foram feitas.]

---

# Observações Finais

[Notas extras sobre o projeto, desempenho, dificuldades, aprendizados, etc.]

