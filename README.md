# timer-tracker
O projeto "timer-tracker" é uma ferramenta que permite monitorar o uso de um programa específico no seu computador. Ele verifica se o programa escolhido está aberto e monitora a atividade do mouse e teclado. Quando o programa está em execução e o mouse ou teclado estão sendo usados, o "timerTrack" começa a contar o tempo. Se a atividade do mouse e teclado for interrompida, o contador é pausado e retomado automaticamente se a atividade for detectada novamente.

# Bibliotecas Utilizadas
Tkinter: Para a criação de uma pequena interface gráfica que exibe o timer.
datetime: Usada para manipular informações de data e hora, permitindo que o projeto registre o tempo decorrido.
time: Utilizada para rastrear o tempo e atrasos.
psutil: Esta biblioteca é usada para verificar se o programa escolhido está em execução e monitorar processos do sistema.
threading: Usada para criar threads que permitem ao projeto monitorar continuamente a atividade do mouse e teclado.
