import contextlib
import logging
import sys


#標準出力を、ファイルにリダイレクトするための処理
# with open('stdout.log', 'w') as f:
#     with contextlib.redirect_stdout(f):
#         print('hello')
#         # help(sys.stdout)

#標準エラー出力
with open('stderr.log','w') as f:
    with contextlib.redirect_stderr(f):
        logging.error('Error!')
        

