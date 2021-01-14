# About Project Intranetsite
Intranetsite is a project undertaken as a process of learning Django framework.📚📚🐣 It basically is an online media storage bucket. It can store images, music files and video files. It also provides an online gallery, video and audio players for preview.

## Basic setup 🔧🔧
1. Clone the repository, cd into django-mediastore-site and activate a virtual environment.
2. Run <code>pip install -r requirements.txt.</code>
3. Set <code>Debug = True</code> in intranetsite/settings.py
4. Run the migrations.<code>python manage.py runserver</code>
5. Spin up the django development server.
6. Visit [link] http://localhost:8000/.
7. Explore!

## Keep in mind  👇
-> The secret key is provided in plain text for this to work out of the box. 🔑🔒<br/>
-> The databases should be set up by default but in case you have the same keys used here in your environment variables modify your database accordingly.<br/>
-> You can also configure the email section to point to your smtp provider.Default is localhost on port 8025.<br/>
-> (if testing on localhost) For this to work, run the following command to start a dummy debugging server<br/>
    <code>python -m smtpd -n -c DebuggingServer localhost:8025</code>
<br/>-> You have to upload a file to play or view it.😎😎

## Known issues
The video player is not very responsive in mobile and small screen devices.🔧🔨
