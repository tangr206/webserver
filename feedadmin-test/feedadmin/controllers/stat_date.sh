#echo $1" "$2
#ssh -T fei.yuan@10.5.18.232 "cd /home/fei.yuan/HadoopStat/bin&&sh dispatch.sh $1 $2" > log 2>&1
#ssh -T fei.yuan@10.5.18.232 "cat /home/fei.yuan/data/dispatch/res.$1"
#ssh -T xce@f87.xce.d.xiaonei.com "ls"


echo $sql
#sql="select date, stype, sum(dispatch) as c from feed_stat_stype where date='2012-04-16' group by date, stype order by c desc"
i=1
trs=""
#while [ $i -le "2" ];do
	#time=`date +'%Y-%m-%d' -d "$i days ago"`
	#i=$(($i+1))
	#echo $time
	sql="select date,stype,sum(dispatch),sum(tosize),sum(dispatch_user),sum(view),sum(reply),sum(reply_user),sum(click),sum(click_user) from feed_stat_stype  where date='$1' group by date,stype order by sum(dispatch) desc"
	echo $sql|mysql -h10.22.202.217 -ufeed -pfeed -Dfeed_stat
	c=`echo $res|wc -w`
	if [ $c -le "5" ]
	then
		continue
	fi
	#echo $res
	#sed '1d' /tmp/totalreply > /tmp/totalreply1
#done

#"	</table>
#"
#echo $res
