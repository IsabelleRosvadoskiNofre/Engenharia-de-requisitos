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
