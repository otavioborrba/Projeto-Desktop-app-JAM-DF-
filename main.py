"""Demonstração do fluxo completo do JAM-DF """
from datetime import datetime, timedelta

from modelos import SistemaJAM
from modelos.notificacoes import EmailNotificador, WhatsAppNotificador
from modelos.pessoas import Cliente, Endereco, Tecnico
from modelos.servicos import Consultoria, Instalacao, Manutencao

sistema = SistemaJAM()
cliente = Cliente("Maria Souza", "(61) 99999-0000", "maria@email.com",
                  Endereco("Quadra 5, Conjunto B, Casa 10", "Brasília"))
tecnico = Tecnico("Carlos Lima", "(61) 98888-1111", "carlos@jamdf.com", "CFTV")
sistema.cadastrar_cliente(cliente)
sistema.cadastrar_tecnico(tecnico)

for srv in (Instalacao("Câmeras IP", 250.0), Manutencao("Revisão de alarme", 120.0),
            Consultoria("Projeto de segurança", 200.0)):
    print(f"{srv}: R$ {srv.calcular_custo(3):.2f}")

email, zap = EmailNotificador(), WhatsAppNotificador()
sol = sistema.abrir_solicitacao(cliente, Instalacao("Câmeras IP", 250.0), "4 câmeras externas")
sol.enviar_orcamento(tecnico, quantidade=4, notificador=email)
sol.responder_orcamento(aprovado=True)
sol.agendar(datetime.now() + timedelta(days=3), zap)
sol.editar_data(datetime.now() + timedelta(days=5), zap)
sol.contatar_tecnico(zap, "Portão com acesso pela lateral.")
print("Status final:", sol.status.value)
