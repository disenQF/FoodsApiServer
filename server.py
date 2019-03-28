from app import app
from views import cate_view, foods_view

app.register_blueprint(cate_view.blue)
app.register_blueprint(foods_view.blue)

if __name__ == '__main__':
    app.run()
