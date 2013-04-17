#!/bin/bash

date=`date  +%Y-%m-%d-%H`
echo $date


python /data/xce/MONITOR/webserver/AdWebPlatform/AdEdmSenderMonitor/history/bin/AdEdmSenderMonitor_rong.py >> /data/xce/MONITOR/webserver/AdWebPlatform/AdEdmSenderMonitor/history/data/res.$date
