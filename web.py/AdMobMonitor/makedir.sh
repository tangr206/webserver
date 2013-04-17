#!/bin/sh
cd 'AdMobMonitor/'
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
for dir in $dir_arr
  do
  if [ ! -d "$dir" ]; then
    mkdir -p $dir
  fi
  done
