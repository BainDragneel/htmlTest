
# 注册接口路由

def create_route(app):
    @app.get("/test")
    def root():
        return {"ok": "true"}

    @app.get("/hello")
    def root():
        return {"hello": "tianHang"}
