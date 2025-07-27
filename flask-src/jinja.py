from flask import Flask, render_template, redirect, url_for ,request

'''
{{}} expression to pring output in html
{%...%} condition, loops
{#...#} comment
'''

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

@app.route('/success/<float:score>')
def success(score):
    res = ''

    if score >= 50:
        res = 'Congratulations! Passed'
    else:
        res = 'Sorry! Failed'
    
    exp = {'result':res, 'score':score}

    return render_template('result.html',results=exp)


@app.route('/score_form',methods=['GET','POST'])
def score_form():
    if request.method == 'POST':
        escore = request.form['escore']
        mscore = request.form['mscore']
        
        total_score = float(escore) + float(mscore)
    else:
        return render_template('score_form.html')

    return redirect(url_for('success',score=total_score))
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')