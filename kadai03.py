import eel

@eel.expose
def from_js_call_python(val_from_js):
  print('スタート！')
  print(f'jsから取得したキーワード={val_from_js}')
  
eel.init('web')

eel.start("index.html",port=9999)

