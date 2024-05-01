<div align="center">

# Traffic Accident backend ML Documentation

</div>

---

-  #### Request

```bash
    POST /forecast
```

Example request

```json
{
	"model_id": 0,
	"options": {
		"temperature": 1.9,
		"atmospheric_pressure": 752.4,
		"humidity": 96,
		"wind_speed": 2,
		"cloudiness": 1.0,
		"hour": 12,
		"season_autumn": 0,
		"season_spring": 0,
		"season_summer": 0,
		"season_winter": 1
	}
}
```

Example response

```json
{
	"model_name": "RandomForestClassifier",
	"model_ru_name": "Случайный лес",
	"predicted_class": 1,
	"predicted_probabilities": [0.2690662494364746, 0.7309337505635257],
	"success": true
}
```

Example error

```json
{
	"message": "Что-то пошло не так!",
	"success": false
}
```

-  #### Request

```bash
    GET /forecast
```

Example response

```json
[
	{
		"id": 0,
		"name": "RandomForestClassifier",
		"ru_name": "Случайный лес"
	},
	{
		"id": 1,
		"name": "RandomForestClassifierOLD",
		"ru_name": "Случайный лес старый"
	},
	{
		"id": 2,
		"name": "RandomForestClassifierTPOT",
		"ru_name": "Случайный лес TPOT"
	}
]
```
