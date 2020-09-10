package com.sigmasharp.flobberapp.services.logger

class MemoryLogger : Logger {
    private val items = arrayListOf<LogItem>()
    private lateinit var callback: LogAddedCallback

    override fun log(text: String, type: LogItemType) {
        val item = LogItem(text, type)
        items.add(item)
        callback.logAdded(items.size - 1)
    }

    override fun addNormal(text: String) {
        log(text, LogItemType.Normal)
    }

    override fun addWarning(text: String) {
        log(text, LogItemType.Warning)
    }

    override fun addError(text: String) {
        log(text,LogItemType.Error)
    }

    override fun getItems() :ArrayList<LogItem>{
        return items
    }

    override fun setLogAddedCallBack(callback: LogAddedCallback) {
        this.callback=callback
    }
}