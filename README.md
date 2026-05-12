# Engenharia-de-requisitos
## Tarefa 1.1 - Proposta de Tema

O sistema proposto é uma plataforma para conectar pessoas neurodivergentes por meio de atividades compartilhadas em pequenos grupos. Ele resolve o problema da dificuldade de iniciar interações sociais e criar vínculos quando não há um contexto claro para a conversa. Os usuários principais são pessoas neurodivergentes, como pessoas autistas, com TDAH ou outras condições que possam impactar comunicação, socialização ou sensibilidade sensorial. A plataforma permite que usuários encontrem ou criem atividades, como caminhadas, oficinas, aulas, jogos, estudos em grupo ou eventos culturais, com limite reduzido de participantes. O problema é relevante porque atividades com objetivo definido tornam a socialização mais previsível, segura e menos pressionante.

## Tarefa 1.2 - Planejamento de Entrevista

### Objetivo da entrevista

O objetivo da entrevista é compreender como pessoas neurodivergentes vivenciam a criação de vínculos, a aproximação com novas pessoas e a participação em atividades sociais. A entrevista busca identificar dificuldades, preferências, frustrações com soluções atuais e critérios que influenciam a decisão de se aproximar de alguém ou participar de uma atividade. As respostas serão usadas para definir requisitos de um sistema que conecte pessoas neurodivergentes por meio de atividades compartilhadas em pequenos grupos, considerando segurança, previsibilidade, conforto social e diferentes níveis de comunicação.

### Roteiro de entrevista semiestruturada

1. **Você pode me contar como geralmente funcionam suas relações de amizade ou aproximação com novas pessoas?**  
   Tipo: pergunta aberta para compreensão do problema.

2. **O que normalmente faz você se aproximar de alguém?**  
   Exemplos: personalidade, interesses em comum, assuntos para conversar, atividades que vocês poderiam fazer juntos, sensação de segurança ou identificação.  
   Tipo: pergunta aberta para compreensão do problema.

3. **Quais situações sociais costumam ser mais confortáveis para você? Exemplo: conversar por mensagem, conversar pessoalmente, fazer uma atividade junto, estar em grupo pequeno ou conhecer uma pessoa individualmente? Por quê?**  
   Tipo: pergunta aberta para compreensão do problema.

4. **Você já usa ou já usou aplicativos de relacionamento, amizade, grupos de WhatsApp, redes sociais ou comunidades online para conhecer pessoas?**  
   Tipo: pergunta sobre rotina/uso de soluções atuais.

5. **O que faz você continuar usando ou desistir de um aplicativo voltado a conhecer pessoas? (Se nunca usou: O que faz você continuar ou desistir de conhecer pessoas?)**  
   Tipo: pergunta sobre frustrações ou limitações com soluções atuais.

6. **Quando você quer sair, participar de uma atividade ou ir a algum lugar, como normalmente decide se vai sozinho(a), chama alguém, procura companhia ou desiste de ir?**  
   Tipo: pergunta sobre fluxo de trabalho/rotina do usuário.

7. **Como você costuma encontrar atividades para fazer, como caminhadas, oficinas, aulas, jogos, eventos culturais, estudos em grupo ou exercícios físicos?**  
   Tipo: pergunta sobre fluxo de trabalho/rotina do usuário.

8. **Você já deixou de participar de alguma atividade por não ter companhia, por não saber como seria o ambiente ou por receio da interação social? Pode contar como foi?**  
   Tipo: pergunta sobre frustrações ou limitações atuais.

9. **Como você lida com convidar pessoas para eventos/atividades?**  
   Tipo: pergunta sobre frustrações ou limitações atuais.

10. **Para você, o quanto importa saber o nível de comunicação esperado antes de participar de uma interação?**  
   Exemplos: pouca conversa, conversa moderada, bastante conversa, mais ouvir do que falar, comunicação por mensagens antes do encontro.  
   Tipo: pergunta voltada à definição de requisitos.

11. **Você preferiria conhecer pessoas vendo primeiro o perfil delas e depois combinando uma atividade, ou vendo primeiro uma atividade e depois as pessoas inscritas nela? Por quê?**  
   Tipo: pergunta voltada à decisão de fluxo do sistema.

12. **Qual seria uma quantidade confortável de pessoas em uma atividade em grupo?**  
   Exemplos: 2 pessoas, até 3 pessoas, até 4 pessoas, mais de 4 pessoas dependendo da atividade.  
   Tipo: pergunta voltada à definição de requisitos.

13. **Quais informações seriam importantes aparecer antes de você decidir participar de uma atividade?**  
   Exemplos: local, horário, duração, quantidade de pessoas, nível de barulho, tipo de ambiente, necessidade de conversa, perfil dos participantes, possibilidade de sair antes, presença de pessoas conhecidas ou regras do grupo.  
   Tipo: pergunta voltada à definição de requisitos.

14. **Você se sentiria confortável criando uma atividade, como “caminhada no parque”, “estudar em uma biblioteca” ou “ir a um evento”, para outras pessoas participarem? O que precisaria existir no sistema para isso parecer seguro?**  
   Tipo: pergunta voltada à definição de requisitos e segurança.

15. **Existe algo que eu não perguntei, mas que você considera importante para criar uma plataforma mais acolhedora e útil para pessoas neurodivergentes?**  
   Tipo: pergunta de encerramento.

### Minha reflexão

Ao revisar as perguntas, percebi que a entrevista não deve servir apenas para confirmar a ideia inicial do sistema, mas para descobrir qual formato realmente faz sentido para o público-alvo e o que faria sentido para eles, o que ajudaria de forma sistemática. Por isso, incluí perguntas que ajudam a decidir se a plataforma deve priorizar perfis de pessoas, atividades ou uma combinação dos dois. Também considerei que pessoas neurodivergentes podem ter preferências muito diferentes de comunicação: algumas podem gostar de conversar bastante, enquanto outras podem preferir interações com menos fala e mais foco na atividade. Assim, o roteiro busca entender não só o problema da dificuldade de socialização, mas também quais informações e controles poderiam tornar a experiência mais previsível, segura e confortável.

## Tarefa 1.3 - Histórias de Usuário

### História de Usuário 1 — Criar perfil com preferências sociais e sensoriais

Como pessoa neurodivergente, quero criar um perfil com meus interesses, preferências de comunicação e sensibilidades sensoriais para encontrar atividades e pessoas mais compatíveis com meu conforto.

Critérios de aceitação:
- O sistema deve permitir cadastrar nome/apelido, interesses e breve descrição do usuário.
- O sistema deve permitir informar preferências de comunicação, como pouca conversa, conversa moderada ou bastante conversa.
- O sistema deve permitir informar preferências sensoriais, como evitar locais muito barulhentos, cheios ou com luz intensa.
- O sistema deve permitir editar essas informações posteriormente.

Prioridade: Alta.  
Justificativa: Essa funcionalidade é essencial porque o sistema depende das preferências individuais para tornar a experiência mais segura e confortável. Sem perfil, a conexão entre usuários ficaria genérica demais.

---

### História de Usuário 2 — Criar uma atividade

Como pessoa neurodivergente, quero criar uma atividade, como caminhada no parque, estudo em biblioteca ou ida a um evento, para encontrar companhia em uma situação com objetivo definido.

Critérios de aceitação:
- O sistema deve permitir cadastrar título, descrição, local, data e horário da atividade.
- O sistema deve permitir definir o número máximo de participantes, respeitando um limite pequeno, como até 4 pessoas.
- O sistema deve permitir informar o nível de interação esperado, como pouca conversa, conversa moderada ou atividade mais social.
- O sistema deve permitir informar características do ambiente, como nível de barulho, duração estimada e possibilidade de sair antes.

Prioridade: Alta.  
Justificativa: Essa é uma das funcionalidades centrais do sistema, pois diferencia a proposta de uma rede social comum. A conexão acontece a partir de uma atividade concreta, não apenas pela avaliação de perfis.

---

### História de Usuário 3 — Visualizar atividades disponíveis

Como pessoa neurodivergente, quero visualizar atividades disponíveis com informações claras sobre ambiente, participantes e nível de interação para decidir se me sinto confortável em participar.

Critérios de aceitação:
- O sistema deve listar atividades disponíveis com título, local, data, horário e quantidade de participantes.
- O sistema deve mostrar o limite máximo de pessoas em cada atividade.
- O sistema deve exibir o nível de comunicação esperado na atividade.
- O sistema deve indicar características relevantes do ambiente, como barulho, lotação esperada ou duração.

Prioridade: Alta.  
Justificativa: A previsibilidade é um ponto importante para o público-alvo. Antes de participar, o usuário precisa entender o contexto da atividade para avaliar se ela combina com suas necessidades e limites.

---

### História de Usuário 4 — Inscrever-se em uma atividade

Como pessoa neurodivergente, quero me inscrever em uma atividade com vagas disponíveis para participar de um encontro em pequeno grupo sem precisar iniciar uma interação social do zero.

Critérios de aceitação:
- O sistema deve permitir inscrição apenas se a atividade ainda tiver vagas disponíveis.
- O sistema deve impedir que o número de participantes ultrapasse o limite definido.
- O sistema deve mostrar uma confirmação após a inscrição.
- O sistema deve permitir visualizar em quais atividades o usuário está inscrito.

Prioridade: Alta.  
Justificativa: A inscrição é necessária para transformar a visualização das atividades em participação real. Também permite controlar o tamanho dos grupos, que é uma regra importante do sistema.

---

### História de Usuário 5 — Ver participantes de uma atividade

Como pessoa neurodivergente, quero visualizar informações básicas das pessoas inscritas em uma atividade para decidir se aquele grupo parece confortável para mim.

Critérios de aceitação:
- O sistema deve mostrar os participantes já inscritos na atividade.
- O sistema deve exibir apenas informações básicas do perfil, como apelido, interesses e preferências de comunicação.
- O sistema não deve exibir informações sensíveis sem consentimento do usuário.
- O sistema deve permitir que o usuário veja se os interesses ou preferências de comunicação dos participantes são compatíveis com os seus.

Prioridade: Média.  
Justificativa: Essa funcionalidade ajuda na sensação de segurança e previsibilidade, mas não é tão essencial quanto criar, visualizar e participar de atividades. Ela melhora a tomada de decisão do usuário antes do encontro.

---

### Minha reflexão

Tentei focar em requisitos que pessoas neurodivergentes poderiam achar que criaria um ambiente mais confortável/adaptado às necessidades delas. Muito da dificuldade desse público é INICIAR quando se trata de relações interpessoais e o objetivo não é criar funcionalidades para cortar o "caminho", é se adaptar a maneira que essas pessoas já criam as relações delas, muitas vezes com trejeitos diferentes de pessoas neurotípicas.

## Tarefa 1.4 - Validação de Requisitos

### Técnica aplicada: Verificação de completude e consistência

Foram escolhidas para validação as histórias 2 e 4, pois elas representam duas funcionalidades centrais do sistema: criar uma atividade e inscrever-se em uma atividade.

---

## História de Usuário 2 — Criar uma atividade

Como pessoa neurodivergente, quero criar uma atividade, como caminhada no parque, estudo em biblioteca ou ida a um evento, para encontrar companhia em uma situação com objetivo definido.

### Análise de ambiguidades nos critérios de aceitação

Alguns critérios ainda possuem termos que podem gerar interpretações diferentes:

- O termo “limite pequeno” precisa ser definido de forma objetiva. Para o protótipo, o limite máximo será de 4 participantes por atividade.
- O “nível de interação esperado” precisa ter opções fechadas para evitar descrições muito vagas. Por exemplo: pouca conversa, conversa moderada ou alta interação.
- A expressão “características do ambiente” pode ser ampla demais. O sistema precisa definir quais campos serão obrigatórios, como nível de barulho, duração estimada e local.
- A “possibilidade de sair antes” precisa ser melhor explicada, pois o sistema não controla o comportamento presencial, apenas informa se a atividade permite saída flexível.

### Conflitos potenciais com outras histórias

Essa história tem relação direta com a História 3, de visualizar atividades disponíveis, pois tudo que for cadastrado na criação da atividade precisa aparecer de forma clara na listagem.

Também se relaciona com a História 4, de inscrição em atividade, pois o limite de participantes definido na criação deve ser respeitado durante a inscrição.

Um possível conflito aparece com a História 5, de ver participantes. Se a atividade for criada por um usuário, é necessário definir se o criador será automaticamente exibido como participante ou se poderá criar uma atividade sem participar dela.

### Informações que precisam ser elucidadas junto ao usuário

- O criador da atividade conta como participante no limite máximo?
- Toda atividade criada por usuário precisa passar por moderação antes de aparecer?
- Quais informações sobre ambiente são obrigatórias?
- O usuário pode editar ou cancelar uma atividade após criá-la?
- O sistema deve permitir atividades online ou apenas presenciais?
- O local exato deve aparecer para todos ou apenas para pessoas inscritas?

### Ajuste sugerido para a história

Como pessoa neurodivergente, quero criar uma atividade presencial com data, horário, local, limite de até 4 participantes, nível de interação e informações básicas do ambiente para encontrar companhia em uma situação social mais previsível.

### Minha reflexão

Ao validar essa história, percebi que “criar atividade” parece simples, mas envolve decisões importantes de segurança, privacidade e previsibilidade. Para o público-alvo, não basta informar o título da atividade; detalhes como quantidade de pessoas, nível de barulho e expectativa de conversa podem influenciar diretamente a decisão de participar. Por isso, essa história precisa ser mais objetiva nos campos obrigatórios e nas regras de participação.

---

## História de Usuário 4 — Inscrever-se em uma atividade

Como pessoa neurodivergente, quero me inscrever em uma atividade com vagas disponíveis para participar de um encontro em pequeno grupo sem precisar iniciar uma interação social do zero.

### Análise de ambiguidades nos critérios de aceitação

Alguns critérios precisam ser especificados melhor:

- “Vagas disponíveis” precisa considerar o limite máximo definido na criação da atividade.
- A “confirmação após a inscrição” precisa ser definida: pode ser uma mensagem simples no sistema ou uma tela/lista de atividades inscritas.
- “Visualizar em quais atividades o usuário está inscrito” pode ser uma funcionalidade própria, mas no protótipo pode ser apenas uma listagem simples.
- É necessário definir se o usuário pode cancelar sua inscrição.
- Também é necessário definir se uma pessoa pode se inscrever mais de uma vez na mesma atividade.

### Conflitos potenciais com outras histórias

Essa história depende diretamente da História 3, pois o usuário precisa visualizar as atividades antes de se inscrever.

Também depende da História 2, pois o limite de participantes definido pelo criador da atividade deve ser respeitado no momento da inscrição.

Pode haver conflito com a História 5, pois se o usuário puder ver os participantes antes de se inscrever, é preciso definir quais dados aparecem publicamente e quais aparecem apenas após a inscrição.

### Informações que precisam ser elucidadas junto ao usuário

- O usuário pode cancelar inscrição depois de confirmar presença?
- Existe lista de espera quando a atividade está cheia?
- O sistema deve impedir que o usuário se inscreva em duas atividades no mesmo horário?
- O usuário precisa enviar mensagem ao criador antes de se inscrever?
- Os participantes são exibidos antes ou somente depois da inscrição?
- Deve haver algum aviso sobre regras de segurança antes da confirmação?

### Ajuste sugerido para a história

Como pessoa neurodivergente, quero me inscrever uma única vez em uma atividade com vagas disponíveis, respeitando o limite máximo de participantes, para participar de um encontro em pequeno grupo com contexto definido e menor pressão social.


---

## Revisão crítica

Dentre as 5 histórias de usuário, eu removeria a História 5 — Ver participantes de uma atividade, caso o escopo do projeto precisasse ser reduzido pela metade.

Essa remoção teria impacto na previsibilidade e na sensação de segurança do usuário, pois ele deixaria de ver quem já está inscrito antes de participar. Porém, as funcionalidades principais do sistema ainda continuariam funcionando: criar perfil, criar atividade, visualizar atividades e se inscrever. 
