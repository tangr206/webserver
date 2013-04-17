#!/bin/sh
#ICE_HOME=/opt/Ice-3.3/
#export LD_LIBRARY_PATH=$ICE_HOME/lib:$HOME/mob/share_lib:.
path=$(pwd)

config_file="shpy/config"
function GetKey(){
    section=$(echo $1 | cut -d '.' -f 1)
    key=$(echo $1 | cut -d '.' -f 2)
    sed -n "/\[$section\]/,/\[.*\]/{
     /^\[.*\]/d
     /^[ \t]*$/d
     /^$/d
     /^#.*$/d
     s/^[ \t]*$key[ \t]*=[ \t]*\(.*\)[ \t]*/\1/p
    }" $config_file
}

#读取ip构建路径
ip=$(GetKey "global.ip")
dir_arr="$path/$ip/get_ad_log/ $path/$ip/ad_index_log/brand_index_log/ $path/$ip/ad_index_log/self_index_log/ $path/$ip/rotate_group_log/ $pa
th/$ip/cache_log/"
pythonpath=$(GetKey "global.pythonbin")
for dir in $dir_arr
  do
  if [ ! -d "$dir" ]; then
    mkdir -p $dir
  fi
  done
#echo $path
#echo $pythonpath
$pythonpath/python shpy/AdMobCache.py
#$pythonpath/python shpy/AdMobTest.py >> $ip/get_ad_log/get_ad_log.log 2>&1
$pythonpath/python shpy/AdMobBrandIndex.py 100000000103 >> $ip/ad_index_log/brand_index_log/brand_index.log 2>&1
$pythonpath/python shpy/AdMobBrandIndex.py 100000000104 >> $ip/ad_index_log/brand_index_log/brand_index.log 2>&1
$pythonpath/python shpy/AdMobBrandIndex.py 100000000099 >> $ip/ad_index_log/brand_index_log/brand_index.log 2>&1
$pythonpath/python shpy/AdMobSelfIndex.py 100000000103 >> $ip/ad_index_log/self_index_log/self_index.log 2>&1
$pythonpath/python shpy/AdMobSelfIndex.py 100000000104 >> $ip/ad_index_log/self_index_log/self_index.log 2>&1
$pythonpath/python shpy/AdMobSelfIndex.py 100000000099 >> $ip/ad_index_log/self_index_log/self_index.log 2>&1
$pythonpath/python shpy/AdMobRotate.py 100000000103 >> $ip/rotate_group_log/rotate_group.log 2>&1
$pythonpath/python shpy/AdMobRotate.py 100000000104 >> $ip/rotate_group_log/rotate_group.log 2>&1
$pythonpath/python shpy/AdMobRotate.py 100000000099 >> $ip/rotate_group_log/rotate_group.log 2>&1
