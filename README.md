Installation
------------

Put the scripts in any directory and make the worklog script executable.

    $ mkdir -p ~/bin
    $ cp worklog.osa ~/bin
    $ cp worklog ~/bin
    $ chmod u+x ~/bin/worklog
    $ echo 'export PATH=$PATH:~/bin' >> ~/.bashrc

Open your cron table.

    $ crontab -e

Add this line in the table.

    * * * * * osascript ~/bin/worklog.osa >> ~/work.log

How to display the logs 
-----------------------

See the all logs.

    $ worklog

See the logs in the specific date.

    $ worklog 2012-01-01

See the logs in the specific period.

    $ worklog 2012-01-01 2012-01-06
    
Dependency
----------

* [mxDateTime](http://www.egenix.com/products/python/mxBase/mxDateTime/)
* psutil
* wnck

### Arch Linux

$ pacman -S python2-psutil python2-wnck python2-egenix-mx-base
