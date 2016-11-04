if __name__ == "__main__":
    print("starting flask application !!")
    from app import app

    app.run(debug=True)
    print("stopping flask application !!")
