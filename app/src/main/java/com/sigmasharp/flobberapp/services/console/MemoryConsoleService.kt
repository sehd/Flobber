package com.sigmasharp.flobberapp.services.console

class MemoryConsoleService : ConsoleService {
    private val items= arrayListOf<String>()

    override fun addNormal(text: String) {
        items.add(text)
    }

    override fun getItems() :ArrayList<String>{
        return items
    }
}