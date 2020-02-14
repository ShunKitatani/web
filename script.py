#! /usr/bin/env python3

import sys
import io
from food import Food
from drink import Drink


food1 = Food('サンドイッチ', 500, 330)
food2 = Food('チョコケーキ', 400, 450)
food3 = Food('シュークリーム', 200, 180)

foods = [food1, food2, food3]

drink1 = Drink('コーヒー', 300, 180)
drink2 = Drink('オレンジジュース', 200, 350)
drink3 = Drink('エスプレッソ', 300, 30)

drinks = [drink1, drink2, drink3]

print('食べ物メニュー')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('飲み物メニュー')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('食べ物の番号を選択してください: '))
selected_food = foods[food_order]

drink_order = int(input('飲み物の番号を選択してください: '))
selected_drink = drinks[drink_order]

# コンソールから入力を受け取り、変数countに代入してください
count = int(input('何セット買いますか？(3つ以上で1割引): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
selected_food.get_total_price(count)
selected_drink.get_total_price(count)
result = selected_food.get_total_price(
    count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
print('合計は' + str(result) + '円です')


# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print("Content-type: text/html; charset=utf-8")

# print(“””  “””)で囲んだ部分にhtmlを書く。printでHTMLコードを表示させることで、ブラウザがHTMLコードとして認識してくれる。
print(
    """
     <html>
       <head>
           <meta http-equiv=\"Content-Type\" content=\ "text/html
           charset=utf-8\" / >
</head>
     <body>
       <header>
    <ul>
      <li><a href="#Who am I">Who am I</a></li>
      <li><a href="#Background">Background</a></li>
      <li><a href="#Strength">Strength</a></li>
      <li><a href="#Vision">Vision</a></li>
      <li><a href="#Achivements">Achivements</a></li>
      <li><a href="#Contact">Contact</a></li>
    </ul>
  </header>
  <div class="top-page">
    <a name="Who am I">
      <img class="top-left" src="IMG_3966.JPG">
      <h1 id="any">Thank you for <br> visiting my website</h1>
      <div class="top-right">
        <h2 id="some">Who am I ?</h2>
        <p>初めまして。　2020年2月現在立命館大学経営学部の２回生の北谷駿です。</p>
        <p>趣味はスポーツ全般と読書です。　主にサッカー、スノボーなどが好きです。　サッカーに関しては小学1年生から高校三年生まで12年間していました。</p>
        <p>読書はビジネス書から食べ物や睡眠、集中力に関するものまで幅広く読んでいます。　</p>
        <p>大学に入ってからはサッカーをやめなかなかやりたいことがみつからず悶々とした日々を送っていました。　それでもやりたいことを探しつずけた結果データサイエンティストになるという目標ができ日々奮闘中です。</p>
        <p>去年の8月から今年の1月にはマレーシアに留学していました。そこで英語はもちろん多文化社会や宗教について学び、自分の価値観を広げることができました。
      </p>
      </div>
    </a>
  </div>

  <div class="background">
    <a name="Background">
      <h1>Background</h1>
      <div class="back-left">
        <ul>
          <li>7歳　サッカーに出会う</li>
          <li>15歳　草津東高校入学</li>
          <li>18歳　立命館大学入学</li>
          <li>20歳　マレーシア留学、未来電子でマーケティングとプログラミングのインターン開始</li>
        </ul>
      </div>
      <div class="back-right">
        <img class="image" src="IMG_2940.jpg">
      </div>
    </a>
  </div>

  <div class="strength">
    <a name="Strength">
      <h1>Strength</h1>
      <div class="action">
        <h2>行動力</h2>
        <p>行動力があることで何事にも挑戦することができます。何事にも挑戦することができるということは、多くの経験を積むことができるということです。加えて無駄な悩み事もしません。悩んでる暇があるなら行動しようと心がけているので、時間を無駄に使わずに日々過ごすことができています。</p>
      </div>
      <div class="positive">
        <h2>失敗をポジティブに捉えることができる</h2>
        <p>
          失敗をポジティブに捉えることができると無駄に落ち込む時間がありませんし失敗を学びにして次に活かすことができます。加えて成功するまでつずけることができます。
         </p>
      </div>
      <div class="think">
        <h2>考えることが好き</h2>
        <p>考えることが好きであるというのはつまり毎日悩むのではなくどうすればよりよくなるかと考えることで、日々状況によって適切な行動に変更し、毎日のやることの精度が高くなります。日々のやることの精度が高くなるとおのずと結果は付いてくると思います。実際に日々考え続けた結果データサイエンティストという職業に行きつくことができました。</p>
      </div>
    </a>
  </div>

  <div class="vision">
    <a name="Vision">
      <h1>Vision</h1>
      <h2>データサイエンティストになること</h2>
      <p>大学に入ってからは僕の人生の一部だったサッカーをやめました。</p>
      <p>サッカーをやめて以来やりたいことがみつからず悶々とした日々を送っていました。</p>
      <p>ですがやりたいことを探しつずけデータサイエンティストになることという目標ができました。</p>
      <p>なりたい理由はまずビジネスが好きだということ。一時期はエンジニアを目指していたけれどもっとビジネスに影響を与えてビジネスに深く関われる仕事がしたいと思い、かつプログラミング能力も必要なデータサイエンティストを目指しました。</p>
      <p>私は文系なので学校でデータを扱うことは学べないので、日々自主学習を進めています。
      </p>
      <p>夢はまだありません。夢は何かもっと大きなものであり、やりたいことをに向かって頑張りつずければいつか見つかると信じて日々精進しています。</p>
    </a>
  </div>
  <div class="achivements">
    <a name="Achivements">
      <div class="ahv">
        <h1>Achivements</h1>
        <h2>
          随時更新していきます。
        </h2>

      </div>
    </a>
  </div>

  <footer>
    　　<div class="contact">
      <a name="Contact">
        <label for="yourname">お名前</label>
        <input type="text" name="yourname" placeholder="山田太郎"><br>
        <label for="comment">コメント</label>
        <textarea id="comment" name="comment" placeholder="ここには自由にコメントを記入してください"></textarea>
      </a>
    </div>
  </footer>
  <script>
    'use strict';

    document.getElementById('any').addEventListener('click', () => {
      // document.getElementById('any').style.background = 'red';
      document.getElementById('any').classList.toggle('any');
    });
    document.getElementById('some').addEventListener('click', () => {
        // document.getElementById('any').style.background = 'red';
        document.getElementById('some').classList.toggle('some');
      });
  </script>
</body>
     </body>
     </html>
     """
)
