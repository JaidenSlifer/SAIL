import sys
from server import ServerController

help = """
  python sail.py [-h] <command> [<args>]

  commands:
    run: starts a Flask development server
    train: NOT IMPLEMENTED
    save: NOT IMPLEMENTED
    
  options:
    run
      -d: enable debug mode on flask server
"""
if __name__ == '__main__':
  quit = False
  while not quit:
    args = sys.argv[1:]
    for arg in args:
      if(arg == '-h'):
        print(help)
        quit = True
        break
      if(arg == 'run'):
        debug = False
        if(args[1] and args[1] == '-d'):
          debug = True
        server = ServerController('sail')
        server.init_routes()
        server.run(debug)
        quit = True
      elif(arg == 'train'):
        raise NotImplementedError
      elif(arg == 'save'):
        raise NotImplementedError
      else:
        print("Command not recognized")
        quit = True
        break