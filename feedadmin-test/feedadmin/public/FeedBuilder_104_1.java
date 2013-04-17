import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Iterator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import MyUtil.MceException;

import xce.feed.FeedTypeConfigNotFoundException;
import xce.feed.NotAllowedToSendException;
import xce.feed.FeedReply;
/**
 * 此FeedBuilder_104_1用于构建发送stype为104，数据版本为1的新鲜事
 * 新鲜事说明：测试2
 * @author antonio
 *
 */

class FeedBuilder_104_1 {
	/**新鲜事的类型*/
	public final static int stype = 104;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
    private List< Map<String,String> > url_list = new ArrayList< Map<String,String> >();
  
    private List< Map<String,String> > buddylist_buddy_name_name2_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_104_1 () {
    
        _flag.put("blogid" , false);
        _flag.put("user.id" , true);
        _flag.put("user.name" , false);
        _flag.put("buddylist.buddy.id" , false);
        _flag.put("url2" , false);
        _flag.put("photo" , true);

    
        _flag.put("url" , false);
        _flag.put("buddylist.buddy.name.name2" , false);

    
	_flag.put("expr",false);
    
  }

  boolean CheckUrl(String url) {
	  if(url.isEmpty()){
		return true;
	  }
	  Pattern p = Pattern
		  .compile("^http://[^#]+$");
	  Matcher m = p.matcher(url);
	  if (m.find()) {
		  return true;
	  }
	  System.err.println("URL格式不正确 url:"+url);
	  return false;
  }

   
   public boolean AddExpr(String expr) {
		Pattern p = Pattern
				.compile("^[ufaApsvgzx]{1}\\([1-9]+[0-9]*\\)([\\+\\-\\&]{1}[ufaApsvgzx]{1}\\([1-9]+[0-9]*\\))*$");
		Matcher m = p.matcher(expr);
		if (m.find()) {
			_data.put("expr", expr);
			_flag.put("expr", true);
			return true;
		}
		System.err.println("分发表达式 expr="+expr+",设置的值无效");
		return false;
   }
   

  
  /**
   *@param blogid comment:日志流水号ID
   */
  public void SetKey_blogid( long  blogid){
    
    _data.put("blogid", String.valueOf( blogid ) );
    _flag.put("blogid",true);
  }
  
  /**
   *@param user_id comment:用户ID
   */
  public void SetKey_user_id( long  user_id){
    
    _data.put("user.id", String.valueOf( user_id ) );
    _flag.put("user.id",true);
  }
  
  /**
   *@param user_name comment:用户名
   */
  public void SetKey_user_name( String  user_name){
    
    if(!CheckUrl(user_name )){
    	_flag.put("user.name",false);
    	return;
    }
    
    _data.put("user.name", String.valueOf( user_name ) );
    _flag.put("user.name",true);
  }
  
  /**
   *@param buddylist_buddy_id comment:buddyid
   */
  public void SetKey_buddylist_buddy_id( String  buddylist_buddy_id){
    
    if(!CheckUrl(buddylist_buddy_id )){
    	_flag.put("buddylist.buddy.id",false);
    	return;
    }
    
    _data.put("buddylist.buddy.id", String.valueOf( buddylist_buddy_id ) );
    _flag.put("buddylist.buddy.id",true);
  }
  
  /**
   *@param url2 comment:test url
   */
  public void SetKey_url2( String  url2){
    
    if(!CheckUrl(url2 )){
    	_flag.put("url2",false);
    	return;
    }
    
    _data.put("url2", String.valueOf( url2 ) );
    _flag.put("url2",true);
  }
  
  /**
   *@param photo comment:test
   */
  public void SetKey_photo( String  photo){
    
    _data.put("photo", String.valueOf( photo ) );
    _flag.put("photo",true);
  }
  

  
  /**
   *@param url comment:用户的URL
   */
  public void AddRepeat_url(
    
	 String 
	 
	url
    
  ){
    _flag.put("url",false);
    
         if(!CheckUrl(url)){return;}
        
         



      int count = url_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      obj.put("url."+ String.valueOf(count),String.valueOf(url));
      url_list.add(obj);
     _flag.put("url",true);
  }
  
  /**
   *@param buddylist_buddy_name_name2 comment:name
   */
  public void AddRepeat_buddylist_buddy_name_name2(
    
	 String 
	 
	buddylist_buddy_name_name2
    
  ){
    _flag.put("buddylist.buddy.name.name2",false);
    
        
         



      int count = buddylist_buddy_name_name2_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      obj.put("buddylist.buddy.name.name2."+ String.valueOf(count),String.valueOf(buddylist_buddy_name_name2));
      buddylist_buddy_name_name2_list.add(obj);
     _flag.put("buddylist.buddy.name.name2",true);
  }
  
  

  
  void MergeData(){
    
      for(int i = 0; i < url_list.size(); ++i){
        _data.putAll(url_list.get(i));
      }
    
      for(int i = 0; i < buddylist_buddy_name_name2_list.size(); ++i){
        _data.putAll(buddylist_buddy_name_name2_list.get(i));
      }
    
  }
  
	  /**
	   *调用此方法触发产生新鲜事，用于产生带回复的新鲜事，所以需要传FeedReply参数
	   */
	  public void DispatchFeed(FeedReply reply) {
		  StringBuffer buf = new StringBuffer();

		  Iterator it = _flag.entrySet().iterator();
		  while(it.hasNext()){
			  Map.Entry<String, Boolean> entry = (Map.Entry<String, Boolean>)it.next(); 
			  if(!entry.getValue()){
				  if(buf.length() == 0){
					  buf.append("Any SetKey function not set, include keys:").append(entry.getKey());
				  }else{
					  buf.append(",").append(entry.getKey());
				  }

			  }
		  }
		  if(buf.length() > 0){
			  System.err.println(buf.toString());
			  return;
		  }
  	
		MergeData();
	
		  try {
			if(reply == null){
			  FeedCreatorAdapter.getInstance().Create(stype, version, _data);
			}else{
			  FeedCreatorAdapter.getInstance().CreateWithReply(stype, version, _data, reply);
			}

		  } catch (FeedTypeConfigNotFoundException e) {
			  e.printStackTrace();
		  } catch (NotAllowedToSendException e) {
			  // TODO Auto-generated catch block
			  e.printStackTrace();
		  } catch (MceException e) {
			  // TODO Auto-generated catch block
			  e.printStackTrace();
		  }
	  }
	/**
	* 调用此方法触发产生新鲜事
	*/
	public void DispatchFeed(){
		DispatchFeed(null);
	}
}
