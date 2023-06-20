# ETA20222B - Testes Unitários

**Aplicação:** Banco de usuários

**Regras da aplicação:**
- Não permite a adição de usuários com o nome repetido
- Campo "nome" deve se string.
- Campos "nome" e "job" não podem ser nulos.
- Valida que o usuário existe antes de excluií-lo, atualizá-lo e/ou buscá-lo.
- So permite atualização do campo "job".

## Tarefa:
Desenvolver os testes unitários para os métodos:
- add_user
- delete_user
- update_user
- select_user
