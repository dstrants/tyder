import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError
try:
    from settings import set_file
except ImportError:
    print('Tyder is not set up. Run setup.py to get started')
    sys.exit()
PROJECT = set_file['project']
LOCALFILE = set_file['backup_file']
BACKUPPATH = '/%s/%s' % (PROJECT, LOCALFILE.split('/')[-1])
dbx = dropbox.Dropbox(set_file['dropbox_token'])


def backup():
    with open(LOCALFILE, 'rb') as f:
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()


if set_file['path_type'] == 'file':
    backup()
