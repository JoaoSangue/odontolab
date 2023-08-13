# Consultótio odontológico

No consultório odontológico, as consultas funcionam por ordem de chegada dos pacientes da seguinte maneira: 

O paciente, ao chegar no consultório, obtém do atendente uma senha numérica de ordem crescente e aguarda até o momento de ser chamado.

O atendente chama os pacientes pela ordem das senhas.	

Inicialmente o atendente solicita o CPF do paciente e procura a ficha dele no arquivo de pacientes.

Se o paciente ainda não tiver ficha no consultório, então o atendente solicita os dados básicos do paciente para criar uma ficha para ele, estes dados são:

* CPF
* Nome
* Data de nascimento
* Endereço
* Telefones.

Com a ficha do paciente em mãos, o atendente pergunta ao paciente o motivo da consulta, que geralmente é consulta de rotina ou dor de dente.

Então o atendente cria uma ficha de atendimento com as informações de motivo da consulta, anexa à ficha do paciente e coloca em baixo da pilha de fichas para atendimentos do dentista.

Neste momento o atendente diz ao paciente que espere que o dentista o chame, e finaliza o atendimento.	

O dentista chama os pacientes pela ordem que o atendente organizou a pilha de fichas, mas antes de chamar cada paciente, o dentista analisa o histórico de atendimentos do paciente e o motivo que ele (paciente) descreveu para a consulta atual.

Após atender o paciente, o dentista descreve detalhes do atendimento na ficha de atendimento, como diagnóstico, receita de remédios, solicitação de retorno, etc.

Finaliza-se a consulta e o paciente é liberado.