package com.sigmasharp.flobberapp.services.console

class MemoryConsoleService : ConsoleService {
    private val items= arrayListOf<ConsoleItem>()

    override fun log(content:String,type:ConsoleItemType){
        items.add(ConsoleItem(content,type))
    }

    override fun addNormal(text: String) {
        items.add(ConsoleItem(text,ConsoleItemType.Normal))
    }

    override fun addWarning(text: String) {
        items.add(ConsoleItem(text,ConsoleItemType.Warning))
    }

    override fun addError(text: String) {
        items.add(ConsoleItem(text,ConsoleItemType.Error))

    }

    override fun getItems() :ArrayList<ConsoleItem>{
        return items
    }
}