from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/")
def start_page():
    return "Миссия Колонизация Марса"


@app.route("/index")
def second_page():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    message = """Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!"""
    return "<br>".join(message.split("\n"))


@app.route("/image_mars")
def show_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src='{url_for('static', filename="img/MARS.png")}'
                        alt='картинки нет'>
                        <h2>Марс</h2>
                      </body>
                    </html>"""


@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet" 
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                       crossorigin="anonymous">
                       <link rel="stylesheet" type="text/css" href="{url_for('static', filename="css/style.css")}">
                       <title>Привет, Марс!</title>
                     </head>
                     <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src='{url_for('static', filename="img/MARS.png")}'
                        alt='картинки нет'>
                        <div class="alert alert-primary" role="alert">
                          Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-primary" role="alert">
                          Человечеству мала одна планета.
                        </div>
                         <div class="alert alert-primary" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-primary" role="alert">
                          И начнем с Марса!
                        </div>
                        <div class="alert alert-primary" role="alert">
                          Присоединяйся!
                        </div>
                      </body>
                   </html>'''


@app.route("/astronaut_selection", methods=["POST", "GET"])
def astronaut_selection():
    if request.method == 'GET':
        joined_options = "\n".join([f"<option>{i}</option>" for i in "инженер-исследователь, \
        пилот, строитель, экзобиолог, \
        врач, инженер по терраформированию, климатолог, специалист по радиационной защите, \
        астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода,\
        киберинженер, штурман, пилот дронов".split(", ")])

        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css"\
                                 href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1>Анкета претендента на участие в миссии</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="surname" class="form-control" id="surname"\
                                         placeholder="Введите фамилию" name="surname">
                                        <input type="name" class="form-control" id="name" placeholder="Введите имя"\
                                         name="name">
                                        <input type="email" class="form-control" id="email"\
                                          aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                            
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              {joined_options}
                                            </select>
                                        </div>
                                        
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male"\
                                               value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female"\
                                               value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>     
                                        </div>
                                        
                                        
                                        <div class="form-group">
                                            <label for="about">Почему вы хотите участвовать в миссии?</label>
                                            <textarea class="form-control" id="why" rows="3" name="why"></textarea>
                                        </div>
                                        
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules"\
                                            name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?\
                                            </label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
