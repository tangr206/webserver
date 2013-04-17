#!/bin/bash

date=`date  +%Y-%m-%d-%H`
echo $date


python /data/xce/MONITOR/webserver/AdWebPlatform/IndexServiceMonitor/history/bin/IndexService_rong.tang.py >> /data/xce/MONITOR/webserver/AdWebPlatform/IndexServiceMonitor/history/data/res.$date
