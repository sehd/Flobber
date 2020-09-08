package com.sigmasharp.flobberapp.services.logger

fun interface LogAddedCallback {
    fun logAdded(item: LogItem)
}