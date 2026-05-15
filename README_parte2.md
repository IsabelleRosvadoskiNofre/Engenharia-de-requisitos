Sim — o problema é que eu coloquei blocos de código Markdown dentro de outro bloco Markdown, e isso quebra fácil.

Use esta versão **sem cercar tudo em bloco de código**. Pode copiar direto para o `README_parte2.md`.

---

## Tarefa 2.1 - Definição da Arquitetura

### Padrão arquitetural escolhido

O padrão arquitetural escolhido para o sistema foi a **arquitetura em camadas**.

Essa arquitetura foi escolhida porque o sistema possui responsabilidades que podem ser separadas de forma clara: 
interação com o usuário, regras de negócio, manipulação dos dados e testes. Como o projeto é um protótipo em Python, 
a arquitetura em camadas permite manter o código simples, organizado e fácil de testar, sem adicionar complexidade 
desnecessária.

No contexto do sistema proposto, as histórias de usuário envolvem ações como criar perfil, criar atividade, 
visualizar atividades disponíveis e inscrever-se em atividades. Essas funcionalidades possuem regras importantes, 
como limite de participantes, preferências de comunicação, informações sensoriais e validação de dados. Por isso, 
é importante separar a interface das regras de negócio, evitando que toda a lógica fique misturada no arquivo principal.

### Representação dos componentes principais

```text
Usuário
  |
  v
app.py
Interface em terminal
  |
  v
servicos.py
Regras de negócio do sistema
  |
  v
repositorio.py
Acesso e manipulação dos dados
  |
  v
dados.py
Dados simulados em memória
```

Também haverá uma pasta de testes:

```text
testes/
  |
  v
test_servicos.py
Testes automatizados das principais regras de negócio
```

### Estrutura planejada do projeto

```text
codigo/
│
├── app.py
├── dados.py
├── repositorio.py
├── servicos.py
└── testes/
    └── test_servicos.py
```

### Componentes e responsabilidades

| Componente                | Responsabilidade                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `app.py`                  | Responsável pela interação com o usuário no terminal, exibindo menus, recebendo entradas e chamando as funções do sistema.                                   |
| `dados.py`                | Responsável por armazenar os dados simulados do protótipo, como usuários, perfis e atividades.                                                               |
| `repositorio.py`          | Responsável por acessar, buscar, cadastrar e atualizar os dados armazenados em memória.                                                                      |
| `servicos.py`             | Responsável pelas regras de negócio do sistema, como criar atividades, listar atividades disponíveis, validar limite de participantes e realizar inscrições. |
| `testes/test_servicos.py` | Responsável por testar as principais funcionalidades e regras do sistema, especialmente as histórias de usuário priorizadas.                                 |

### Relação da arquitetura com as histórias de usuário

A arquitetura escolhida apoia diretamente as histórias de usuário do projeto:

* Para a história **Criar perfil**, a interface recebe os dados, a camada de serviço valida as informações e o repositório armazena o perfil.
* Para a história **Criar uma atividade**, a camada de serviço verifica regras como limite máximo de participantes e campos obrigatórios antes de salvar a atividade.
* Para a história **Visualizar atividades disponíveis**, o repositório busca as atividades e a camada de serviço pode aplicar filtros ou regras de exibição.
* Para a história **Inscrever-se em uma atividade**, a camada de serviço verifica se ainda há vagas disponíveis e impede inscrições acima do limite.
* Para a história **Ver participantes de uma atividade**, a arquitetura permite separar quais dados podem ou não ser exibidos, respeitando a privacidade dos usuários.

### Limitação ou trade-off da arquitetura escolhida

Uma limitação da arquitetura em camadas é que ela pode parecer mais trabalhosa para um protótipo pequeno, pois exige criar mais arquivos e separar responsabilidades que poderiam estar em um único script. Isso aumenta um pouco o esforço inicial.

Por outro lado, essa separação torna o sistema mais fácil de entender, testar e evoluir. Caso o projeto cresça, será mais simples substituir os dados em memória por um banco de dados ou trocar a interface em terminal por uma interface web sem reescrever toda a lógica do sistema.

### Minha reflexão

Essa arquitetura além de facilitar na organização e visualização do projeto, também permite uma atualização/expansão mais fácil.
Tendo os componentes menos acoplados facilitamos a manutenção isolada de uma função.

## Tarefa 2.2 - Implementação com Padrões de Projeto

### Histórias de usuário atendidas pelo protótipo

O protótipo funcional em Python atenderá pelo menos duas histórias de usuário de prioridade alta definidas na Parte 1:

1. **Criar uma atividade**
   Como pessoa neurodivergente, quero criar uma atividade, como caminhada no parque, estudo em biblioteca ou ida a um evento, para encontrar companhia em uma situação com objetivo definido.

2. **Inscrever-se em uma atividade**
   Como pessoa neurodivergente, quero me inscrever em uma atividade com vagas disponíveis para participar de um encontro em pequeno grupo sem precisar iniciar uma interação social do zero.

Essas histórias foram escolhidas porque representam o fluxo principal do sistema: primeiro uma atividade é criada, depois outros usuários podem se inscrever nela respeitando o limite de participantes.

---

### Padrão 1: Factory Method

**Nome do padrão:** Factory Method
**Categoria:** Criacional

#### Justificativa do uso

O padrão **Factory Method** foi aplicado na criação de atividades. Em vez de espalhar a lógica de criação de objetos diretamente pelo sistema, a criação das atividades fica concentrada em uma fábrica.

Isso é útil porque toda atividade precisa seguir algumas regras antes de existir no sistema, como ter título, local, data, horário, nível de interação e limite máximo de participantes. Além disso, o sistema pode crescer futuramente para ter diferentes tipos de atividade, como atividade presencial, atividade online, atividade individual ou atividade em grupo.

Com esse padrão, a criação de atividades fica mais organizada e fácil de alterar.

#### Diagrama aplicado ao projeto

```text
app.py
  |
  | solicita dados da atividade
  v
AtividadeFactory
  |
  | cria objeto Atividade
  v
Atividade
```

#### Classes e módulos envolvidos

```text
codigo/
│
├── app.py
├── modelos.py
├── fabrica.py
└── servicos.py
```

#### Representação do padrão no projeto

```text
+-------------------+
|      app.py       |
+-------------------+
          |
          v
+------------------------+
|   AtividadeFactory     |
|------------------------|
| criar_atividade(...)   |
+------------------------+
          |
          v
+------------------------+
|       Atividade        |
|------------------------|
| id                     |
| titulo                 |
| descricao              |
| local                  |
| data                   |
| horario                |
| limite_participantes   |
| nivel_interacao        |
| participantes          |
+------------------------+
```

#### Onde foi aplicado no código

O padrão será aplicado no arquivo:

```text
codigo/fabrica.py
```

Função/classe relevante:

```text
AtividadeFactory.criar_atividade()
```

Essa função será responsável por criar objetos do tipo `Atividade` com os dados necessários para o sistema.

Exemplo conceitual:

```python
atividade = AtividadeFactory.criar_atividade(
    titulo="Caminhada no parque",
    descricao="Caminhada leve no fim da tarde",
    local="Parque Jaboti",
    data="20/05/2026",
    horario="16:00",
    limite_participantes=4,
    nivel_interacao="pouca conversa"
)
```

---

### Padrão 2: Observer

**Nome do padrão:** Observer
**Categoria:** Comportamental

#### Justificativa do uso

O padrão **Observer** foi aplicado para representar notificações após uma inscrição em atividade.

Quando um usuário se inscreve em uma atividade, pode ser necessário avisar outras partes do sistema. Por exemplo, em uma versão futura, o sistema poderia notificar o criador da atividade, atualizar uma interface gráfica, enviar uma mensagem ou registrar um histórico.

No protótipo, esse comportamento será simplificado: quando uma inscrição for realizada com sucesso, um observador será notificado e exibirá uma mensagem no terminal. Mesmo simples, isso demonstra a separação entre a regra principal de inscrição e as ações que acontecem depois dela.

#### Diagrama aplicado ao projeto

```text
Usuario se inscreve
        |
        v
ServicoAtividades.inscrever_usuario()
        |
        v
Atividade notifica observadores
        |
        v
NotificadorConsole
```

#### Classes e módulos envolvidos

```text
codigo/
│
├── modelos.py
├── servicos.py
└── notificadores.py
```

#### Representação do padrão no projeto

```text
+--------------------------+
|   ServicoAtividades      |
|--------------------------|
| inscrever_usuario(...)   |
+--------------------------+
             |
             v
+--------------------------+
|        Atividade         |
|--------------------------|
| adicionar_observador()   |
| notificar_observadores() |
+--------------------------+
             |
             v
+--------------------------+
|    NotificadorConsole    |
|--------------------------|
| atualizar(...)           |
+--------------------------+
```

#### Onde foi aplicado no código

O padrão será aplicado principalmente nos arquivos:

```text
codigo/modelos.py
codigo/notificadores.py
codigo/servicos.py
```

Trechos relevantes:

```text
Atividade.adicionar_observador()
Atividade.notificar_observadores()
NotificadorConsole.atualizar()
ServicoAtividades.inscrever_usuario()
```

No fluxo do sistema, quando a inscrição for aceita, a atividade notificará seus observadores.

Exemplo conceitual:

```python
atividade.adicionar_observador(NotificadorConsole())
servico.inscrever_usuario(atividade_id=1, usuario_id=2)
```

Após a inscrição, o observador poderá exibir uma mensagem como:

```text
Usuário inscrito com sucesso na atividade Caminhada no parque.
```

---

### Relação dos padrões com as histórias de usuário

O **Factory Method** está diretamente relacionado à história **Criar uma atividade**, pois organiza a criação dos objetos de atividade e centraliza as regras iniciais de construção.

O **Observer** está diretamente relacionado à história **Inscrever-se em uma atividade**, pois permite que o sistema reaja a uma inscrição bem-sucedida sem misturar a lógica de inscrição com a lógica de notificação.

Essa separação ajuda a manter o código mais organizado, principalmente porque o sistema trabalha com ações sensíveis para o usuário, como participação em pequenos grupos, limite de vagas e confirmação de inscrição.

---

### Revisão crítica

O padrão **Observer** poderia se tornar um problema se o sistema crescesse e muitos observadores fossem adicionados sem controle, como notificações por e-mail, mensagens internas, atualização de interface e histórico de eventos. Nesse caso, uma simples inscrição poderia disparar várias ações difíceis de rastrear, dificultando a manutenção e o entendimento do fluxo por novos membros da equipe. Para evitar isso em um projeto maior, seria necessário documentar bem os observadores e talvez usar uma estrutura mais robusta de eventos.

## Tarefa 2.3 - Testes

### Estratégia de teste adotada

A estratégia adotada foi criar testes automatizados com `unittest` para validar as principais regras de negócio do protótipo, especialmente as funcionalidades relacionadas às histórias de usuário de prioridade alta: criação de atividades e inscrição em atividades. Os testes foram concentrados nas camadas de fábrica e serviço, pois nelas estão as regras mais importantes do sistema, como validação de campos obrigatórios, limite de participantes, busca de atividades e controle de inscrição.

Foram testados dois conjuntos principais:

1. `AtividadeFactory.criar_atividade()`
2. `ServicoAtividades.inscrever_usuario()`

Essa estratégia é adequada porque o sistema foi organizado em arquitetura em camadas. Assim, é possível testar a lógica principal sem depender diretamente da interface em terminal presente no `app.py`.

### Testes da função `AtividadeFactory.criar_atividade()`

Foram criados testes para verificar:

* cenário de sucesso: criação de uma atividade válida;
* cenário de falha/exceção: tentativa de criar atividade com limite de participantes inválido;
* cenário de borda: criação de atividade com o limite mínimo permitido de participantes.

Esses testes validam o padrão Factory Method aplicado ao projeto, garantindo que as atividades sejam criadas de forma controlada e respeitando as regras definidas.

### Testes do método `ServicoAtividades.inscrever_usuario()`

Foram criados testes para verificar:

* cenário de sucesso: inscrição de um usuário em uma atividade existente;
* cenário de falha/exceção: tentativa de inscrição em uma atividade inexistente;
* cenário de borda: inscrição até atingir exatamente o limite máximo de participantes;
* cenário adicional de falha: tentativa de inscrição duplicada do mesmo usuário.

Esses testes validam uma regra central do sistema: permitir participação em grupos pequenos sem ultrapassar o limite definido na criação da atividade.

### Aspectos não cobertos pelos testes

Os testes não cobrem diretamente a interface em terminal implementada em `app.py`, pois ela depende de entradas manuais do usuário por meio de `input()`. Também não foram testadas notificações impressas no console pelo `NotificadorConsole`, pois no protótipo elas funcionam apenas como uma saída visual simples. O foco dos testes foi validar as regras de negócio, que são mais críticas para o funcionamento correto do sistema.

### Revisão crítica

Uma parte do código que seria mais difícil de testar é o arquivo `app.py`, porque ele depende de interação direta com o usuário por meio do terminal. Em um projeto maior, essa dificuldade se tornaria mais relevante porque fluxos com muitos menus, entradas inválidas e respostas diferentes exigiriam simulações mais complexas ou testes de interface. Para reduzir esse problema, seria importante manter o máximo possível de lógica fora do `app.py`, deixando esse arquivo apenas como camada de entrada e saída.
