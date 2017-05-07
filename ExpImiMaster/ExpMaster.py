from flask import Flask, render_template, make_response, redirect, url_for,request
from flask_mongoengine import MongoEngine
from flask import jsonify
import threading
import camera
from camera import camera_oprate
import wx

app = Flask(__name__)
db = MongoEngine(app)
app1 = wx.App()
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
}

@app.route('/',methods=['POST', 'GET'])
def overview():
    return render_template('Overview.html',user='Hacks')

'''The route to for the reclaimed bonding groups web page'''
@app.route('/expression1',methods=['POST', 'GET'])
def expression1():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression1score',methods=['POST', 'GET'])
def expression1score():
    global score
    print score
    return render_template('comperisonScore.html', user='Hackx', scores=score)


@app.route('/expression2',methods=['POST', 'GET'])
def expression2():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression2score',methods=['POST', 'GET'])
def expression2score():
    global score
    print score
    return render_template('comperisonScore2.html', user='Hackx', scores=score)


@app.route('/expression3',methods=['POST', 'GET'])
def expression3():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression3score',methods=['POST', 'GET'])
def expression3score():
    global score
    print score
    return render_template('comperisonScore3.html', user='Hackx', scores=score)

@app.route('/expression4',methods=['POST', 'GET'])
def expression4():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression4score',methods=['POST', 'GET'])
def expression4score():
    global score
    print score
    return render_template('comperisonScore4.html', user='Hackx', scores=score)


@app.route('/expression5',methods=['POST', 'GET'])
def expression5():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression5score',methods=['POST', 'GET'])
def expression5score():
    global score
    print score
    return render_template('comperisonScore5.html', user='Hackx', scores=score)


@app.route('/expression6',methods=['POST', 'GET'])
def expression6():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression6score',methods=['POST', 'GET'])
def expression6score():
    global score
    print score
    return render_template('comperisonScore6.html', user='Hackx', scores=score)


@app.route('/expression7',methods=['POST', 'GET'])
def expression7():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression7score',methods=['POST', 'GET'])
def expression7score():
    global score
    print score
    return render_template('comperisonScore7.html', user='Hackx', scores=score)


@app.route('/expression8',methods=['POST', 'GET'])
def expression8():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression8score',methods=['POST', 'GET'])
def expression8score():
    global score
    print score
    return render_template('comperisonScore8.html', user='Hackx', scores=score)

@app.route('/expression9',methods=['POST', 'GET'])
def expression9():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression9score',methods=['POST', 'GET'])
def expression9score():
    global score
    print score
    return render_template('comperisonScore9.html', user='Hackx', scores=score)


@app.route('/expression10',methods=['POST', 'GET'])
def expression10():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression10score',methods=['POST', 'GET'])
def expression10score():
    global score
    print score
    return render_template('comperisonScore10.html', user='Hackx', scores=score)

@app.route('/expression11',methods=['POST', 'GET'])
def expression11():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression11score',methods=['POST', 'GET'])
def expression11score():
    global score
    print score
    return render_template('comperisonScore11.html', user='Hackx', scores=score)


@app.route('/expression12',methods=['POST', 'GET'])
def expression12():
    picture_num = request.form['picture']
    print picture_num
    global score
    score = camera_oprate(int(picture_num),app1)
    print score
    resp = make_response(jsonify({
        'success': True,
        'type': 'success',
        'message': 'successfully'
    }))
    return resp

@app.route('/expression12score',methods=['POST', 'GET'])
def expression12score():
    global score
    print score
    return render_template('comperisonScore12.html', user='Hackx', scores=score)



'''The thread for web part will start firstly'''
if __name__ == '__main__':
    app.run(port=8091)
