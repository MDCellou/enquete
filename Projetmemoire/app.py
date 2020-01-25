from flask import Flask, render_template,request, flash
import csv

app = Flask(__name__)
app.secret_key = "s3cr3t"


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        ip = request.environ['REMOTE_ADDR']
        smat = '' 
        age ='' 
        genre = '' 
        moyenheur = '' 
        reseau = '' 
        spro = ''
        # recuperation des
        # Situation Matrimoniale
        if request.form['smat'] == '':
            # si il n'y rien selectionné alors msg d'erreur
            flash('Situation Matrimoniale non renseigné')
        else:
            #on recupere dans une variable
            smat = request.form['smat']

        if request.form['age'] == '':
            flash("l'age n'est pas renseigné")
        else:
            age = request.form['age']

        if request.form['genre'] == '':
            flash("le genre n'est pas renseigné")
        else:
            genre = request.form['genre']

        # if request.form['moyenheur'] == '' ne marche pas pour le type radio
        moyenheur = request.form['moyenheur']

        # if request.form['reseau'] == '' ne marche pas pour le type checkbox
        reseau = request.form.getlist('reseau')
        

        if request.form['spro'] == '':
            flash("la Situation Socio-professionnelle n'est pas renseignée")
        else:
            spro = request.form['spro']

        
        if smat != '' and age !='' and genre != '' and moyenheur != '' and reseau != '' and spro != '' and ip != '':
            # return str(smat) + str(age) + str(genre) + str(moyenheur) + str(reseau) + str(spro) + str(ip)

            with open('DB.csv', 'a') as f:
                f.write("""{},{},{},{},{},{},{}\n""".format(ip, smat, age, genre, moyenheur, reseau, spro))
         
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 