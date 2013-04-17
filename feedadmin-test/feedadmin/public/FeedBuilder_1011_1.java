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
 * 此FeedBuilder_1011_1用于构建发送stype为1011，数据版本为1的新鲜事
 * 新鲜事说明：用户收听人人电台
 * @author antonio
 *
 */

class FeedBuilder_1011_1 {
	/**新鲜事的类型*/
	public final static int stype = 1011;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
    private List< Map<String,String> > listener_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_1011_1 () {
    
        _flag.put("time" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("radio.id" , false);
        _flag.put("radio.name" , false);
        _flag.put("radio.img" , false);
        _flag.put("radio.url" , false);
        _flag.put("radio.desc" , false);

    
        _flag.put("listener" , false);

    
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

   

  
  /**
   *@param time comment:时间戳
   */
  public void SetKey_time( long  time){
    
    _data.put("time", String.valueOf( time ) );
    _flag.put("time",true);
  }
  
  /**
   *@param from_id comment:触发者id
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:触发者姓名
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_tinyimg comment:触发者头像
   */
  public void SetKey_from_tinyimg( String  from_tinyimg){
    
    _data.put("from.tinyimg", String.valueOf( from_tinyimg ) );
    _flag.put("from.tinyimg",true);
  }
  
  /**
   *@param radio_id comment:电台id
   */
  public void SetKey_radio_id( long  radio_id){
    
    _data.put("radio.id", String.valueOf( radio_id ) );
    _flag.put("radio.id",true);
  }
  
  /**
   *@param radio_name comment:电台名称
   */
  public void SetKey_radio_name( String  radio_name){
    
    _data.put("radio.name", String.valueOf( radio_name ) );
    _flag.put("radio.name",true);
  }
  
  /**
   *@param radio_img comment:电台图片
   */
  public void SetKey_radio_img( String  radio_img){
    
    _data.put("radio.img", String.valueOf( radio_img ) );
    _flag.put("radio.img",true);
  }
  
  /**
   *@param radio_url comment:电台链接
   */
  public void SetKey_radio_url( String  radio_url){
    
    if(!CheckUrl(radio_url )){
    	return;
    }
    
    _data.put("radio.url", String.valueOf( radio_url ) );
    _flag.put("radio.url",true);
  }
  
  /**
   *@param radio_desc comment:电台描述（xxxx人收听）
   */
  public void SetKey_radio_desc( String  radio_desc){
    
    _data.put("radio.desc", String.valueOf( radio_desc ) );
    _flag.put("radio.desc",true);
  }
  

  
  /**
   *@param listener comment:打开人人电台的人（实际上就是触发者，用于合并）
   */
  public void AddRepeat_listener(
    
	
	
		
          		
			 
			 String 
			  
			name
		
	
		
	
		
	
		
          		, 
			 long   
			id
		
	
		
          		, 
			 String 
			  
			url
		
	
    
  ){
    
        
                
                        
                
        
                
        
                
        
                
                        
                
        
                
                         if(!CheckUrl(url)){return;}
                        
                
        
         



      int count = listener_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      
          obj.put("listener."+String.valueOf(count)+".name", String.valueOf(name ));
          obj.put("listener."+String.valueOf(count)+".id", String.valueOf(id ));
          obj.put("listener."+String.valueOf(count)+".url", String.valueOf(url ));
     
      listener_list.add(obj);
     _flag.put("listener",true);
  }
  
  

  
  void MergeData(){
    
      for(int i = 0; i < listener_list.size(); ++i){
        _data.putAll(listener_list.get(i));
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
