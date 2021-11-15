import eel
import csv
import datetime
import traceback
import socket 

LOG_FILE_PATH = "./log/log_{datetime}.log"
log_file_path = LOG_FILE_PATH.format(
    datetime=datetime.datetime.now().strftime('%Y-%m-%d'))
#log出力関数
def make_log(txt):
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    logStr = '[%s:%s] %s' % ('log', now, txt)
    #ファイルに出力
    with open(log_file_path, 'a', encoding='utf-8_sig') as f:
        f.write(logStr + '\n')
    print(logStr)
    
@eel.expose #これでjsから呼び出せるようになる
def python_function(search_char, fileName):
  try:
    char_list = []
    with open(fileName, 'r', encoding="utf-8_sig") as csv_file:
      char_list = csv_file.read().splitlines()
    # print(char_list)
    if search_char in char_list:
      res = f'「{search_char}」はいます'
    else:
      res = f'「{search_char}」はいません。' + '\n' + f'「{search_char}」を追加します。'
      char_list.append(search_char)
      with open(fileName,"w", newline="", encoding="utf-8_sig") as csv_file:
        csv_file.write("\n".join(char_list))
        make_log(f'{search_char}をファイルに追加')
    make_log('検索終了')
    return res
  except:
    make_log('検索失敗')
    
eel.init("web")
# 未使用ポート取得
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
port = s.getsockname()[1]
s.close()
web_app_options = {
  "mode": "chrome",
  "port": port,
  "chromeFlags": [
    "--window-size=800,600",
    "--window-position = 0,0",
  ]
}
eel.start("index.html", suppress_error=True, options=web_app_options)

# eel.start("index.html")
make_log('idex.html起動')
