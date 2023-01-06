# sortter homework

## Running the app

```
docker compose up
```

This will expose a  host/port at

```
http://0.0.0.0:8088
```

## Endpoints

### About

* Path: `/`
* Method: `GET`
* Response payload:
  * `{author: Cameron Jones}`

### Support Requests

* Path: `/support_request`
* Method: `GET`
* Response payload: List of [SupportRequest](#SupportRequest) JSON objects

--

* Path: `/support_request`
* Method: `POST`
* Request payload: [SupportRequest](#SupportRequest) JSON object
* Response payload: None

Example:
```
curl --request POST \
  --url http://0.0.0.0:8088/support_request \
  --header 'Content-Type: application/json' \
  --data '{
	"first_name": "Jonny",
	"last_name": "Finland",
	"email": "homework@sortter.fi",
	"phone": "0000000000",
	"description": "This homework does not work"
}'
```

## SupportRequest JSON object
* `first_name` [string, required]
* `last_name` [string, required]
* `email` [string, required]
  * format = x@x.x
* `phone` [string, required]
  * format = either 10 digits, or 12 digits with a leading `+`, or 12 digits with a leading `0`. Spaces not permitted
* `description` [string, required]

Example:
```
{
	"first_name": "Cameron",
	"last_name": "Jones",
	"email": "cameronjones@sortter.fi",
	"phone": "0000000000",
	"description": "Shit's broken"
}
```