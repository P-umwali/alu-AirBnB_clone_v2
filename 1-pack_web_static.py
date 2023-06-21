#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder."""
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = 'web_static_' + now + '.tgz'
    archive_path = 'versions/' + archive_name

    # Create the versions folder if it doesn't exist
    local('mkdir -p versions')

    # Compress the web_static folder into a .tgz archive
    result = local('tar -czvf {} web_static'.format(archive_path))

    if result.failed:
        return None

    return archive_path

