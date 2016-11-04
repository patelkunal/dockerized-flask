from service.app import app

if __name__ == "__main__":
    print("starting flask application !!")
    app.run(debug=True)
    print("stopping flask application !!")
