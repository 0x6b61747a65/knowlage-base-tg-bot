# Telegram knowlege database bot

## External libs used

- aiogram
- psycopg2

## Server setup

1. Set environmental variable txt on server

    ```bash
    cat >> env_file.txt << EOF
    TOKEN=123456:abcdefg1234567890
    DB_NAME=dbname
    DB_USERNAME=username
    DB_PASSWORD=dbpassword
    EOF
    ```

2. Run `env_export_script.sh` script

    ```bash
    source env_export_script.sh env_file.txt
    ```

3. Start `venv`

    ```bash
    python3 -m venv venv
    ```

    ```bash
    source venv/bin/activate
    ```

4. Install requirements

    ```bash
    pip install -r requirements.txt
    ```
