import redis

# Подключение к Redis-серверу (по умолчанию localhost и порт 6379)
client = redis.StrictRedis(host='localhost', port=6379, db=0)

try:
    # Установим значение ключа
    client.set('mykey', 'Hello Redis')
    print("Key 'mykey' has been set to 'Hello Redis'.")

    # Получим значение ключа
    value = client.get('mykey')
    print(f"The value of 'mykey' is: {value.decode('utf-8')}")

except Exception as e:
    print(f"An error occurred: {e}")

