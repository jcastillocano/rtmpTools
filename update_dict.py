# -*- encoding:utf8 -*-
from threading import Thread
from rtmpSnoop import main_sniffer
from cStringIO import StringIO
import sys
import subprocess
import time

class Sniffer(Thread):

    def __init__(self, device='eth0'):
        Thread.__init__(self)
        self.device = device
        self.backup = sys.stdout

    def run(self):
        global results
        sys.stdout = StringIO()
        main_sniffer(self.device)
        results = sys.stdout.getValue()
        sys.stdout.close()
        sys.stdout = self.backup

if __name__ == '__main__':
    results = None
    # Params
    _device = 'usb0'
    _url = u'http://cinestrenostv.tv/ver-canales-nacionales-de-españa-online-en-directo/'
    print "Initializating sniffer"
    thr = Sniffer(_device)
    print "Starting sniffer"
    thr.start()
    print "Opening url in web browser"
    _proc = subprocess.Popen(['firefox', "%s" % _url], stdout=subprocess.PIPE)
    while not results:
        print "Waiting for results..."
        time.sleep(1)
    _proc.kill()
    print "Results", results

