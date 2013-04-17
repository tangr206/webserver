#echo $1" "$2
#ssh -T fei.yuan@10.5.18.232 "cd /home/fei.yuan/HadoopStat/bin&&sh dispatch.sh $1 $2" > log 2>&1
#ssh -T fei.yuan@10.5.18.232 "cat /home/fei.yuan/data/dispatch/res.$1"

i=1
while [ $i -le "10" ];do
	time=`date +'%Y-%m-%d' -d "$i days ago"`
	i=$(($i+1))
	#echo $time
	sql="select date,dispatch,tosize,dispatch_user,view,view_user,reply,reply_user,click,click_user from feed_stat_total where date='$time'"
	res=`echo $sql|mysql -h10.22.202.217 -ufeed -pfeed -Dfeed_stat|sed '1d'`
	c=`echo $res|wc -w`
	if [ $c -le "5" ]
	then
		continue
	fi
	echo $res
	#sed '1d' /tmp/totalreply > /tmp/totalreply1
done

#"	</table>
#"
#date dispatch tosize dispatch_user view reply reply_user click click_user
#echo $res
