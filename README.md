# pandapush

Basic tool to send text from device to dropbox file.

Soon to be added:
  - multi-device push feature through an application
  - security, keeping the application simple, and adding the option to encrypt the file hosted on dropbox
  
Future goal is to mimic the likes of applications such as pushbullet, KDE connect, and etc. This could still be possible to do while using dropbox, but files should be able to stored elsewhere with the addition of security.

# dbx
This is the csv initialization and dropbox api connection. The purpose of this is to first create as .csv which serves as a dropbox "mini database." This could have as easily been a local .csv or sqlite file, or anything for that matter. But using dropbox allows for multi-device access. This file follows the format:

    import dropbox

    TOKEN = 'your_token'

    dbx = dropbox.Dropbox(TOKEN)

    def init_doc(f):
        dbx.files_upload(f.read(),path='/file_name.csv', mode=dropbox.files.WriteMode("overwrite"))
