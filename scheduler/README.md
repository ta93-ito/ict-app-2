ユーザー入力をGUIで受けるため、一つのホストに参加者らが実地で入力していくようなユースケースとし、大まかなフローはイベント作成(主催者)→日程へ投票(参加者ら)→集計(主催者)のように実装する。
基本的に一つのウィンドウ上で画面遷移を実現する。

## 実装計画

- イベント作成画面(主催者)
    - タイトル、複数候補日程(tkcalendar)とメモ
        - バリデーション
            - `候補日程リスト.length > 1`
            - `候補日程 is unique`
            - `タイトル is not null`
    - 日程調整を開始するボタン
- 日程登録画面(参加者)
    - 名前入力(not null)
    - 候補日程リストのフォーム
        - デフォルト値はfalse
    - 集計するボタン
- 集計結果画面
    - 日程一覧と結果リスト表示。最大のものをハイライトする
