# ros2_communicationコマンド
![test](https://github.com/fjord-takuto/mypkg2/actions/workflows/test.yml/badge.svg)(https://github.com/fjord-takuto/mypkg2/actions/workflows/test.yml)

端末1のtalker側で標準入力した文字を、端末2のlistener側に送信する。

## 使い方
- Code（緑のボタン）をクリック
- HTTPSをクリックし、URLをコピー
- 任意のディレクトリを用意し、`git clone <コピーしたURL>`を実行
- 端末1
```
colcon build
source install/setup.bash
ros2 run mypkg talker
[INFO] [1767860777.136012165] [keyboard_talker]: 入力してください（qで終了）
>> hello
[INFO] [1767860785.146372196] [keyboard_talker]: Sent: "hello"
>> q
[INFO] [1767860788.559070986] [keyboard_talker]: 終了します
```
- 端末2
```
colcon build
source install/setup.bash
ros2 run mypkg listener
[INFO] [1767860785.162654679] [keyboard_listener]: Received: "hello"
^C
```
 
## 必要なソフトウェア	
- Ros2
  - テスト済みバージョン：jazzy
- Python
  - テスト済みバージョン：3.13

## テスト環境
- Ubuntu24.04.1LTS

## 権利関係
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。[ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025)
- © 2025 Takuto Irie
