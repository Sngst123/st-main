#!/bin/bash
mkdir -p attachments
cd attachments
for i in {1..20}
do
    filename="photo$i.jpg"
    curl -sSL https://picsum.photos/800/400 --output "$filename"
    echo "Загружено изображение $i: $filename"
done

echo "Загрузка изображений завершена!"

