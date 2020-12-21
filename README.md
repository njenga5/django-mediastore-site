# About Project Intranetsite
Intranetsite is a project undertaken as a process of learning Django framework. It basically is an online media storage bucket. It can store images, music files and video files. It also provides an online gallery, video and audio players for preview.

## Basic setup 
1. Clone the repository, cd into django-mediastore-site/intranetsite and activate a virtual environment.
2. Run pip install -r requirements.txt.
3. Run the migrations.
4. Set debug to True in settings.py
5. Spin up the django development server.
6. Visit http://localhost:8000/.
7. Explore!.

## Keep in mind
-> The secret key is provided in plain text for this to work out of the box.
-> The databases should be set up by default but in case you have the same keys used here in your   environment variables modify your database accordingly.
-> You can also configure the email section to point to your smtp provider.Default is localhost on port 8025.
->(if using localhost) For this to work, run the following command to start a dummy debugging server
    python -m smtpd -n -c DebuggingServer localhost:8025
-> You have to upload a file to play or view it.

## Known issues
The video player is not very responsive in mobile and small screen devices.
