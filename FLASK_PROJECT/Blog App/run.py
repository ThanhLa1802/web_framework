#create by:thanh.la - 07-09- 2021
from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)