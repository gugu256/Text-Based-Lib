from os import system as cmd
from os import listdir as ls
from os import getcwd as pwd
import platform

print("TBLIB's Plugin Manager")
if "tblib.py" not in ls():
  print(f"TBLIB was not found in current directory {pwd()}")
  input("Press Enter to quit./")
  quit()
else:
  pluginName = input("Plugin to add : ")
  cmd("curl https://tblib-docs.devplodocus.repl.co/pluginslist > pluginslist.txt")
  if pluginName in open("pluginslist.txt", "r").read():
    command = "curl tblib-docs.devplodocus.repl.co/plugins/" + pluginName + ".py -L > " + pluginName + ".py"
    cmd(command)
    try:
      open("tblib.py", "a").write("\n" + open(pluginName + ".py", "r").read())
    except FileNotFoundError:
      print("You need to install TBLIB first !")
      input("Press enter to continue./")

    ostype = platform.system()
    if ostype == "Linux" or ostype == "Darwin":
      cmd("rm " + pluginName + ".py")
      cmd("rm pluginslist.txt")
    else:
      cmd("del " + pluginName + ".py")
      cmd("del pluginslist.txt")
    input("Plugin installed successfully!\nPress enter to continue./")
  else:
    print("This plugin doesn't exist")
    input("Press enter to continue./")