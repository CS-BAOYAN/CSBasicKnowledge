from flask import Flask, jsonify
from user import User
"""
接口说明：
1.返回的是json数据
2.结构如下：
{
    res_code: 0, 不是0就是错误
    data: 数据的位置，一般是数组
    message: '对本次请求的说明'
}
"""
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    user = User()
    data = user.get_user_info()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2002, debug=True)
