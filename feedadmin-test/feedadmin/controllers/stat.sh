#echo $1" "$2
#ssh -T fei.yuan@10.5.18.232 "cd /home/fei.yuan/HadoopStat/bin&&sh dispatch.sh $1 $2" > log 2>&1
#ssh -T fei.yuan@10.5.18.232 "cat /home/fei.yuan/data/dispatch/res.$1"
#ssh -T xce@f87.xce.d.xiaonei.com "ls"


echo $sql
#sql="select date, stype, sum(dispatch) as c from feed_stat_stype where date='2012-04-16' group by date, stype order by c desc"


head="	<div style=\"position:absolute;left:50%;margin-left:-600px;width:1200px;\">
        <table width=\"1200\" style=\"text-align:center;border:1px solid #cad9ea;color:#666;\">
	<tr style=\"height:30px;background-color:#EEE;font-weight:bold;\">
		<td width=\"10%\" style=\"border:1px solid #cad9ea;\">日期</td>
		<td width=\"13%\" style=\"border:1px solid #cad9ea;\">新鲜事条数</td>
		<td width=\"13%\" style=\"border:1px solid #cad9ea;\">分发给</td>
		<td width=\"14%\" style=\"border:1px solid #cad9ea;\">产生新鲜事的用户数</td>
		<td width=\"10%\" style=\"border:1px solid #cad9ea;\">曝光条次</td>
		<td width=\"14%\" style=\"border:1px solid #cad9ea;\">取新鲜事的用户数</td>
		<td width=\"10%\" style=\"border:1px solid #cad9ea;\">回复数</td>
		<td width=\"10%\" style=\"border:1px solid #cad9ea;\">回复的用户数</td>
		<td width=\"10%\" style=\"border:1px solid #cad9ea;\">点击数</td>
		<td width=\"10%\" style=\"border:1px solid #cad9ea;\">点击的用户数</td>

	</tr>
"
i=1
trs=""
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
	res=`echo $res | sed 's/ /<\/td><td style=\"border:1px solid #cad9ea;\">/g'`
	tmp="<tr><td style=\"border:1px solid #cad9ea;\">$res</td></tr>"
	trs="$trs$tmp"
	#sed '1d' /tmp/totalreply > /tmp/totalreply1
done
html="$head$trs</table></div>"

#"	</table>
#"
echo $html
#date dispatch tosize dispatch_user view reply reply_user click click_user
#echo $res
