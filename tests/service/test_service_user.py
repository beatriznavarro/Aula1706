from src.service.service_user import ServiceUser


class TestServiceUser:

    # Adiciona usuário
    def test_add_usuario_com_sucesso(self):
        # Setup
        name = "Beatriz"
        job = "sdet"
        resultado_esperado = "Usuário adicionado com sucesso."
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name, job=job)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_usuario_invalido_nomeNulo(self):
        # Setup
        name = None
        job = "sdet"
        resultado_esperado = "Usuário não adicionado - campo nome e/ou job igual a nulo."
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name, job=job)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_usuario_invalido_jobNulo(self):
        # Setup
        name = "Beatriz"
        job = None
        resultado_esperado = "Usuário não adicionado - campo nome e/ou job igual a nulo."
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name, job=job)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_usuario_invalido_jobAndNomeNulos(self):
        # Setup
        name = None
        job = None
        resultado_esperado = "Usuário não adicionado - campo nome e/ou job igual a nulo."
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name, job=job)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_usuario_invalido_naoString(self):
        # Setup
        name = 32
        job = "sdet"
        resultado_esperado = "Usuário não adicionado - campo nome diferente de string."
        service = ServiceUser()

        # Chamada
        resultado = service.add_user(name=name, job=job)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_usuario_duplicado(self):
        # Setup
        name = "Beatriz"
        job = "sdet"
        resultado_esperado = "Usuário já existente."
        service = ServiceUser()

        # Adicionar user
        service.add_user(name=name, job=job)

        # Chamada
        resultado = service.add_user(name=name, job=job)

        # Avaliacao
        assert resultado_esperado == resultado

    # Deleta usuário
    def test_deleta_usuario_com_sucesso(self):
        # Setup
        name = "Beatriz"
        job = "sdet"
        resultado_esperado = "Usuário deletado com sucesso."
        service = ServiceUser()
        service.add_user(name=name, job=job)

        # Chamada
        resultado = service.delete_user(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_deleta_usuario_invalido(self):
        # Setup
        name = "Beatriz"
        job = "sdet"
        resultado_esperado = "Usuário não encontrado."
        service = ServiceUser()
        service.add_user(name=name, job=job)

        # Chamada
        resultado = service.delete_user(name="Alicia")

        # Avaliacao
        assert resultado_esperado == resultado

    # Atualiza usuário
    def test_atualiza_usuario_com_sucesso(self):
        # Setup
        name = "Beatriz"
        job = "sdet"
        resultado_esperado = "Usuário atualizado com sucesso."
        service = ServiceUser()
        service.add_user(name=name, job=job)

        # Chamada
        resultado = service.update_user(name=name, job="Usuário atualizado com sucesso.")

        # Avaliacao
        assert resultado_esperado == resultado

    def test_atualiza_usuario_invalido(self):
        # Setup
        name = "Beatriz"
        job = "sdet"
        resultado_esperado = "Usuário não encontrado."
        service = ServiceUser()
        service.add_user(name=name, job=job)

        # Chamada
        resultado = service.update_user(name="Alicia", job=job)

        # Avaliacao
        assert resultado_esperado == resultado

    # Recupera usuário
    def test_recupera_usuario_com_sucesso(self):
        # Setup
        name = "Beatriz"
        job = "sdet"
        resultado_esperado = job
        service = ServiceUser()
        service.add_user(name=name, job=job)

        # Chamada
        resultado = service.select_user(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_recupera_usuario_invalido(self):
        # Setup
        name = "Beatriz"
        job = "sdet"
        resultado_esperado = "Usuário não encontrado."
        service = ServiceUser()
        service.add_user(name=name, job=job)

        # Chamada
        resultado = service.select_user(name="Alicia")

        # Avaliacao
        assert resultado_esperado == resultado
