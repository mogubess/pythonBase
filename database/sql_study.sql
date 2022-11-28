-- 定義部分
CREATE TABLE members
    (
        id     INTEGER NOT NULL,
        name   CHAR(32),
        height REAL,
        weight REAL,
        age INTEGER,
        job_id INTEGER,
        PRIMARY KEY (id)
    )
;

CREATE TABLE jobs
    (
        id     INTEGER NOT NULL,
        name   CHAR(32),
        salary INTEGER,
        PRIMARY KEY (id)
    )
 ;

-- 入力部分
INSERT
    INTO members(id, name, height, weight, age, job_id)
    VALUES
        (1, '佐藤', 170.2, 65.2, 60, 4),
        (2, '鈴木', 151.5, 50.3, 53, 2),
        (3, '高橋', 182.1, 85.1, 31, 8),
        (4, '田中', 163.5, 70.6, 36, 3),
        (5, '渡辺', 157.8, 55.8, 62, 7),
        (6, '伊藤', 173.0, 65.3, 75, 1),
        (7, '山本', 166.4, 49.1, 25, 5),
        (8, '中村', 144.1, 56.9, 45, 7),
        (9, '小林', 168.7, 90.1, 38, 3),
        (10, '加藤', 178.6, 78.5, 26, 6)
;
        
INSERT
    INTO jobs(id, name, salary)
    VALUES
        (1, '医師', 1232),
        (2, '弁護士', 1028),
        (3, 'SE', 515),
        (4, '会計士', 1024),
        (5, '薬剤師', 542),
        (6, '保育士', 341),
        (7, '大学教授', 1050),
        (8, '塾講師', 361)
;


/*input***************************************************************/
SELECT name, salary FROM jobs;
/*output***************************************************************/
name	salary
医師	1232
弁護士	1028
SE	515
会計士	1024
薬剤師	542
保育士	341
大学教授	1050
塾講師	361

/*input***************************************************************/
SELECT COUNT(*) AS "30歳以上かつ身長170cm以上の人数" FROM members WHERE age >= 30 AND height >= 170;
/*output***************************************************************/
30歳以上かつ身長170cm以上の人数
3

/*input***************************************************************/
SELECT name, age FROM members ORDER BY age DESC;
/*output***************************************************************/
name	age
伊藤	75
渡辺	62
佐藤	60
鈴木	53
中村	45
小林	38
田中	36
高橋	31
加藤	26
山本	25

/*input***************************************************************/
SELECT job_id, AVG(height) FROM members GROUP BY job_id;
/*output***************************************************************/
job_id	AVG(height)
4	170.2
2	151.5
8	182.1
3	166.1
7	150.95
1	173
5	166.4
6	178.6

/*input***************************************************************/
⑤職種ごとの平均身長が170cmよりも高い職種と、その職種ごとの平均身長を取得してみよう！
SELECT job_id, AVG(height) FROM members GROUP BY job_id HAVING AVG(height) > 170;
/*output***************************************************************/
job_id	AVG(height)
4	170.2
8	182.1
1	173
6	178.6


/*input***************************************************************/
SELECT members.name, jobs.salary FROM members INNER JOIN jobs ON jobs.id = members.job_id WHERE jobs.salary >= 1000 ORDER BY jobs.salary DESC;
/*output***************************************************************/
name	salary
伊藤	1232
渡辺	1050
中村	1050
鈴木	1028
佐藤	1024


/*input***************************************************************/
①体重が50kg以上かつ年収が500万円以上かつ年齢が40歳未満の人の名前を取得

得たい結果
name
田中
小林

SELECT members.name FROM members INNER JOIN jobs ON jobs.id = members.job_id WHERE members.weight >= 50 AND jobs.salary >= 500 AND members.age < 40;
/*output***************************************************************/
name
田中
小林

/*input***************************************************************/
②BMIが22以下の人の名前、身長、体重、BMIをBMIが低い順に取得
ただしBMIは以下の計算式で求められる（BMI＝ 体重kg ÷ 身長m ÷ 身長m）
SELECT members.name AS "名前", members.height AS "身長", members.weight AS "体重", members.weight/(members.height/100)/(members.height/100) AS "BMI" FROM members WHERE members.weight/(members.height/100)/(members.height/100) <= 22
/*output***************************************************************/
名前	身長	体重	BMI
鈴木	151.5	50.3	21.915062793408055
伊藤	173	65.3	21.818303317852248
山本	166.4	49.1	17.7326992418639


/*input***************************************************************/
jobsテーブルに新しい職業を追加してみよう！（id=9であればその他は自由）

INSERT INTO jobs(id, name, salary) VALUES (9, '政治家', 2000);
SELECT * FROM jobs;
/*output***************************************************************/
id	name	salary
1	医師	1232
2	弁護士	1028
3	SE	515
4	会計士	1024
5	薬剤師	542
6	保育士	341
7	大学教授	1050
8	塾講師	361
9	政治家	2000


/*input***************************************************************/
INSERTの演習で追加した新しい職業の年収を100万円増やしてみよう！

UPDATE jobs SET salary = salary + 100 WHERE id = 9;
SELECT * FROM jobs;
/*output***************************************************************/
id	name	salary
1	医師	1232
2	弁護士	1028
3	SE	515
4	会計士	1024
5	薬剤師	542
6	保育士	341
7	大学教授	1050
8	塾講師	361
9	政治家	2100

/*input***************************************************************/
membersテーブルにおいて身長が180cm以上、または体重が50kg以下のレコードを削除してみよう！

DELETE FROM members WHERE height >= 180 OR weight <= 50;
SELECT * FROM members;
/*output***************************************************************/
id	name	height	weight	age	job_id
1	佐藤	170.2	65.2	60	4
2	鈴木	151.5	50.3	53	2
4	田中	163.5	70.6	36	3
5	渡辺	157.8	55.8	62	7
6	伊藤	173	65.3	75	1
8	中村	144.1	56.9	45	7
9	小林	168.7	90.1	38	3
10	加藤	178.6	78.5	26	6

/*部分一致検索***************************************************************/

■条件式を簡単に書く（LIKE・IN・BETWEEN）
WHERE句の中に条件式を書くには比較演算子を使ったが、ほかの書き方もある
・LIKE
文字列の部分一致検索をするにはLIKEを使う
部分一致　⇒　指定した文字が含まれていること

例：TシャツとYシャツの値段を取得する
SELECT name, selling_price FROM Products WHERE name LIKE '%シャツ';


「%」は「0字以上の任意の文字列」を意味する記号
上記の例の場合、「%シャツ」は「”シャツ”で終わるすべての文字列」という意味

部分一致には前方一致・中間一致・後方一致の3種類がある
前方一致：文字列の最初に指定した文字が含まれている（<検索する文字>%）
中間一致：文字列のどこかに指定した文字が含まれている（%<検索する文字>%）
後方一致：文字列の末尾に指定した文字が含まれている（%<検索する文字>）

Point!
「%」を適切に使用して正しく部分一致検索できるようになろう！


/*input***************************************************************/
SELECT name, selling_price FROM Products WHERE category LIKE '%用品' ORDER BY selling_price DESC;

/*output***************************************************************/
name	selling_price
プリンター	9800
圧力鍋	5900
包丁	1200
コピー用紙	500
カッター	130
ボールペン	100


・BETWEEN
範囲検索を行うにはBETWEENを使う
範囲検索　⇒　上限と下限の値を設定した検索

例：販売価格が500円から2000円までの商品名を取得
SELECT name, selling_price FROM Products
WHERE selling_price BETWEEN 500 AND 2000;


比較演算子を使うと以下のように表現できる
SELECT name, selling_price FROM Products
WHERE selling_price >= 500 AND selling_price <= 2000;


BETWEENを使った場合は両端の値を含むことに注意が必要
上の例で500円と2000円ちょうどの商品を含みたくないときは、
BETWEENを使わずに以下のように書く
SELECT name, selling_price FROM Products
WHERE selling_price > 500 AND selling_price < 2000;


Point!
ANDを忘れずに！
BETWEENを使うと上限と下限の値が含まれることに注意！


/*input***************************************************************/
SELECT name, cost_price FROM Products WHERE cost_price BETWEEN 100 AND 450;

/*output***************************************************************/
name	cost_price
包丁	400
Yシャツ	300
コピー用紙	200


・IN
ORで複数の条件式をつなぐ必要がある場合はINを使うとスッキリ書ける

例：販売価格が100円、2300円、9800円の商品の名前と値段を取得する
ORを使った場合
SELECT name, selling_price FROM Products
WHERE selling_price = 100
   OR selling_price = 2300
   OR selling_price = 9800;


INを使った場合
SELECT name, selling_price FROM Products
WHERE selling_price IN (100, 2300, 9800);


反対に、販売価格が100円、2300円、9800円以外の
商品を選択したいときはNOT INを使う

例：販売価格が100円、2300円、9800円以外の商品の名前と値段を取得する
INを使った場合
SELECT name, selling_price FROM Products
WHERE selling_price NOT IN (100, 2300, 9800);


ORを使った場合
SELECT name, selling_price FROM Products
WHERE selling_price != 100
   OR selling_price != 2300
   OR selling_price != 9800;



Point!
「IN (値1, 値2, … )」という形を覚えよう！

/*input***************************************************************/
SELECT name, (cost_price/selling_price)*100 AS "原価率" FROM Products WHERE selling_price NOT IN (100 ,500,1500);

/*output***************************************************************/

name	原価率
包丁	33.3333
Yシャツ	13.0435
圧力鍋	33.8983
カッター	38.4615
プリンター	28.5714