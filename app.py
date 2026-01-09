import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# 设置你想让用户下载的文件夹路径，'.' 表示当前文件夹
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'files_to_download')

# 如果文件夹不存在则创建它
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def index():
    # 获取文件夹下的所有文件（排除 Python 脚本本身）
    files = [f for f in os.listdir(DOWNLOAD_FOLDER) if os.path.isfile(os.path.join(DOWNLOAD_FOLDER, f))]
    return render_template('index.html', files=files)

@app.route('/download/<path:filename>')
def download_file(filename):
    # 安全地发送文件
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    # 从环境变量获取端口，如果没有（比如在本地运行），则默认使用 8080
    port = int(os.environ.get('PORT', 8080))
    
    # 这里的 host 必须是 '0.0.0.0'，port 必须使用变量
    app.run(host='0.0.0.0', port=port)
