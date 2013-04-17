ps aux | grep feedadmin-test.ini$ | awk '{print $2}' | xargs kill -9
