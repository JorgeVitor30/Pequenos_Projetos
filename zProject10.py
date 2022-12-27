#C:\Users\\I5 11400F\AppData\\Local\\Programs\\Python\\Python311\\python.exe
# ABRIR A PARTE DO SERVER (HOST)
### CGI 

import cgitb, cgi
cgitb.enable(display=1, logdir='./')

form = cgi.FieldStorage()

altura_ = float(form.getvalue('altura'))
peso_ = float(form.getvalue('peso'))
abd_ = float(form.getvalue('abd'))
sexo_ = str(form.getvalue('sexo').upper())


imc = peso_ / ((altura_ / 100) ** 2)



if 18.5 < imc <= 24.9:
    global info1
    global info2
    info1 = 'Normal'
    info2 ='18.5 < imc <= 24.9'
elif 25 <= imc <= 29.9:
    info1 = 'SobrePeso'
    info2 = '25 < imc <= 29'
elif 30 <= imc <= 40:
    info1 = 'Obesidade' 
    info2 = '30 <= imc < 40'     
elif imc > 40 :
    info1 = 'Obesidade Grave'
    info2 = 'imc > 40'
else:
    info1 = 'Desconhecido'
    info2 = 'Desconhecido'

ag = 'PESO x 0.035'
agua = 0.035 * peso_

if sexo_ == 'M':
    sexo_ = 'Masculino'
    if abd_ <= 90:
        global info3
        global info4
        info3 = 'Risco Normal'
        info4 = 'Circu. Abdominal <= 90'
    elif 90 < abd_ <= 94:
        info3 = 'Risco Médio'
        info4 = '90 < Circu. Abdominal<= 94'
    elif 94 <= abd_ < 102:
        info3 = 'Risco Alto'
        info4 = '94 <= Circu. Abdominal< 102'
    elif abd_ >= 102:
        info3 = 'Risco Altíssimo'
        info4 = 'Circu. Abdominal> 102'
            
elif sexo_ == 'F':
    sexo_ = 'Feminino'
    if abd_ <= 80:
        info3 = 'Risco Normal'
        info4 = 'Circu. Abdominal <= 80'
    elif 80 < abd_ <= 84:
        info3 = 'Risco Médio'
        info4 = '84 < Circu. Abdominal < 84'
    elif 84 <= abd_ < 94:
        info3 = 'Risco Alto'
        info4 = '84 <= Circu. Abdominal < 94'
    elif abd_ >= 88:
        info3 = 'Risco Altíssimo'
        info4 = 'Circu. Abdominal > 88'


style = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700;800;900&display=swap');

      * {
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
      }

      body {
        font-family: 'Poppins', sans-serif;
        background-color: #f5f5f5;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        gap: 2rem;
        text-align: center;
      }

      body > div {
        margin-top: 3rem;
      }

      .box {
        /* border: 1px solid red; */
        background-color: #f8f5f8;
        box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
        padding: 2rem;
        border-radius: 10px;
      }

      li {
        list-style: none;
        font-size: 1.2rem;
        font-weight: 500;

        padding: 1rem;
      }

      p {
        font-size: 1.2rem;
        font-weight: 500;
      }

      p span {
        font-weight: 700;
      }
"""

print(f"""
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Resultado</title>
    <style>
    {style}
    </style>
  </head>
  <body>
    <div class="box">
      <h1>Resultado</h1>
      <p>Peso: <span>{peso_} kg</span></p>
      <p>Altura: <span>{altura_/100} m</span></p>
      <p>Circunf. Abdominal: <span>{abd_} cm</span></p>
      <p>Sexo: <span>{sexo_}</span></p>
    </div>

    <div class="box">
      <h2>Calculos</h2>
      <p>IMC: aprox. {imc:.2f}</p>
      <ul>
        <li>{info1}</li> 
        <li>{info2}</li>
      </ul> <br>
      <p>Agua Diaria: {agua:.2f} L</p>
      <ul>
        <li>{ag}</li> <br> <br>
      </ul>
      <p>Risco Cardiaco:</p> 
      <ul>
        <li>{info3}</li> 
        <li>{info4}</li>
      </ul>
    </div>
  </body>
</html>
      
      
      
""")












