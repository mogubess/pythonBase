import contextlib

def is_ok_job():
    try:
        print('do somthing')
        raise Exception('error')
        return True
    except Exception:
        return False

def cleanup():
    print('clean up')

# try:
#     is_ok = is_ok_job()
#     print('more task')
# finally:
#     if not is_ok:
#         cleanup()

# with statment内で、最初にstack.callback(cleanup)に関数を登録して
# withを出るまでに、stack.pop_all()がコールされなければ、最初に登録された
# cleanup関数がコールされる、2つ登録された場合は、あといれから呼ばれる、stackだけに
with contextlib.ExitStack() as stack:
    stack.callback(cleanup)

    @stack.callback
    def cleanup2():
        print('cleanup2')

    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        stack.pop_all()

# out ---
# do somthing
# more task
# cleanup2
# clean up
