from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',methods=['GET'])


@app.route('/get_post',methods=['GET','POST'])
def get_post():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        ratings = request.form['rating']
        review = request.form['comment']
        
        print(f'Name:  {name}')
        print(f'Email:  {email}')
        print(f'Rating:  {ratings}')
        print(f'Review:  {review}')

    return render_template('post_form.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')