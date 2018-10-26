from flask import Flask, render_template, redirect

app = Flask(__name__)

counts = {
    'get' : 0,
    'post' : 0,
    'delete' : 0,
    'put' : 0
}

@app.route('/')
def index():
    global counts
    return render_template('index.html', counts=counts)

@app.route('/request_counter', methods=['POST'])
def post_couter():
    global counts
    counts['post'] += 1
    return redirect('/')

@app.route('/request_counter', methods=['GET'])
def get_couter():
    global counts
    counts['get'] += 1
    return render_template('request.html')

@app.route('/request_counter', methods=['DELETE'])
def delete_couter():
    global counts
    counts['delete'] += 1
    return redirect('/')

@app.route('/statistics')
def statistics():
    with open("request_counts.txt", "w") as fo:
        fo.write(str(counts))
    text = open('request_counts.txt', 'r+')
    content = text.read()
    return render_template('statistics.html', text = content)

if __name__ =='__main__':
    app.run(
        debug=True
    )