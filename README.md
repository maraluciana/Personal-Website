# Personal-Website

### - You need to install:
#### Flask

```
pip install Flask
```

#### Dotenv
```
pip install python-dotenv
```

#### Ruby 
```
sudo apt-get install ruby-full
```

#### SASS
```
sudo gem install sass
```

### - Copy the content from .env.example to .env and configure the variables
LOGGING = 'true' for error message in contact form (debugging purpose)     
LOGGING = 'false' for basic message     

### - Compile the CSS file 

#### Go to the css folder

```
cd static/css
```

#### Compile the SASS file to CSS
```
sass main.scss main.css
```

### - Run personalwebsite.py

> If it worked, it should look like this (in visual studio code)

![image](https://user-images.githubusercontent.com/71257603/223697338-1e005930-d089-4bb6-9838-9193517312a9.png)

If you work directly in the terminal, use this command : 

```
python3 personalwebsite.py
```
> If it worked, it should look like this (in terminal)

![image](https://user-images.githubusercontent.com/71257603/223698870-ac72cf54-3415-456e-b2c9-cf8672ba81e6.png)

### Open http://localhost:5000

#### enjoy :D
