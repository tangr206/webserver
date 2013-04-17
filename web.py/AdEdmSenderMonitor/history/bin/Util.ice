#ifndef UTIL_ICE
#define UTIL_ICE

module MyUtil
{
    exception MceException
    {
        string message;
    };
    
    exception NoSuchObjectException extends MceException {};
    exception NoSuchPropertyException extends MceException {};
    
    sequence<int> IntSeq;
    ["java:type:java.util.ArrayList"] sequence<int> IntList;
    sequence<IntSeq> IntSeqSeq;
    sequence<int> IntArray;
    sequence<long> LongSeq;
    sequence<long> LongArray;
    sequence<string> StrSeq;
    sequence<string> StringArray;
    
    dictionary<int, int> Int2IntMap;   
    dictionary<int, string> Int2StrMap; 
    dictionary<long, int> Long2IntMap;
    dictionary<long, long> Long2LongMap;
    dictionary<string, int> Str2IntMap;
    dictionary<string, long> Str2LongMap;
	
    dictionary<string, string> Str2StrMap;
    dictionary<string, string> PropertyMap;
    sequence<Str2StrMap> Str2StrMapSeq;
    
    dictionary<int, IntSeq> Int2IntSeqMap;     
};
#endif
