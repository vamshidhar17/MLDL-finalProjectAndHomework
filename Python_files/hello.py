from flask import Flask,jsonify, request, render_template,json
app = Flask(__name__)
ant="asdfghjklqwertyuiop"

@app.route("/")
def hello():
    return render_template("index.html", a=ant)
@app.route('/op', methods=['POST'])
def sum_num():
 
    rf=request.form
 
    for key in rf.keys():
        data=key
    print(data[0])
    
    data_dic=json.loads(data)
    print(data_dic['str'],12234)
    print(data_dic.keys())
    sum_data = data_dic['str']
    
    
    resp_dic={'str':data_dic['str']}
    resp = jsonify(resp_dic)
    resp.headers['Access-Control-Allow-Origin']='*'
    return resp

if __name__ == "__main__":
    #print("hi")
    app.run()
