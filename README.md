📟 Calculadora Tkinter + Docker = ❤️
A calculadora mais charmosa do universo (ou quase)!

<div align="center"> <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjN0aDE3cWZtamFzbWVybHVwOXVqaTg1b3YwNWV2eDVzbWNianplNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L2djWse2JlucU/giphy.gif" width="300" alt="GIF de uma calculadora animada"> </div>
🚀 Como rodar essa maravilha?
Você tem 3 opções mágicas para usar essa calculadora:

1️⃣ Método Docker (recomendado para impressionar seus amigos)
bash
# 1. Construa a imagem (como um chef construindo um bolo 🎂)
docker build -t calculadora-tkinter .

# 2. Permita que o Docker converse com seu X11 (só Linux!)
xhost +local:docker

# 3. Execute e veja a mágica acontecer ✨
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  calculadora-tkinter
🔹 Nota para usuários de Mac/Windows:
Infelizmente, o Docker não brinca bem com GUIs nesses sistemas. Se estiver no Mac, considere usar XQuartz. No Windows, o WSL2 + XServer pode ajudar (ou só rode direto no Python 😉).

2️⃣ Método Python Puro (sem Docker, para os puristas)
bash
python3 calculadora.py
Pré-requisitos:

Python 3.x

Tkinter (geralmente já vem instalado)

3️⃣ Método "Eu só quero ver como funciona"
Se você só quer testar sem instalar nada, dê uma olhada na calculadora em ação:

<div align="center"> <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmZpMG8wbG01cDRpaHYxbG95ZmduOGxhOGJ6c2g1eGY4eWRxZmY4eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FxfuJVTj0takrn2B40/giphy.gif" alt="Demonstração da calculadora" width="400"> </div>
🛠 Funcionalidades Incríveis
✅ Operações básicas: +, -, ×, ÷
✅ Limpeza total (C) - para quando tudo der errado 😅
✅ Backspace (<) - porque todo mundo merece uma segunda chance
✅ Avaliação em tempo real - sem frescura, só resultados

🐛 Problemas?
"A calculadora não abre no Docker!"
🔸 Verifique se seu sistema tem X11 (Linux) ou XQuartz (Mac).
🔸 Se aparecer Error: Can't open display, tente:

bash
export DISPLAY=host.docker.internal:0  # Mac/Windows (ajuste conforme seu SO)
🤔 Por que essa calculadora é especial?
Dockerizada 🐳 → Roda em qualquer lugar (quase)

Tkinter 🎨 → Interface clássica e funcional

Divertida 🎉 → Porque calculadoras podem ser legais!

<div align="center"> <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2dvYnBodTJ6OTF5ZjU5dmxvajk2a3BwMGhjZXlubGtyNzNxNWcwZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2QHLYZFJgjsFq/giphy.gif" width="200"> <br> <strong>Divirta-se calculando! 🎉</strong> </div>
🔹 Créditos:

Tkinter - Pelos widgets clássicos

Docker - Por tornar tudo portátil

Você - Por usar essa calculadora incrível! 😊
