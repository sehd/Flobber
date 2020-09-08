package com.sigmasharp.flobberapp.services.logger

interface Logger {
    fun log(text:String,type:LogItemType=LogItemType.Normal)
    fun addNormal(text:String)
    fun addWarning(text:String)
    fun addError(text:String)
    fun getItems() :ArrayList<LogItem>
    fun setLogAddedCallBack(callback:LogAddedCallback )
}

