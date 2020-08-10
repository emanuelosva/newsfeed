# News Feed -- Backend

### About
A simple REST api to serve the backend service to the "**NewsFeed**" client build in REACT.
The api works with json-web-token authentication to access to routes and firebase storage and authentication for users info.

### Porpuse
- Make CRUD operations about the user information
- Get news info throgh a scraper implemented in xpath and send it to client

### Specifications
- The user can make sigup and storage his/her data
- The user can make login and acces to his/her data
- The user can subscribe to any news chanels
- The user can unsuscribe to any news chanel
- The api must send the info of the user to the client
- The api must send the principal 3 news of each chanel to wich the user is subscribed

### Work Instructions
In the backend dir route create a nuew python env
Run:

```bash
python3 -m venv .env
pip3 install -r requirements.txt
```

Each time you add a new package run:
```bash
pip3 freeze > requirements.txt
```

To start the server run the start.bash file
```bash
source start.bash
```

### API docs (Resume)

**Interactive documentation** 
Go to [docs](https://documenter.getpostman.com/view/11575536/T1LJkozg?version=latest)

##### Entities
- User:
```js
// Schema

{
  email: str, // The user email (index)
  username: str, // The user name
  password: str, // The user password
  subscriptions: [News] // The user subscriptions
}
```

- News:

```js
// Schema

{
  title: str, // The name of the new
  summary: str // Summary of new
  link_image: str // The url to news portrait
  link_article: str, // The url to site
}
```

##### End points

**Users**

> metjod: POST -- path: /users

Description: Add a news subscription to user subscriptions list
Body: { id: str, news_name: str }
Returns:
- Status: 201
- Type: Application/json
- Value:

```js
{
  "error": false,
  "message": "Suscribed"
}
```

> metjod: DELETE -- path: /users

Description: Remove a news subscription to user subscriptions list
Body: { id: str, news_name: str }
Returns:
- Status: 200
- Type: Application/json
- Value: 

```js
{
  "error": false,
  "message": "Unsuscribed"
}
```

> method: POST -- path: /users/signup

Description: Register a new user
Body: { name: str, email: str, password:str }
Returns:
- Status: 201
- Type: Application/json
- Value: 
```js
{
  "error": false,
  "message": "User created"
}
```

> method: POST -- path: /users/login

Description: Login a user
Body: { User schema }
Returns:
- Status: 201
- Type: Application/json
- Value: 

```js
{
  "data": {
    "token": str, // jwt
    "user": {
      "name": str,
      "password": "",
      "subscriptions": [str]
    }
  },
  "error": false,
  "message": "Logged"
}
```

**News**

> method: GET -- path: /news?news_name=valid_news_name

Description: Retrieve the news info
query - valid_news_name: str
valid_news_names:
- bbc
- el_universal
- new_york_times
Returns:
- Status: 200
- Type: Application/json
- Value: {

```js
{
  "data": {
    "copywrigt": "The info and it rigths belogns to https://www.nytimes.com",
    "info": [
      {
        "summary": str,
        "title": str,
        "link_article": str,
        "link_image": str
      },
      ...
  ],
  },
  "error": false,
  "message": "News Retrieved"
}
```
