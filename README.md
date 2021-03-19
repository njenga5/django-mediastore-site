# About Project Intranetsite
Intranetsite is a fun, fullstack website made with the Django framework.📚📚🐣 It, basically, is an online media storage bucket. It can store images, music files and video files. It also provides an online gallery, video and audio players for preview.

## Basic setup 🔧🔧
 Clone the repository, cd into django-mediastore-site and activate a virtual environment.
 Run 
   ```bash
    pip install -r requirements.txt.
   ```
    
 Set 
  ```python 
    DEBUG = True
  ``` 
 in intranetsite/settings.py
 Make the migrations.

 ```bash
    python manage.py migrate
 ```
 Spin up the django development server.
 Visit http://localhost:8000/.
 Explore and enjoy!

## Keep in mind  👇
-> You need to configure your environment variables to have the necessary values for:<br />
<ul>
    <li>SECRET_KEY</li>🔑🔒
    <li>EMAIL Options</li>
</ul>
-> The databases should be set up by default but in case you have the same keys used here in your environment variables modify your databases section in intranetsite/settings.py accordingly.It will use sqlite.<br/>
-> You can also configure the email section to point to your smtp provider.Default is localhost on port 8025.<br/>
-> (if testing on localhost) For this to work, run the following command to start a dummy debugging server<br/>

```bash
   python -m smtpd -n -c DebuggingServer localhost:8025
```
<br/>-> You have to upload a file to play or view it.😎😎

## Contributing
Clone the repository, make your changes and make a pull request
