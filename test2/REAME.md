Pytestのまとめ
https://mogubess.hatenablog.com/entry/2022/09/25/014708

・インストール
pip install pytest

・コマンド打鍵
pytest {ディレクトリパス} -k {クラス名/メソッド名}
・オプション
 -s 標準出力
 -r 詳細情報表示(SKIPの理由など)



・関数名の先頭を"test"にすればテスト関数として認識してくれる
def test_*************():
  ******
  assert add(1,2) == 3   #OKパターン

・クラスで宣言する場合Testが先頭につくクラス名をつける
class TestCall(object):
    def test_save(self, tmpdir):
        cal = Cal()
        cal.save(tmpdir, self.test_file_name)
        print(tmpdir)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

・pytestで例外
with pytest.raise(ValueError):
  add("1","1") #文字列どおしの演算でValueErrorを出すとする
  #ValueErrorが発生すれば、テストとしては合格

・pytestのクラスの開始終了、メソッドの開始終了時に呼ばれるメソッド
クラスの開始前に呼び出される
    @classmethod
    def setup_class(cls):
        pass
クラスの終了後に呼び出される
    @classmethod
    def teardown_class(cls):
        pass
メソッドの開始前に呼び出される（引き数はmethod名）
    def setup_method(self,method):
        pass
メソッドの開始後に呼び出される（引き数はmethod名）
    def teardown_method(self,method):
        pass

・テストのSKIP設定
@pytest.mark.skip(reason='skip!')

変数"is_Release"がTrueならばテスト実行
@pytest.mark.skipif(is_Release==True,reason='skip!')

・conf_test.pyが同じディレクトリないにあれば、そちらを先にみて、各種fixtureを設定できる

conftest.pyの記述

・def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os_name')

上記のように記述をすれば
> pytest --helpと打鍵すると

custom options:
  --os-name=OS_NAME     os_name
と出力されてpytestで、--os-name=macと渡せる。

テスト側で受け取るには、fixtureの中にrequestと定義して、以下のように取り出す
  def test_add(self,request):
    os_name = request.config.getoption('--os-name')
    print(f'method=ada start os {os_name}')

fixtureは他に以下がある
 available fixtures: _xunit_setup_class_fixture_TestCall, _xunit_setup_method_fixture_TestCall, anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, cov, csv_file, doctest_namespace, monkeypatch, no_cover, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, testrun_uid, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, worker_id

pytest --fixtures
で各詳細がわかる

・tmpdirのfixture
一時ディレクトリとして用意してくれて、テスト終了後に自動で消去
一時ディレクトリにファイルなどを作成するなどができる

    def test_save(self, tmpdir):
        cal = Cal()
        cal.save(tmpdir, self.test_file_name)
        print(tmpdir)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

・独自のfixtureを作成する　@pytest.fixture

@pytest.fixture
def csv_file(tmpdir):
    with open(tmpdir, 'w+') as c:
        yield c

class TestHogeHoge:
    def test_add(self,csv_file):
        print(f'csv_file {csv_file}')

@fixtureの "yield c"とcsvfileをコールしたときに、cで処理を実施できるすることで実現できるので、
テスト時にファイルを開いて閉めるといった処理が必要なくなる


