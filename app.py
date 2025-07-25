from flask import *

class Server:
    def __init__(self, name):
        self.app = Flask(name)
        
        @self.app.route("/")
        def rota():
            return self.Rota()
        
    def Rota(self):
        return "oiiii"
    
    def Run(self):
        self.app.run(debug=True)
    
def main():
    server = Server(__name__)
    server.Run()
    
if __name__ == "__main__":
    main()
        