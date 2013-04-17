i=1
trs=""
while [ $i -le "2" ];do
	time=`date +'%Y-%m-%d' -d "$i days ago"`
	i=$(($i+1))
	echo $time
	sql="select date,stype,sum(dispatch),sum(tosize),sum(dispatch_user),sum(view),sum(reply),sum(reply_user),sum(click),sum(click_user) from feed_stat_stype  where date='$time' and stype=$1 group by date,stype"
	#echo $sql
	res=`echo $sql|mysql -h10.22.202.217 -ufeed -pfeed -Dfeed_stat`
	#res=`echo $sql|mysql -h10.22.202.217 -ufeed -pfeed -Dfeed_stat|sed '1d'`
	#c=`echo $res|wc -w`
	#if [ $c -le "5" ]
	#then
	#	continue
	#fi
	#echo $res
done
	#sed '1d' /tmp/totalreply > /tmp/totalreply1
