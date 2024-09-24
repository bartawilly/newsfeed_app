
# Newsfeed App

A simple newsfeed application built with Flask and MySQL. The app allows users to create, read, update, and delete posts.

## Features
- Add new posts
- Update existing posts
- Delete posts
- View posts

## Prerequisites
- Python 3.x
- MySQL Server
- Git

## Installation

### Clone the repository:

```bash
git clone https://github.com/bartawilly/newsfeed_app.git
cd newsfeed_app
```

### Create a virtual environment:

```bash
python -m venv venv
```

### Activate the virtual environment:

- For Windows:
  ```bash
  venv\Scripts\activate
  ```

- For macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Install the dependencies:

```bash
pip install Flask mysql-connector-python
```

### Set up the database:

1. Create a MySQL database named `newsfeed_db`.
2. Run the SQL script to create the tables:

   ```bash
   mysql -u your_username -p newsfeed_db < schema.sql
   ```

### Configure the application:

1. Copy the sample configuration file:

   ```bash
   copy config.py.sample config.py  # For Windows
   cp config.py.sample config.py     # For macOS/Linux
   ```

2. Edit `config.py` and update your database credentials.

## Running the Application

### Start the app:

```bash
python run.py
```

### Access the app:

Open your browser and navigate to `http://127.0.0.1:5000/`. You should see:

```css
Welcome to Newsfeed APP
```

## API Endpoints

### GET `/`

Returns a welcome message.

### POST `/posts`

Create a new post.

#### Request body:

```json
{
  "user_id": 1,
  "content": "Your post content"
}
```

### GET `/posts/<post_id>`

Retrieve a post by its ID.

### PUT `/posts/<post_id>`

Update a post.

#### Request body:

```json
{
  "content": "Updated post content"
}
```

### DELETE `/posts/<post_id>`

Delete a post by its ID.

## Additional Notes

- Make sure your MySQL server is running before starting the application.
