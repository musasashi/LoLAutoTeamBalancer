このファイルは、AutoTeamBalancerのREADME.txtです。

このソフトウェアはオープンソースで、誰でも自由に書き換えたり、譲渡することができます。
ただし、このソフトウェアを使用する際に不具合が起きた場合、作者は一切の責任を負いません。自己責任でご利用ください。


■実行環境の作成
このソフトウェアを実行するにはpython実行環境が必要です。
ライブラリはpython標準ライブラリの他にはstreamlitのみを使っています。

https://www.python.org/downloads/release/python-31011/
上のwebサイトからWindows installer (64-bit)をダウンロードしてインストールを実行してください。

またインストール途中でpythonをpathに追加するかどうか問われるので追加するようチェックボックスを入れるのがおススメです。

インストールが終わったらコマンドプロンプトを起動し以下のコマンドを実行して、バージョン情報が表示されれば
pythonのインストールは完了です。
>> python --version

次にstreamlitのインストールをします。
以下のコマンドを実行すると自動的にstreamlitが実行されます。
>> pip install streamlit


■使い方
まずはPlayerStats.jsonをテキストエディタで開いてください。
player_statsは各プレイヤーのレーン毎の大体の強さです。
強さはランクで示し、adc, jug, mid, sup, topのランクを記載してください。

PlayerStats.jsonの編集が終わったら、コマンドプロンプトで以下のコマンドを実行するとアプリケーションが起動します。
>> python main.py

更にOptimizationParams.jsonを編集することで
レーン毎の影響力を設定したり、ランクと強さの関係を変更することができます。
