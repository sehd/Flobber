package com.sigmasharp.flobberapp.services.console

interface ConsoleService {
    fun log(text:String,type:ConsoleItemType=ConsoleItemType.Normal)
    fun addNormal(text:String)
    fun addWarning(text:String)
    fun addError(text:String)
    fun getItems() :ArrayList<ConsoleItem>
}