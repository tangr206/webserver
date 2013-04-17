import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Iterator;

import MyUtil.MceException;

import xce.feed.FeedTypeConfigNotFoundException;
import xce.feed.NotAllowedToSendException;
import xce.feed.FeedReply;
/**
 * 此FeedBuilder_102_3用于构建发送stype为102，数据版本为3的新鲜事
 * 新鲜事说明：测试类型
 * @author antonio
 *
 */

class FeedBuilder_102_3 {
	/**新鲜事的类型*/
	public final static int stype = 102;
	/**新鲜事的版本号*/
	public final static int version = 3;

	
  
    private List< Map<String,String> > url_list = new ArrayList< Map<String,String> >();
  
    private List< Map<String,String> > owner_fav_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_102_3 () {
    
        _flag.put("time" , false);
        _flag.put("owner.id" , false);

    
        _flag.put("" , false);
        _flag.put("" , false);

    
  }

   

  
  /**
   *@param time comment:dd
   */
  public void SetKey_time( long  time){
    _data.put("time", String.valueOf( time ) );
    _flag.put("time",true);
  }
  
  /**
   *@param owner_id comment:v
   */
  public void SetKey_owner_id( String  owner_id){
    _data.put("owner.id", String.valueOf( owner_id ) );
    _flag.put("owner.id",true);
  }
  

  
  /**
   *@param url comment:
   */
  public void AddRepeat_url(
    
	 String 
	 
	url
    
  ){
      int count = url_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      obj.put("."+ String.valueOf(count),String.valueOf(url));
      url_list.add(obj);
     _flag.put("",true);
  }
  
  /**
   *@param owner_fav comment:
   */
  public void AddRepeat_owner_fav(
    
	 String 
	 
	owner_fav
    
  ){
      int count = owner_fav_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      obj.put("."+ String.valueOf(count),String.valueOf(owner_fav));
      owner_fav_list.add(obj);
     _flag.put("",true);
  }
  
  

  
  void MergeData(){
    
      for(int i = 0; i < url_list.size(); ++i){
        _data.putAll(url_list.get(i));
      }
    
      for(int i = 0; i < owner_fav_list.size(); ++i){
        _data.putAll(owner_fav_list.get(i));
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
