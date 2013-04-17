#!/bin/sh
today=`date +'%Y-%m-%d'`
yesterday=`date -d yesterday +'%Y-%m-%d'`
ago15=`date -d "15 days ago" +'%Y-%m-%d'`

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

#备份
find $path/$ip/ad_index_log/brand_index_log -name brand_index.log |xargs -i mv {} $path/$ip/ad_index_log/brand_index_log/brand_index.log.$yesterday
find $path/$ip/ad_index_log/self_index_log -name self_index.log |xargs -i mv {} $path/$ip/ad_index_log/self_index_log/self_index.log.$yesterday
find $path/$ip/rotate_group_log -name rotate_group.log |xargs -i mv {} $path/$ip/rotate_group_log/rotate_group.log.$yesterday 
find $path/$ip/get_ad_log -name get_ad_log.log |xargs -i mv {} $path/$ip/get_ad_log/get_ad_log.log.$yesterday 

#删除15天前的log
find $path/$ip/ad_index_log/brand_index_log -name brand_index.log.$ago15 |xargs -i rm {} -rf
find $path/$ip/ad_index_log/self_index_log -name self_index.log.$ago15 |xargs -i rm {} -rf
find $path/$ip/cache_log -name cache_log_${ago15}*.log |xargs -i rm {} -rf
find $path/$ip/rotate_group_log -name rotate_group.log.$ago15 |xargs -i rm {} -rf
find $path/$ip/get_ad_log -name get_ad_log.log.$ago15 |xargs -i rm {} -rf
