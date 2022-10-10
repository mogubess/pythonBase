import contextlib
import os

# try exceptでイベントを受けた時にexceptで何の処理もしないときにコードを短縮する方法
# エラー抑圧処理

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')
