from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def check_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def add_user(self, name, job):

        # Se não é nulo
        if name != None and job != None:
            # Se nome é um campo string
            isString = isinstance(name, str)
            if isString == True:
                for user in self.store.bd:
                    if user.name == name:
                        return "Usuário já existente."
                user = User(name=name, job=job)
                self.store.bd.append(user)
                return "Usuário adicionado com sucesso."
            else:
                return "Usuário não adicionado - campo nome diferente de string."
        else:
            return "Usuário não adicionado - campo nome e/ou job igual a nulo."

    def delete_user(self, name):
        user_db = self.check_user(name)
        if user_db != None:
            self.store.bd.remove(user_db)
            return "Usuário deletado com sucesso."
        else:
            return "Usuário não encontrado."

    def update_user(self, name, job):
        user_db = self.check_user(name)
        if user_db != None:
            user_db.job = job
            return "Usuário atualizado com sucesso."
        else:
            return "Usuário não encontrado."

    def select_user(self, name):
        user_db = self.check_user(name)
        if user_db != None:
            return user_db.job
        else:
            return "Usuário não encontrado."
