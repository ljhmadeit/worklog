How to record worklog
---------------------

Add this into your crontab and log what you do with your Mac.

`* * * * * osascript /path/to/worklog.osa >> /path/to/work.log`

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
