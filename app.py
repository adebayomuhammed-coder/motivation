from flask import Flask,render_template, session , request , redirect
import random 
from athletes import athletes_quotes
from hadith import hadith_quotes
from quran import quran_success_quotes 
from mindset import mindset
from islamic import islamic_quotes
from anime import anime_style_quotes
from any import random_quote
import os 

app = Flask('__name__')
app.secret_key = os.getenv("SECRET_KEY")

@app.route ("/")
def home():
    return render_template("index.html")




@app.route ("/quote")
def motivation ():
    save = session.get('category')
    if save == "hadith":
     message = random.choice(hadith_quotes)
    elif save == "quran" :
         message = random.choice(quran_success_quotes)
    elif save == "anime" :
        message = random.choice(anime_style_quotes)
    elif save == "islamic" :
         message = random.choice(islamic_quotes)       
    elif save == "mindset" :
         message = random.choice(mindset)
    elif save == "athletes" :
         message = random.choice(athletes_quotes)
    else:
         message = random.choice(random_quote)          

    return render_template ("quote.html" ,motivation= message)


@app.route("/preference")
def choose ():

    return render_template ("preference.html")


@app.route("/save_preference" , methods = ['POST'])
def save ():
    prefrence = request.form['Category']
    session['category'] = prefrence
    return redirect ("/")
    



if __name__ == "__main__" :
    app.run(debug=True)