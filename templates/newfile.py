import subprocess
import sys
import os

def install_flask_fix():
    # 国内清华大学镜像源
    index_url = "https://pypi.tuna.tsinghua.edu.cn/simple"
    
    print("检测到网络连接问题，正在尝试使用清华镜像源安装...")
    
    # 构造安装命令
    # --trusted-host 确保在没有 SSL 证书时也能信任该源
    command = [
        sys.executable, "-m", "pip", "install", 
        "flask", 
        "-i", index_url,
        "--trusted-host", "pypi.tuna.tsinghua.edu.cn"
    ]
    
    # 临时禁用环境变量中的代理设置（防止 pip 走报错的代理）
    env = os.environ.copy()
    env.pop("http_proxy", None)
    env.pop("https_proxy", None)
    env.pop("HTTP_PROXY", None)
    env.pop("HTTPS_PROXY", None)

    try:
        subprocess.check_call(command, env=env)
        print("\nFlask 安装成功！")
    except subprocess.CalledProcessError as e:
        print(f"\n安装仍然失败。这通常是因为您的办公网络或防火墙彻底断开了连接。")
        print("建议操作：请检查您的 VPN 或代理软件是否开启，或者尝试关闭它们后再运行。")

if __name__ == "__main__":
    install_flask_fix()