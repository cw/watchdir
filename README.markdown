#  watchdir.py [github.com/cw/watchdir](https://github.com/cw/watchdir) #

watch given directory for changes. zip changed files and upload zip file to
given URL.

config.ini is expected to exist in the same directory as watchdir.py.

config.ini is expected to have a single group called [settings]

the [settings] group is expected to contain two config options called `url` and `directory`.

the `directory` option specifies which directory to watch.

the `url` option specifies which url to notify when a change is detected to `directory`
