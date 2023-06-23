# ETA20222B - Testes Unitários

**Aplicação:** Banco de usuários

**Regras da aplicação:**
- Não permite a adição de usuários com o nome repetido
- Campo "nome" deve ser uma string.
- Campos "nome" e "job" não podem ser nulos.
- Valida que o usuário existe no banco antes de excluií-lo, atualizá-lo e/ou buscá-lo.
- Só permite atualização do campo "job".

## Tarefa:
Desenvolver os testes unitários para os métodos:
- add_user
- delete_user
- update_user
- select_user
