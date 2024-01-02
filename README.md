# Приложение создает краткое содержимое из текста на английском языке

Задание по дисциплине программная инженерия магистратуры "Инженерия машинного обучения".

## Установка

`$ pip install -r requirements.txt`

## Запуск

`$ uvicorn main:app`

## Документация API

http://127.0.0.1:8000/docs

## Пример использования

### Запрос

`curl -X 'POST' \
'http://127.0.0.1:8000/shorten_text/' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"original_text": " An enormous sea snake from Norse legend that was fathered by the trickster god Loki and grew big enough to circle the globe is now the namesake for a different type of “monster” — a newly discovered species of a massive, meat-eating marine reptile known as a mosasaur, which lived about 80 million years ago.Paleontologists recently described the previously unknown mosasaur from fossils found near the North Dakota town of Walhalla. The town’s name comes from Valhalla, the feasting hall of Norse mythology where dead heroes gather, so the scientists dubbed the mosasaur Jormungandr walhallaensis. Its name references Norse myths of Jǫrmungandr, the Midgard Serpent, as well as the site of the fossil’s discovery, the researchers reported Monday in the journal Bulletin of the American Museum of Natural History.Repenomamus robustus attacks Psittacosaurus lujiatunensis moments before a volcanic debris flow buries them both, ca. 125 million years ago.‘Once in a lifetime’ fossil reveals a dinosaur and mammal locked in mortal combatThe fossil itself has a somewhat less poetic name: NDGS 10838. It includes a near-complete skull with a bony ridge over the eyes as well as jaws and some skeletal parts, including 11 ribs and 12 vertebrae. In life, the animal would have measured about 24 feet (7.3 meters) long and had a long face slimmer than those of its mosasaur cousins, said lead study author Amelia Zietlow, a paleontologist and doctoral candidate at the American Museum of Natural History’s Richard Gilder Graduate School in New York City.In general, Jormungandr walhallaensis resembled most mosasaurs — “kind of like if you took a Komodo dragon, made it 30 feet long and gave it flippers and a shark tail,” Zietlow told CNN.Yet in other ways, the animal was one of a kind. A mix of features in the bones of its skull made it unexpectedly challenging for the scientists to classify the newcomer and hinted that the mosasaur group includes more diverse forms than expected, the study authors reported."
}'`

### Ответ

`{
"short_text": "Paleontologists recently described the previously unknown mosasaur from fossils found near the North Dakota town of Walhalla. The town’s name comes from Valhalla, the feasting hall of Norse mythology where dead heroes gather. In life, the animal would have measured about 24 feet (7.3 meters) long and had a long face slimmer than those of its Mosasaur cousins."
}`
