import eel
import csv

@eel.expose #これでjsから呼び出せるようになる
def python_function(search_char, fileName):
  char_list = []
  with open(fileName, 'r', encoding="utf-8_sig") as csv_file:
    char_list = csv_file.read().splitlines()
  # print(char_list)
  if search_char in char_list:
    res = f'「{search_char}」の名前が登場人物リストにありました。'
  else:
    res = f'「{search_char}」の名前が登場人物リストにありませんでした。'
  return res

eel.init("web")
web_app_options = {
  "mode": "chrome-app",
  "port": 9999,
  "chromeFlags": [
    "--window-size=800,600",
    "--window-position = 0,0",
  ]
}
# eel.start("index.html", suppress_error=True, options=web_app_options)

eel.start("index.html")

