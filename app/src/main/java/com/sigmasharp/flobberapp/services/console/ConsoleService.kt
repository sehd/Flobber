package com.sigmasharp.flobberapp.services.console

interface ConsoleService {
    fun addNormal(text:String)
    fun getItems() :ArrayList<String>
}