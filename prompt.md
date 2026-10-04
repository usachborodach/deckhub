У меня есть mongodb с базой "quote_gun", коллекция "quotes".
В файле "all_quotes.yml" ❗️ все документы оттуда. 
Я нагенерировал картинок для части цитат. А именно для цитат с "_id": ['6aad421d60ac3bd3a3f2f41b', '6aad421d60ac3bd3a3f2f41c', '6aad421d60ac3bd3a3f2f41d', '6aad421d60ac3bd3a3f2f41e', '6aad421d60ac3bd3a3f2f41f', '6aad421d60ac3bd3a3f2f420', '6aad421d60ac3bd3a3f2f421', '6aad421d60ac3bd3a3f2f422', '6aad421d60ac3bd3a3f2f423', '6aad421d60ac3bd3a3f2f424', '6aad421d60ac3bd3a3f2f425', '6aad421d60ac3bd3a3f2f426', '6aad421d60ac3bd3a3f2f427', '6aad421d60ac3bd3a3f2f428', '6aad421d60ac3bd3a3f2f429', '6aad421d60ac3bd3a3f2f42a', '6aad421d60ac3bd3a3f2f42b', '6aad421e60ac3bd3a3f2f42c', '6aad421e60ac3bd3a3f2f42d', '6aad421e60ac3bd3a3f2f42e', '6aad421e60ac3bd3a3f2f42f', '6aad421e60ac3bd3a3f2f430', '6aad421e60ac3bd3a3f2f431', '6aad421e60ac3bd3a3f2f432', '6aad421e60ac3bd3a3f2f433']

Картинки я разместил в файловой системе в папке /root/images/deckhub/
Картинки имеют соотвествующие имена: "6aad421d60ac3bd3a3f2f41d.jpeg" и так далее

В файле "quote_gun.md" описан мой старый сервис без картинок.
Напиши сервис "deckhub" по типу "quote_gun" только для перечисленных id. 
Пусть сервис при запросе http://127.0.0.1:8005/chinese возвращает одну (не десять) "карточку". Картинку, а внизу текст из поля "text"
Оформление и инфраструктурные вещи вроде systemd и nginx файлов сделать по типу quote_gun