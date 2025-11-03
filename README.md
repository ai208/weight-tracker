# weight-tracker
体重記録とBMI計算のDjangoアプリ


### 1. GitHub からプロジェクトを取得

```bash
git clone https://github.com/ai208/weight-tracker.git
cd weight-tracker
```

### 2. 最新の変更を取得（すでに clone 済みの場合）

```bash
git pull origin main
```

### 3. Python 仮想環境を作成して有効化

```bash
python -m venv venv
```

*   Windows:
    ```bash
    .\venv\Scripts\activate
    ```
*   Mac/Linux:
    ```bash
    source venv/bin/activate
    ```

### 4. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

※ `requirements.txt` がない場合は、元のPCで以下のコマンドで作成できます：

```bash
pip freeze > requirements.txt
```

### 5. Django のマイグレーションと起動

```bash
python manage.py migrate
python manage.py runserver
```

***


