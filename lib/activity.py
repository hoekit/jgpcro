# activity.py

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

def activity_start():
    print("jgpcro: Ok, start logging start of activity")
    print("jgpcro: Done logging start of activity")

def activity_stop():
    print("jgpcro: Ok, start logging end of activity")
    print("jgpcro: Done logging end of activity")

def activity(task):
    if task == "start":
        activity_start()
    elif task == "stop":
        activity_stop()
    else:
        usage()

