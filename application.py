from flask import Flask, render_template, request, send_from_directory
import requests # Webサービスにデータを送って結果を受信するため
import time 

app = Flask(__name__,
            static_url_path='',
            static_folder='static')

@app.route('/homepage')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST', 'GET'])
def input_form():
    query = request.form['query']
    url = f"https://api.cognitive.microsoft.com/bing/v7.0/search?q={query}"
    # time.sleep(3) # 3秒待つ
    headers = {"Ocp-Apim-Subscription-Key" : SUBSCRIPTION_KEY} # HTTPリクエストのヘッダにAPIキーを含める
    response = requests.get(url, headers=headers) # 実際にリクエストを送る．　ちなみに，このセルを実行するごとにお金がかかっています．
    newsdata = response.json() # 取得した結果をJSON形式として読み込み
    print(newsdata['webPages']) #返ってきたjsonを表示
    newsdata = newsdata['webPages']['value']# 取得した結果をJSON形式として読み込み
    
    return render_template("result.html", query=query, response=newsdata)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='18102')
