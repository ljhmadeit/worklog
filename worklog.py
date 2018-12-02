import sys
import subprocess
import traceback
import re
import psutil
import time

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

output = sys.stdout

debug = False

def log(output):
    if debug:
        sys.stderr.write("%s log start\n" % (get_date()));

    try:
        window = get_current_window()
        if not window:
            sys.stderr.write('failed to get window\n')
            return True

        format = 'a4'
        output.write("%s %s %s %s %s %s\n" % (
            format, get_ip(), get_ssid(), get_date(),
            get_name(window.get_pid()), window.get_name()))
        output.flush()
        if debug:
            sys.stderr.write("%s log success\n" % (get_date()));
    except Exception:
        traceback.print_exc(file=sys.stderr)

    return True

def get_ssid():
    arg='iwconfig'    
    ssid = None
    p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE, stderr=None)
    for line in p.communicate():
        if line:
            match = re.search('ESSID:"(.*)"', line.decode('utf-8'))
            if match:
                ssid = match.groups()[0]

    if ssid:
        ssid = ssid.replace(' ', '+')
        return ssid
    else:
        return '-'

def get_name(pid):
    return [ps.name() for ps in list(psutil.process_iter()) if ps.pid == pid][0]

def get_date():
    return time.strftime('%Y/%m/%d-%H:%M', time.localtime())

def get_current_window():
    try:
        return Wnck.Screen.get_default().get_active_window()
    except AttributeError:
        traceback.print_exc(file=sys.stderr)
        return False

def get_ip():
    #Use ip route list
    try:
        arg = 'ip route list'    
        p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
        data = p.communicate()
        sdata = data[0].split()
        ipaddr = sdata[ sdata.index('src')+1 ]
        return ipaddr
    except Exception:
        traceback.print_exc(file=sys.stderr)
        return '-'

    # netdev = sdata[ sdata.index('dev')+1 ]
    
GObject.timeout_add(60 * 1000, log, output) # 60sec
Gtk.main()
