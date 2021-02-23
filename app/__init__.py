from fastapi import FastAPI, routing


# 生成一个服务启动的 app 实例
def create_app():
    # 生成实例
    app = FastAPI()

    # 返回实例
    return app
